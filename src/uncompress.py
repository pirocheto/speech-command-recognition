from pathlib import Path

import pandas as pd
from dvc.api import params_show
from pydub import AudioSegment
from tqdm import tqdm

words = [
    "droite",
    "gauche",
    "avance",
    "recule",
    "stop",
    "start",
]

clips = Path("data/audio/fr/clips")

df_splits = pd.read_csv("data/splits/fr_splits.csv")
df_splits = df_splits[df_splits["WORD"].isin(words)]

data = Path("data/audio")
dataset = Path("dataset")

for _, row in tqdm(df_splits.iterrows(), total=df_splits.shape[0]):
    input_path = data / "fr/clips" / row["LINK"]
    output_path = dataset / row["SET"].lower() / row["WORD"] / f"{input_path.stem}.wav"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    audio_opus = AudioSegment.from_file(input_path)
    audio_opus = audio_opus.set_sample_width(2)
    audio_opus = audio_opus.set_frame_rate(16000)
    audio_opus.export(output_path, format="wav")
