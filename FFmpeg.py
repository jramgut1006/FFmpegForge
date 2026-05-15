import os
import subprocess
from pathlib import Path

# SETTINGS
INPUT_DIR = "./"
OUTPUT_DIR = "./output"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    customwidth = input("Enter width (e.g.: 1920): ")
    compression = input("Enter compression level (1-31 | Lower = better quality | Default is 4): ")
    RUN(customwidth, compression)

def setParameters(file: str, customwidth: int, compression: int, OutputFile: str) -> list[str]:
    command = [
        "ffmpeg", "-y", "-i", str(file),
        # resize if exceeds 1920px in width
        # "-vf", "scale='min(3840,iw)':-2",
        "-vf", f"scale={customwidth}:-2",
        # quality / compression level
        "-q:v", str(compression),
    ]

    command.append(str(OutputFile))

    return command

def RUN(customwidth, compression):
    for file in Path(INPUT_DIR).iterdir():
        if file.suffix.lower() not in EXTENSIONS:
            continue
        
        OutputFile = Path(OUTPUT_DIR) / f"{file.stem}{file.suffix.lower()}"
        command = setParameters(file, customwidth, compression, OutputFile)

        print(f"Compressing: {file.name}")

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

print("Done.")

if __name__ == "__main__":
    main()