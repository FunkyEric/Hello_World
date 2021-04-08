import mcpi.minecraft as minecraft
import minecraftstuff as stuff
mc = minecraft.Minecraft.create()
pen = stuff.MinecraftTurtle(mc)
pen.position = (0, 0, 0)
pen.penblock(41)

# 无限循环漩涡
b = 3
angle = 360/4+1
while True:
    pen.forward(b)
    b = b + 1
    pen.right(angle)