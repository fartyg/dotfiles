from pathlib import Path
import argparse
import sys

parser = argparse.ArgumentParser(
    prog="rsub", description="Rename sub files in directory based on video file names"
)

parser.add_argument("path", type=Path, help="Full path to directory")
args = parser.parse_args()
path = Path(args.path)

subexts = [".srt", ".srr"]
subs = [p for p in path.iterdir() if p.suffix in subexts]

videxts = [".mkv", ".mp4"]
vids = [p for p in path.iterdir() if p.suffix in videxts]

if not subs and vids:
    print("Either no subs found or no videos found in dir... Exiting.")
    sys.exit()

for sub, vid in zip(subs, vids):
    renamed_sub = path / f"{vid.stem}{sub.suffix}"
    print(f"{sub.name} --> {renamed_sub.name}")
    sub.rename(renamed_sub)
