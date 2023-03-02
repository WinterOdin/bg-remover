from rembg import remove 
from PIL import Image, ImageDraw, ImageFont
import glob, os
from pathlib import Path


main_output_folder = "output"
watermark_txt = "MKP"

path_list = []
for path in Path("input").rglob("*.png"):
    case = {path.name: path.parent}
    path_list.append(case)



for x in path_list:
    for key, value in x.items():

        img = Image.open(os.path.join(value, key))
        output = remove(img)

        #saving without watermark
        output_path = os.path.join(main_output_folder, "nonwatermark", *value.parts[1:])
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        output.save(os.path.join(main_output_folder, "nonwatermark", *value.parts[1:], key))
        ##########
        
        t = ImageDraw.Draw(img, "RGBA")
        #font type and scale
        fnt = ImageFont.truetype("comicbd.ttf", 40)
        
        #position of watermark X Y
        t.text((img.size[0]/1.5, img.size[1]/2), watermark_txt, font=fnt, fill=(255, 255, 255, 120))

        output_watermark = remove(img)
        output_path = os.path.join(main_output_folder, *value.parts[1:])
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_watermark.save(os.path.join(main_output_folder, *value.parts[1:], key))

        








