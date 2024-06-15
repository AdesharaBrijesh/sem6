import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases randomly in the range (-1, 1)
        self.W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
        self.b1 = np.random.uniform(-1, 1, (1, hidden_size))
        self.W2 = np.random.uniform(-1, 1, (hidden_size, output_size))
        self.b2 = np.random.uniform(-1, 1, (1, output_size))

    def forward(self, X):
        # Forward propagation
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, learning_rate):
        # Backward propagation
        delta2 = (self.a2 - y) * sigmoid_derivative(self.a2)
        delta1 = np.dot(delta2, self.W2.T) * sigmoid_derivative(self.a1)

        # Update weights and biases
        self.W2 -= learning_rate * np.dot(self.a1.T, delta2)
        self.b2 -= learning_rate * np.sum(delta2, axis=0, keepdims=True)
        self.W1 -= learning_rate * np.dot(X.T, delta1)
        self.b1 -= learning_rate * np.sum(delta1, axis=0, keepdims=True)

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            for i in range(len(X)):
                self.forward(X[i].reshape(1, -1))
                self.backward(X[i].reshape(1, -1), y[i].reshape(1, -1), learning_rate)

# XOR function
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create neural network
nn = NeuralNetwork(2, 3, 1)

# Train the neural network
nn.train(X, y, epochs=10000, learning_rate=0.1)

# Print weights and biases after training
print("Weights 1:", nn.W1)
print("Biases 1:", nn.b1)
print("Weights 2:", nn.W2)
print("Biases 2:", nn.b2)

# Print output of neural network after training for all possible inputs
for i in range(len(X)):
    print(f"Input: {X[i]}, Output: {nn.forward(X[i].reshape(1, -1))}")
