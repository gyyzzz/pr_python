from PIL import Image
from PIL import ImageDraw , ImageFont
from random import randint 
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')

    # 生成随机点坐标
def randomPoint():
    return randint(0, img.width), randint(0, img.height)

def randomColor(start=0, end=255):
    return randint(start, end), randint(start, end),randint(start, end)

for i in range(img.width * img.height // 8):
    draw.point(randomPoint(),randomColor(150))

myfont = ImageFont.truetype('Chalkduster.ttf', size=20)

for i in range(4):
    res = []
    txt = chr(randint(65,90))
    res.append(txt)
    draw.text((i * 30 + 10, 5), txt, fill=randomColor(0, 150), font=myfont)
res = ''.join(res)

for i in range(4):
    draw.line((randomPoint()) + img.size, fill=randomColor(0, 150))

img.show()

with open('verification_code.png', 'wb') as f:
    img.save(f, 'png')
