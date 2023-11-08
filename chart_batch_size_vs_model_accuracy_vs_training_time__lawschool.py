import matplotlib.pyplot as plt

# | Batch Size | One-bit Encoding Accuracy | Binary Encoding Accuracy | Time to Converge (seconds)|
# |------------|---------------------------|--------------------------|---------------------------|
# | 1          | 88.67%                    | 87.99%                   | 44.72                     |
# | 2          | 88.62%                    | 88.30%                   | 26.23                     |
# | 4          | 88.81%                    | 88.53%                   | 12.93                     |
# | 8          | 88.84%                    | 88.48%                   | 6.69                      |
# | 16         | 88.69%                    | 88.45%                   | 3.39                      |
# | 32         | 88.93%                    | 88.41%                   | 1.63                      |
# | 64         | 88.87%                    | 88.50%                   | 0.96                      |
# | 128        | 88.74%                    | 87.77%                   | 0.51                      |

# Data
batch_size = [1, 2, 4, 8, 16, 32, 64, 128]
one_bit_accuracy = [88.67, 88.62, 88.81, 88.84, 88.69, 88.93, 88.87, 88.74]
binary_accuracy = [87.99, 88.30, 88.53, 88.48, 88.45, 88.41, 88.50, 87.77]
time_to_converge = [44.72, 26.23, 12.93, 6.69, 3.39, 1.63, 0.96, 0.51]

# Create subplots
plt.figure(figsize=(12, 4))

# Plot One-bit Encoding Accuracy
plt.subplot(131)
plt.plot(batch_size, one_bit_accuracy, marker='o', label='One-bit Encoding', color='blue')
plt.xlabel('Batch Size')
plt.ylabel('Accuracy (%)')
plt.title('One-bit Encoding Accuracy')
plt.grid(True)
plt.legend()

# Plot Binary Encoding Accuracy
plt.subplot(132)
plt.plot(batch_size, binary_accuracy, marker='o', label='Binary Encoding', color='green')
plt.xlabel('Batch Size')
plt.ylabel('Accuracy (%)')
plt.title('Binary Encoding Accuracy')
plt.grid(True)
plt.legend()

# Plot Time to Converge
plt.subplot(133)
plt.plot(batch_size, time_to_converge, marker='o', label='Time to Converge', color='red')
plt.xlabel('Batch Size')
plt.ylabel('Time (seconds)')
plt.title('Time to Converge')
plt.grid(True)
plt.legend()

plt.tight_layout()

# Display the graph
plt.show()
