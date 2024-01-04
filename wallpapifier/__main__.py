import click
# import os
import glob
from PIL import Image
from pathlib import Path

def dir_or_file(p):
    p = Path(p)
    if p.is_dir():
        # return a list of all the files
        return [x for x in p.iterdir() if x.is_file()]
    elif p.is_file():
        return p
    else:
        raise ValueError()
        

def convert_image(path, width, height, out_path):
    print(f"Hello {path} {out_path} in {width} by {height}!")

@click.command()
@click.option("--input", "-i", type=dir_or_file, required=True)
@click.option("--width", "-w", type=click.INT, required=True)
@click.option("--height", "-h", type=click.INT, required=True)
def main(input, width, height):
    if isinstance(input, list):
        print("Lol this isn't supported lol")
        exit(0)
    out_fname = input.stem + "_converted" + input.suffix
    out_path = input.parent / out_fname
    convert_image(input, width, height, out_path)
