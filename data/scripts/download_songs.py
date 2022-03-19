from multiprocessing import Pool
import subprocess

import pandas as pd

HISTORY_PATH = "../youtube_data/watch-history.json"
DOWNLOAD_DIR = "../downloaded"
YOUTUBE_DL_BINARY = "yt-dlp"
KEYWORDS = ["music", "vevo", "lyric", "audio", "song"]
        
def download_youtube_file(url, format="m4a"):
    cmd = f"{YOUTUBE_DL_BINARY} --no-playlist --max-filesize 5m -P {DOWNLOAD_DIR} -f {format} {url}"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL)
    return p.wait()

def get_video_title(url):
    cmd = f"{YOUTUBE_DL_BINARY} -O title {url}"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, err = p.communicate()
    return output.decode("utf-8")

def parse_watch_history(path=HISTORY_PATH):
    history = pd.read_json(path)
    return history["titleUrl"].dropna().values

def is_song(title):
    return any([keyword in title.lower() for keyword in KEYWORDS])

def main():
    urls = parse_watch_history()
    # urls = urls[]
    # get titles
    titles = None
    with Pool() as p:
        titles = p.map(get_video_title, urls)
    
    titles = list(enumerate(titles))
    titles = list(filter(lambda x: is_song(x[1]), titles))
    urls = [urls[i] for i, _ in titles]
    with Pool() as p:
        p.map(download_youtube_file, urls)
    # print(titles[:10])
    # print(len(titles))
        
    
if __name__ == "__main__":
    main()