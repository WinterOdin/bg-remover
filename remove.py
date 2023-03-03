
import glob, os
from pathlib import Path

import subprocess
import locale
from PIL import Image, ImageDraw, ImageFont
import subprocess
import time


main_output_folder = "output"
watermark_txt = "MKP"

path_list = []
for path in Path("input").rglob("*.png"):
    case = {path.name: path.parent}
    path_list.append(case)



for x in path_list:
    for key, value in x.items():

        output_path = os.path.join(main_output_folder, *value.parts[1:])
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_path_watermark = os.path.join(main_output_folder, "watermark", *value.parts[1:])
        if not os.path.exists(output_path_watermark):
            os.makedirs(output_path_watermark)

        input_file_location = os.path.join(value, key)
        output_file_location = os.path.join(main_output_folder, *value.parts[1:], key)

        cli_comand = f"backgroundremover -i {input_file_location} -m u2netp -o {output_file_location}"
        
        out = str(subprocess.check_output(cli_comand).decode(encoding="utf-8", errors="ignore"))

        try:

            out = str(subprocess.check_output(cli_comand).decode(encoding="utf-8", errors="ignore"))

        except subprocess.CalledProcessError as ex:
            print(f"Error with {input_file_location}")

        img = Image.open(output_file_location)
        t = ImageDraw.Draw(img, "RGBA")
        #font type and scale
        fnt = ImageFont.truetype("comicbd.ttf", 40)
        
        #position of watermark X Y
        t.text((img.size[0]/1.5, img.size[1]/2), watermark_txt, font=fnt, fill=(255, 255, 255, 120))
        img.save(os.path.join(output_path_watermark, key))
        


        








