from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess
import glob, os
import locale
import time


MAIN_OUTPUT = "output"
WATERMARK_TXT = "MKP"

def create_dir(path: str) -> None:

    if not os.path.exists(path):
        os.makedirs(path)
    

def save_with_watermark(file_location: str, watermark_path: str, key:str ) -> None:
    
        img = Image.open(file_location)
        t = ImageDraw.Draw(img, "RGBA")

        #font type and scale
        fnt = ImageFont.truetype("comicbd.ttf", 40)

        #position of watermark X Y
        t.text((img.size[0]/1.5, img.size[1]/2), WATERMARK_TXT, font=fnt, fill=(255, 255, 255, 120))
        img.save(os.path.join(watermark_path, key))


def remove() -> None:
    path_list = []
    for path in Path("input").rglob("*.png"):
        case = {path.name: path.parent}
        path_list.append(case)


    for x in path_list:
        for key, value in x.items():

            output_path = os.path.join(MAIN_OUTPUT, *value.parts[1:])
            output_path_watermark = os.path.join(MAIN_OUTPUT, "watermark", *value.parts[1:])

            create_dir(output_path)
            create_dir(output_path_watermark)

            input_file_location = os.path.join(value, key)
            output_file_location = os.path.join(MAIN_OUTPUT, *value.parts[1:], key)

            try:

                cli_comand = f"backgroundremover -i {input_file_location} -m u2net -ab 20 -ae 20 -o {output_file_location}"
                subprocess.call(cli_comand)

            except subprocess.CalledProcessError as ex:
                out = str(ex.stdout.decode(encoding="utf-8")).rstrip()
                print(f'Value error{out}')

            
            save_with_watermark(output_file_location, output_path_watermark, key)
        

if __name__ == "__main__":
    remove()