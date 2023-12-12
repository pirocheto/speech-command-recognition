import librosa

filename = "dataset/test/gauche/common_voice_fr_17299523.wav"
waveform, sample_rate = librosa.load(filename, sr=None)

# Convertir la fréquence d'échantillonnage en kHz
sample_rate_khz = sample_rate / 1000.0

print(f"Fréquence d'échantillonnage : {sample_rate_khz} kHz")
