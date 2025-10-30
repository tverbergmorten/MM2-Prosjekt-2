import numpy as np
import matplotlib.pyplot as plt

N = np.logspace(2, 6, 100)  # 10^2 til 10^6 punkter
dft_ops = N**2
fft_ops = N * np.log2(N)

plt.figure(figsize=(7,4))
plt.loglog(N, dft_ops, label="DFT ($N^2$)")
plt.loglog(N, fft_ops, label="FFT ($N \log_2 N$)")
plt.xlabel("Antall datapunkter N")
plt.ylabel("Relativ beregningsmengde")
plt.title("Sammenligning av beregningskompleksitet")
plt.grid(True, which="both", ls="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
