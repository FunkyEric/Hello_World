import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraftstuff as stuff

mc = minecraft.Minecraft.create()
mcDrawing = stuff.minecraftstuff.MinecraftDrawing(mc)

id = mc.getPlayerEntityId('Eric')

pos = mc.entity.getTilePos(id)
x, y, z = pos
a = 34
for i in range(5):
    mcDrawing.drawHorizontalCircle(x, y, z, a-i, block.GLASS, 0)
# mcDrawing.drawHorizontalCircle(x, y, z, 33, block.GOLD_BLOCK, 0)
# mcDrawing.drawSphere(x, y, z, 30, block.AIR, 0)
# mcDrawing.drawHollowSphere(x, y, z, 34, block.WATER, 0)
# mcDrawing.drawSphere(x, y, z, 16, block.SEA_LANTERN, 0)


