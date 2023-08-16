import os
import sys

# >>>pip3 install Pillow
from PIL import Image, ImageOps, ImageDraw, ImageFont


def make_images_3x3_grid(imgs, id_imgs, border=0):
    cols = 3
    rows = len(imgs) // 3
    w, h = 900, 300 * rows
    grid = Image.new('RGB',
        size=(w + border * 2 ,  h + border * (rows - 1)),
        color=(200,200,200))
    
    if sys.platform == 'linux':
        font_name = 'arial.ttf'
    else:
        font_name = 'Helvetica'

    for i, img in enumerate(imgs):
        img_tmp = ImageOps.fit(img, size=(300, 300))
        draw_img = ImageDraw.Draw(img_tmp)
        draw_img.rectangle([0, 0, 60, 35], fill=(200,200,200))
        draw_img.text(
                    (10, 5),  # Coordinates
                    str(id_imgs[i]),  # Text
                    (0, 0, 0),  # Color
                    font=ImageFont.truetype(font=font_name, size=30))

        grid.paste(img_tmp,
            box=(i%cols*300 + (i%cols*border), i//cols*300 + (i//cols*border)))

    return grid


def make_catalog(imgs, id_imgs):
    assert len(imgs) == len(id_imgs)

    catalog = []
    
    imgs_divide = divide(imgs, 9)
    id_imgs_divide = divide(id_imgs, 9)

    for index, imgs_element in enumerate(imgs_divide):
        catalog.append(
            {'img' : make_images_3x3_grid(imgs_element,
                                          id_imgs_divide[index],
                                          border=20),
            'id_imgs': id_imgs_divide[index]})

    return catalog


def divide(lst: list, n: int):
    divide_list = []
    for i in range(0, len(lst), n):
        divide_list.append(lst[i:i+n])

    return divide_list


if __name__ == '__main__':
    images = []
    images_name = os.listdir('./images/')
    for image_name in images_name:
        images.append(Image.open(f'./images/{image_name}'))

    id_list = [*range(75, 96)]
    catalog = make_catalog(images, id_list)
    catalog[0]['img'].show()
