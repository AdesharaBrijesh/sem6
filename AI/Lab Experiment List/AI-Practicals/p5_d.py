import numpy as np

class Neural_Network:
    def _init_(self, Input_Neuron, Hidden_Neuron, Output_Neuron):
        self.Input_Neuron = Input_Neuron
        self.Hidden_Neuron = Hidden_Neuron
        self.Output_Neuron = Output_Neuron

        self.Weights_Input_Hidden = np.random.randn(self.Input_Neuron, self.Hidden_Neuron)
        self.Bias_Hidden = np.random.randn(1, self.Hidden_Neuron)
        self.Weights_Hidden_Output = np.random.randn(self.Hidden_Neuron, self.Output_Neuron)
        self.Bias_Output = np.random.randn(1, self.Output_Neuron)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def Forward(self, X):
        self.Hidden_Input = np.dot(X, self.Weights_Input_Hidden) + self.Bias_Hidden
        self.Hidden_Output = self.sigmoid(self.Hidden_Input)
        self.Output_Input = np.dot(self.Hidden_Output, self.Weights_Hidden_Output) + self.Bias_Output
        self.Output = self.sigmoid(self.Output_Input)
        return self.Output

    def Backward(self, X, y, Output, Learning_Rate):
        Error = y - Output
        d_Output = Error
        d_Hidden_Output = np.dot(d_Output, self.Weights_Hidden_Output.T)
        d_Hidden_Input = d_Hidden_Output * self.sigmoid_derivative(self.Hidden_Output)

        self.Weights_Hidden_Output += np.dot(self.Hidden_Output.T, d_Output) * Learning_Rate
        self.Bias_Output += np.sum(d_Output, axis=0, keepdims=True) * Learning_Rate
        self.Weights_Input_Hidden += np.dot(X.T, d_Hidden_Input) * Learning_Rate
        self.Bias_Hidden += np.sum(d_Hidden_Input, axis=0, keepdims=True) * Learning_Rate

    def train(self, X, y, Epochs, Learning_Rate):
        print("thakkar dharmik : 21012531026")
        for epoch in range(Epochs):
            Output = self.Forward(X)
            self.Backward(X, y, Output, Learning_Rate)
            Loss = np.mean(np.square(y - Output))
            if epoch % 100 == 0:
                print("for mean square:")
                print(f'Epoch {epoch}, Loss: {Loss}')
        print("weights are:\n",self.Weights_Hidden_Output)
        print("bias are:\n",self.Bias_Output)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

learning = Neural_Network(Input_Neuron=2, Hidden_Neuron=3, Output_Neuron=1)
learning.train(X, y, Epochs=1000, Learning_Rate=0.1)

print("Predictions after training:")
print(learning.Forward(X))