import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load audio file
y, sr = librosa.load(r"C:\Users\LAB\Documents\MM2\Seven Nation Army.wav")

# Compute spectrogram
spec = librosa.feature.melspectrogram(y=y, sr=sr)

# Convert power to decibels
spec_db = librosa.power_to_db(spec, ref=np.max)

# Plot spectrogram
fig, ax = plt.subplots(nrows = 1, ncols = 1)
img = librosa.display.specshow(spec_db, x_axis='time', y_axis='mel', ax = ax)
fig.colorbar(img, ax = ax, format='%+2.0f dB')
ax.set_title('Spectrogram')
fig.show()
input("Trykk enter for å fortsette ... ")
