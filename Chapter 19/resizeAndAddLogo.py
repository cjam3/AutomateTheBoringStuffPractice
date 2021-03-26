#! python3
# resizeAndAddLogo.py - Resizes images in working directory to fit in a 300 x 300 square and
# adds catlogo.png to bottom right if the image width and height are at least twice the 
# width and height of catlogo.png

import os
from PIL import Image

def main():
    SQUARE_FIT_SIZE = 300
    LOGO_FILENAME = 'catlogo.png'
    resizeAndAddLogo(SQUARE_FIT_SIZE, LOGO_FILENAME)

def resizeAndAddLogo(squareDimmension, LOGO_FILENAME):
    logoIm = Image.open(LOGO_FILENAME)
    logoWidth, logoHeight = logoIm.size

    os.makedirs('withLogo', exist_ok=True)
    for filename in os.listdir('.'):
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.bmp') \
            or filename.lower().endswith('.gif')) or filename == LOGO_FILENAME:
            continue

        img = Image.open(filename)
        width, height = img.size
        if not (width > 2 * logoWidth and height > 2 * logoHeight):
            print('Skipping %s' % (filename))
            continue

        if width > height:
            height = int((squareDimmension / width) * height)
            width = squareDimmension
        else:
            width = int((squareDimmension / height) * width)
            height = squareDimmension
        
        print('Resizing %s' % (filename))
        img = img.resize(width, height)

        print('Adding logo to %s' % (filename))
        img.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        img.save(os.path.join('withLogo', filename))


if __name__ == '__main__':
    main()