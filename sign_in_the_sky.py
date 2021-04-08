import cv2
import mcpi.minecraft as minecraft
import time

a = cv2.imread("sign.png")
sign = a.tolist()  # 将图片转换成数组列表格式

mc = minecraft.Minecraft.create('121.37.222.74')
name = mc.getPlayerEntityId('Eric')
pos = mc.entity.getTilePos(name)
x, y, z = pos

X = x
Z = z
for row in sign:
    for col in row:
        time.sleep(0.00000)
        if col == [219, 29, 56]:
            mc.setBlock(X, y, Z, 169)
        X += 1
    Z += 1
    X = x
