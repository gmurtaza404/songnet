import os
import torch
import torchaudio
from songnet.audio.loader import AudioLoader
from songnet.models.transformer import SongNet

AUDIO_DIR = "data/converted/"
FREQ = 8000

def main():

    files = os.listdir(AUDIO_DIR)
    for f in files:
        f = f"{AUDIO_DIR}/{f}"
        loader = AudioLoader()
        waveform, freq = loader.load_resample(f, FREQ)
        # print(audio)
        print(waveform)
        print(waveform.shape)
        print(f"Mean: {waveform.mean()}, Max: {waveform.max()}, Min: {waveform.min()}")
        break
    net = SongNet(features=1)
    src = torch.rand((2, 10, 1)).cuda()
    tgt = torch.rand((2, 10, 1)).cuda()
    print(net(src, tgt))
    

    # loader = AudioLoader("")

if __name__ == "__main__":
    main()