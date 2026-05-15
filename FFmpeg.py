import os
import subprocess
from pathlib import Path

# SETTINGS
INPUT_DIR = "./"
OUTPUT_DIR = "./output"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    pass

def setCommand():
    command = [
        "ffmpeg","-y","-i", str(file),
        # Resize if exceeds 1920px in width
        # "-vf", "scale='min(3840,iw)':-2",
        "-vf", f"scale={customwidth}:-2",
        # Quality
        "-q:v", "4",
    ]

    return command

def setOutputFile(command: list[str], output_file: str) -> list[str]:
    command.append(str(output_file))
    return command

def RUN():
    command = setCommand()
    for file in Path(INPUT_DIR).iterdir():
        if file.suffix.lower() not in EXTENSIONS:
            continue
        
        OutputFile = Path(OUTPUT_DIR) / f"{file.stem}{file.suffix.lower()}"
        command = setOutputFile(command, OutputFile)

        print(f"Compressing: {file.name}")

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

print("Done.")

if __name__ == "__main__":
    main()