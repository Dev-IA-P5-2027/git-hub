from PIL import Image

# i = 0
# print(i)
# while i < 10:
#     print(i)
#     i+=1

im = Image.new("RGB",(1000,1000),"grey")

im.putpixel((10, 50),(0, 0, 0))
# im.putpixel((200, 100),(0, 0, 0))
# im.putpixel((500, 200),(0, 0, 0))
# im.putpixel((600, 500),(0, 0, 0))
# im.putpixel((700, 400),(0, 0, 0))


def colo_pix(x, y, R, G, B):
    im.putpixel((x, y), (R, G, B))

def save_image():
    im.save("essai.png", "PNG")




colo_pix(200, 100, 0 ,0 ,0)
colo_pix(500, 200, 0 ,0 ,0)
colo_pix(600, 500, 0 ,0 ,0)
colo_pix(700, 400, 0 ,0 ,0)

for x in range(0,1000):
    colo_pix(x, 250, 0, 0, 0)

for y in range(0, 1000):
    colo_pix(250, y, 0, 0, 0)


y = 0
while y < 1000:
    for x in range(0, 1000):
        colo_pix(x, y, 0, 0, 255)
    y+=60

x = 0
while x < 1000:
    for y in range(0, 1000):
        colo_pix(x, y, 0, 255, 0)
    x+=60

for x in range(500, 700):
    for y in range(100, 300):
        colo_pix(x, y, 255, 255, 0)
# x = 10
# y = 10
# while x < 1000:
#     while y < 1000:

def carré_violet():
    for x in range(10, 40):
        for y in range(10, 40):
            colo_pix(x, y, 255, 0, 255)

def carré_violet2():
    for x in range(40, 70):
        for y in range(40, 70):
            colo_pix(x, y, 255, 0, 255)

carré_violet()
carré_violet2()

# a = 0
# while a < 1000:
#     for x in range(40+a, 70+a):
#         for y in range(40+a, 70+a):
#             colo_pix(x, y, 255, 0, 255)
# a+=30

# x = 0
# y = 0

# while x < 900:
#     y = 0
#     while y < 900:
#         for px in range(x, x + 30):
#             for py in range(y, y + 30):
#                 colo_pix(px, py, 255, 0, 255)
#         y += 30
#     x += 30


im.show()
save_image()
im = Image.open("essai.png")