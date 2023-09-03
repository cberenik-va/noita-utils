import os
import subprocess
from pathlib import Path

home = str(Path.home())
noita_dir = (
    f"{home}\\AppData\\LocalLow\\Nolla_Games_Noita\\save_rec\\screenshots_animated"
)

# listdir returns items in alphabetical order. Noita outputs files with timestamped names, so the newest file will
# always be the last one
files = os.listdir(noita_dir)
last_file = files[-1]

subprocess.run(
    [
        "ffmpeg",
        "-i",
        f"{noita_dir}\\{last_file}",
        "-pix_fmt",
        "yuv420p",
        f"{home}\\Desktop\\{last_file}.mp4",
    ],
    check=True,
)
