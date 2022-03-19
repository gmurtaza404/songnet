import os
import subprocess
from multiprocessing import Pool

INPUT_DIR = "../downloaded"
OUTPUT_DIR = "../converted"

def convert_song(src):
    """
    Converts the given song to wav format using ffmpeg
    """

    output = src.replace(".m4a", ".wav")
    cmd = f'ffmpeg -i "{INPUT_DIR}/{src}" "{OUTPUT_DIR}/{output}"'
    p = subprocess.Popen(cmd, shell=True)
    return p.wait()


def main():
    files = os.listdir(INPUT_DIR)
    with Pool() as p:
        p.map(convert_song, files)

if __name__ == "__main__":
    main()
