import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# MNIST-Daten laden
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Werte normalisieren (0–255 → 0–1)
x_train = x_train / 255.0
x_test = x_test / 255.0

print("Trainingsdaten:", x_train.shape)
print("Testdaten:", x_test.shape)

# Beispielbild anzeigen
plt.imshow(x_train[0], cmap="gray")
plt.title(f"Label: {y_train[0]}")
plt.show()
