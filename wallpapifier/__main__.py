import click
from PIL import Image
from pathlib import Path
from math import ceil

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
    try:
        im = Image.open(path)
    except:
        print(f"Skipping {path}.")

    img_width = im.size[0]
    img_height = im.size[1]

    tiles_horiz = ceil(width / img_width)
    tiles_vert = ceil(height / img_height)

    dest = Image.new('RGB', (width, height))

    for i in range(0, tiles_horiz):
        for j in range(0, tiles_vert):
            dest.paste(im, (i*img_width, j*img_height))

    # dst_cropped = .crop(())

    dest.save(out_path)

    


@click.command()
@click.option("--input", "-i", type=dir_or_file, required=True)
@click.option("--width", "-w", type=click.INT, required=True)
@click.option("--height", "-h", type=click.INT, required=True)
def main(input, width, height):
    if isinstance(input, list):
        print("Lol this isn't supported lol")
        exit(0)
    out_fname = input.stem + "_converted.png"
    out_path = input.parent / out_fname
    convert_image(input, width, height, out_path)
    print("All done ^-^")
