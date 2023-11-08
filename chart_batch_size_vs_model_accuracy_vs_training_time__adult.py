import matplotlib.pyplot as plt

# | Batch Size | One-bit Encoding Accuracy | Binary Encoding Accuracy | Time to Converge (seconds)|
# |------------|---------------------------|--------------------------|---------------------------|
# | 1          | 84.68%                    | 82.07%                   | 16.44                     |
# | 2          | 84.87%                    | 82.47%                   | 10.29                     |
# | 4          | 84.69%                    | 82.41%                   | 5.27                      |
# | 8          | 84.60%                    | 82.16%                   | 2.57                      |
# | 16         | 84.72%                    | 82.15%                   | 1.3                       |
# | 32         | 84.70%                    | 82.09%                   | 0.68                      |
# | 64         | 84.49%                    | 82.11%                   | 0.36                      |
# | 128        | 84.34%                    | 82.01%                   | 0.21                      |


# Data
batch_size = [1, 2, 4, 8, 16, 32, 64, 128]

one_bit_accuracy = [84.68, 84.87, 84.69, 84.60, 84.72, 84.70, 84.49, 84.34]
binary_accuracy = [82.07, 82.47, 82.41, 82.16, 82.15, 82.09, 82.11, 82.01]
time_to_converge = [16.44, 10.29, 5.27, 2.57, 1.3, 0.68, 0.36, 0.21]

# Create the figure and three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot One-bit Encoding Accuracy
ax1.plot(batch_size, one_bit_accuracy, marker='o', label='One-bit Encoding', color='blue')
ax1.set_xlabel('Batch Size')
ax1.set_ylabel('Accuracy (%)')
ax1.set_title('One-bit Encoding Accuracy')
ax1.grid(True)
ax1.legend()

# Plot Binary Encoding Accuracy
ax2.plot(batch_size, binary_accuracy, marker='o', label='Binary Encoding', color='green')
ax2.set_xlabel('Batch Size')
ax2.set_ylabel('Accuracy (%)')
ax2.set_title('Binary Encoding Accuracy')
ax2.grid(True)
ax2.legend()

# Plot Time to Converge
ax3.plot(batch_size, time_to_converge, marker='o', label='Time to Converge', color='red')
ax3.set_xlabel('Batch Size')
ax3.set_ylabel('Time (seconds)')
ax3.set_title('Time to Converge')
ax3.grid(True)
ax3.legend()

plt.tight_layout()

# Display the graph
plt.show()
