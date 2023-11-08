import matplotlib.pyplot as plt

# Data
batch_size_4_1 = [100.0, 50.0, 35, 60, 39, 32, 39, 53, 46, 32, 39, 50.0, 53, 46, 53, 46]
batch_size_4_2 = [100.0, 46.0, 57.0, 46.0, 46.0, 54.0, 32.0, 54.0, 43.0, 46.0, 43.0, 36.0, 43.0, 50.0, 46.0, 39.0, 46.0, 46.0, 36.0, 54.0, 57.0, 43.0, 43.0, 46.0, 54.0, 50.0, 54.0, 54.0, 43.0, 57.0, 68.0, 43.0, 50.0, 46.0, 43.0, 46.0, 29.0, 43.0, 46.0, 29.0, 36.0, 57.0, 54.0, 43.0, 54.0, 43.0, 39.0, 39.0, 50.0, 43.0, 36.0, 43.0, 32.0, 39.0, 54.0, 50.0, 46.0, 43.0, 39.0, 50.0, 46.0, 39.0, 43.0, 54.0, 50.0, 54.0, 43.0, 50.0, 57.0, 43.0, 32.0, 46.0, 50.0, 46.0, 39.0, 54.0]
batch_size_16 = [81.0, 57.0, 50.0, 54.0, 61.0, 54.0, 46.0, 59.0, 60.0, 51.0, 55.0, 51.0, 50.0, 46.0, 53.0, 48.0]
batch_size_24 = [71.0, 62.0, 62.0, 58.0, 60.0, 54.0, 60.0, 58.0, 58.0, 55.0, 61.0, 54.0, 57.0, 55.0, 61.0, 60.0, 59.0, 57.0, 58.0, 60.0, 52.0, 60.0, 61.0, 54.0, 57.0, 61.0, 60.0, 57.0, 58.0, 54.0, 58.0, 58.0, 61.0]
batch_size_64_1 = [72.0, 67.0, 65.0, 66.0, 67.0, 67.0, 60.0, 59.0, 57.0, 53.0, 60.0, 56.0, 59.0]
batch_size_64_2 = [72.0, 69.0, 66.0, 66.0, 64.0, 57.0, 59.0, 57.0, 56.0, 58.0, 59.0, 60.0, 53.0]

# Create the figure and plot the data
plt.figure(figsize=(12, 6))
plt.plot(batch_size_4_1, label='Batch Size 4 - Line 1', marker='o')
# plt.plot(batch_size_4_2, label='Batch Size 4 - Line 2', marker='o')
plt.plot(batch_size_16, label='Batch Size 16', marker='o')
plt.plot(batch_size_24, label='Batch Size 24', marker='o')
plt.plot(batch_size_64_1, label='Batch Size 64 - Line 1', marker='o')
plt.plot(batch_size_64_2, label='Batch Size 64 - Line 2', marker='o')

# Customize the plot
plt.xlabel('Data Points')
plt.ylabel('Reconstruction Accuracy')
plt.title('Reconstruction Accuracy vs. Data Points')
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
