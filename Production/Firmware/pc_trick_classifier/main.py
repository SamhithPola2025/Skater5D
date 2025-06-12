import serial
import json
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

ollie = np.load('patterns/ollie.npy')
kickflip = np.load('patterns/kickflip.npy')
tricks = {'Ollie': ollie, 'Kickflip': kickflip}

ser = serial.Serial('COM3', 115200, timeout=1) 

buffer_size = 100
data_buffer = np.zeros((buffer_size, 6))

def classify(window):
    best, best_dist = None, float('inf')
    for name, pattern in tricks.items():
        dist, _ = fastdtw(window, pattern, dist=euclidean)
        if dist < best_dist:
            best, best_dist = name, dist
    return best, best_dist

plt.ion()
fig, axs = plt.subplots(2, 1)

while True:
    try:
        line = ser.readline().decode().strip()
        if not line:
            continue

        vals = json.loads(line)
        sample = np.array([vals['ax'], vals['ay'], vals['az'], vals['gx'], vals['gy'], vals['gz']])
        data_buffer = np.roll(data_buffer, -1, axis=0)
        data_buffer[-1] = sample

        axs[0].cla(); axs[0].plot(data_buffer[:, :3]); axs[0].set_title('Accel')
        axs[1].cla(); axs[1].plot(data_buffer[:, 3:]); axs[1].set_title('Gyro')
        plt.pause(0.001)

        if np.random.randint(0, 10) == 0:
            trick, score = classify(data_buffer)
            print(f"Detected: {trick} (score={score:.2f})")

    except Exception as e:
        print("Error:", e)