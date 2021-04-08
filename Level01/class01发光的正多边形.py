import mcpi.minecraft as minecraft
import minecraftstuff as stuff
mc = minecraft.Minecraft.create()
pen = stuff.MinecraftTurtle(mc)
pen.position = (0, 0, 0)
pen.penblock(169)

# 绘制正五边形
angle = 360/5
b = 10

pen.forward(b)
pen.right(angle)
pen.forward(b)
pen.right(angle)
pen.forward(b)
pen.right(angle)
pen.forward(b)
pen.right(angle)
pen.forward(b)
pen.right(angle)


