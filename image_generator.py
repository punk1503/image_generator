from PIL import Image
from random import randint

# TODO: symmetry_mode
def generate_pixels(size):
    base_color = (randint(0, 256), randint(0, 256), randint(0, 256))
    accent_color = (255 - base_color[0], 255 - base_color[1], 255 - base_color[2])
    img = Image.new('RGB', (size, size))
    for i in range(size):
        for j in range(size):
            img.putpixel((i, j), base_color if randint(0, 2) == 0 else accent_color)
    # uncomment for auto-open
    # img.show()
    return img


if __name__ == '__main__':
    img = generate_pixels(int(input()))
    img.save(f'./examples/{randint(0, 100)}.png')