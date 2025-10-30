import numpy as np
import matplotlib.pyplot as plt
N = 256
n = np.arange(N)
windows = {
    "Rectangular": np.ones(N),
    "Hann": 0.5*(1 - np.cos(2*np.pi*n/(N-1))),
    "Hamming": 0.54 - 0.46*np.cos(2*np.pi*n/(N-1)),
    "Blackman": 0.42 - 0.5*np.cos(2*np.pi*n/(N-1)) + 0.08*np.cos(4*np.pi*n/(N-1))
}
plt.figure()
for name, w in windows.items():
    plt.plot(w, label=name)
plt.legend()
plt.title("Ulike vindustyper")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.show()
