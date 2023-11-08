import torch
import numpy as np
import copy
from attacks import invert_grad
from models import FullyConnected, FullyConnectedTrainer
from datasets import Lawschool, Lawschool_Binary, ADULT, ADULT_BINARY
from utils import get_acc_and_bac
import time
from attacks import fed_avg_attack
from utils import match_reconstruction_ground_truth
import gc

n_clients_s = [ 16] 
max_client_dataset_size = 32
local_batch_size = 64
architecture_layout = [100, 100, 2]  # network architecture (fully connected)
n_local_epochs = 1
lr = 0.01
criterion = torch.nn.CrossEntropyLoss()

dataset = Lawschool()
dataset.standardize()
Xtrain, ytrain = dataset.get_Xtrain(), dataset.get_ytrain()

for n_clients in n_clients_s:
    reconstructions = []
    model_accuracy = []

    # now, instantiate a global neural network, that serves as initial copy of all client neural networks
    global_net = FullyConnected(dataset.num_features, architecture_layout)
    client_nets = [copy.deepcopy(global_net) for _ in range(n_clients)]

    trainloader = torch.utils.data.DataLoader(dataset, batch_size=local_batch_size, shuffle=True)
    last_params = global_net.parameters()

    data_list = [batch for batch in trainloader]

    round = 0

    for i in range(len(data_list)):
        data_x, data_y = data_list[i]
        client_net = client_nets[(i % n_clients)]

        attack = False
        if((i % n_clients) == 1):
            attack = True
            prev_x, prev_y = data_list[i - 1]
            per_client_ground_truth_data = [prev_x.detach().clone()]
            per_client_ground_truth_labels = [prev_y.detach().clone()]
            attacked_clients_params = [[param.clone().detach() for param in last_params]]

            per_client_best_scores = [None]
            per_client_best_reconstructions = [None]

            per_client_candidate_reconstructions, per_client_final_losses = fed_avg_attack(
                original_net=copy.deepcopy(client_net),
                attacked_clients_params=attacked_clients_params,
                attack_iterations=1500,
                attack_learning_rate=0.06,
                n_local_epochs=n_local_epochs,
                local_batch_size=local_batch_size,
                lr=lr,
                dataset=dataset,
                per_client_ground_truth_data=per_client_ground_truth_data,
                per_client_ground_truth_labels=per_client_ground_truth_labels,
                reconstruction_loss='cosine_sim',
                priors=None,
                epoch_matching_prior=None,
                initialization_mode='uniform',
                softmax_trick=False,
                gumbel_softmax_trick=False,
                sigmoid_trick=False,
                temperature_mode='constant',
                sign_trick=True,
                apply_projection_to_features=None,
                device=None
            )
            true_x_mixed, rec_x_mixed = dataset.decode_batch(per_client_candidate_reconstructions[0], standardized=True), dataset.decode_batch(prev_x.detach(), standardized=True)
            tolerance_map = dataset.create_tolerance_map()
            _, error_map, _, _ = match_reconstruction_ground_truth(true_x_mixed, rec_x_mixed, tolerance_map)
            reconstruction_accuracy = 100 * (1 - np.mean(error_map))

            reconstructions.append(reconstruction_accuracy.round());
            round = round + 1

            # print(f'Reconstruction accuracy: {reconstruction_accuracy:.1f}%')

        for last, client in zip(last_params, client_net.parameters()):
            client.data.copy_(last.data)

        optimizer = torch.optim.Adam(client_net.parameters())
        outputs = client_net(data_x)
        loss = criterion(outputs, data_y)
        grad = torch.autograd.grad(loss, client_net.parameters(), retain_graph=True)

        with torch.no_grad():
            for param, param_grad in zip(client_net.parameters(), grad):
                param -= lr * param_grad

        last_params = client_net.parameters()


        if attack:
            acc, bac = get_acc_and_bac(client_net, dataset.get_Xtest(), dataset.get_ytest())
            model_accuracy.append((acc * 100).round())
            # print(f'Client :{(i % n_clients) + 1}    Acc: {acc * 100:.2f}%    BAcc: {bac * 100:.2f}%')
            attack = False

        if round > 50: break

    print(f'No of nodes: {n_clients}')
    print(f'Reconstruction accuracy: {reconstructions}')
    print(f'Model accuracy: {model_accuracy}')

    del global_net
    del client_nets
    gc.collect()

# batch_sizes = [1, 2, 4, 8, 16, 32, 64, 128]

# for batch_size in batch_sizes:
#     centeralized_net = FullyConnected(dataset.num_features, architecture_layout)
#     optimizer = torch.optim.Adam(centeralized_net.parameters())
#     centeralized_trainer = FullyConnectedTrainer(data_x=Xtrain.detach().clone(), data_y=ytrain.detach().clone(),
#                                 optimizer=optimizer, criterion=criterion, verbose=False)
#     start_time = time.time()
#     centeralized_trainer.train(centeralized_net, n_local_epochs, batch_size, shuffle=False, reset=False)
#     acc, bac = get_acc_and_bac(centeralized_net, dataset.get_Xtest(), dataset.get_ytest())
#     print(f'Centeralized Client with batch size {batch_size}:  Acc: {acc * 100:.2f}%    BAcc: {bac * 100:.2f}% with time {str(round((time.time() - start_time), 2))} seconds')
