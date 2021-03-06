#-*-coding:UTF-8-*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def randChar():
    return chr(random.randint(48,57))

def randColor1():
    return (random.randint(64,255), random.randint(64,266), random.randint(64,255))

def randColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32, 127))

width = 60*4
height = 60

image = Image.new('RGB', (width, height), (255,255,255))

font = ImageFont.truetype('Arial.ttf', 40)

draw  = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y), fill = randColor1())

for t in range(4):
    draw.text((60*t+10,10), randChar(), font = font, fill = randColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')


