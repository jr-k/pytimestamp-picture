from PIL import Image, ImageDraw, ImageFont
import time
import os
import sys
fileName = sys.argv[1] if len(sys.argv) > 1 else 'frame1.jpg'
fileInfo = os.stat(fileName)
timeInfo = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(fileInfo.st_mtime))
im = Image.open(fileName)
myfont = ImageFont.truetype('FreeSans.ttf', 15)
topLeftWidth = int(im.size[0] - (im.size[0] / 8))
topLeftHeight = int(im.size[1] - (im.size[1] / 30))
draw = ImageDraw.Draw(im)
draw.rectangle([topLeftWidth, topLeftHeight, im.size[0], im.size[1]], fill="white")
draw.text([topLeftWidth + 12, topLeftHeight + 3], timeInfo, fill="black", font=myfont)
del draw
fileNameOut = fileName.replace('.', '_timestamped.')
print(fileNameOut + ": " + timeInfo)
im.save(fileNameOut, 'JPEG')
