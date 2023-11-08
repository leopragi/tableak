import torch
from attacks import invert_grad
from models import FullyConnected, FullyConnectedTrainer
from datasets import Lawschool, Lawschool_Binary, ADULT, ADULT_BINARY
from utils import get_acc_and_bac
import time

architecture_layout = [100, 100, 2]  # network architecture (fully connected)
n_local_epochs = 1
lr = 0.01
criterion = torch.nn.CrossEntropyLoss()

batch_sizes = [1, 2, 4, 8, 16, 32, 64, 128]

for dataset in [Lawschool(), Lawschool_Binary(), ADULT(), ADULT_BINARY()]:
    dataset.standardize()
    Xtrain, ytrain = dataset.get_Xtrain(), dataset.get_ytrain()
    for batch_size in batch_sizes:
        centeralized_net = FullyConnected(dataset.num_features, architecture_layout)
        optimizer = torch.optim.Adam(centeralized_net.parameters())
        centeralized_trainer = FullyConnectedTrainer(data_x=Xtrain.detach().clone(), data_y=ytrain.detach().clone(),
                                    optimizer=optimizer, criterion=criterion, verbose=False)
        start_time = time.time()
        centeralized_trainer.train(centeralized_net, n_local_epochs, batch_size, shuffle=False, reset=False)
        acc, bac = get_acc_and_bac(centeralized_net, dataset.get_Xtest(), dataset.get_ytest())
        print(f'Centeralized Client with batch size {batch_size}:  Acc: {acc * 100:.2f}%    BAcc: {bac * 100:.2f}% with time {str(round((time.time() - start_time), 2))} seconds')
