import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraftstuff as stuff

mc = minecraft.Minecraft.create()
mcDrawing = stuff.minecraftstuff.MinecraftDrawing(mc)

id = mc.getPlayerEntityId('Eric')

pos = mc.entity.getTilePos(id)
x, y, z = pos

# mcDrawing.drawHorizontalCircle(x, y, z, 27, block.DIAMOND_BLOCK, 0)
# mcDrawing.drawHorizontalCircle(x, y, z, 33, block.GOLD_BLOCK, 0)
# mcDrawing.drawHollowSphere(x, y, z, 25, block.LAVA, 0)
# mcDrawing.drawHollowSphere(x, y, z, 100, block.GLASS, 0)
mcDrawing.drawSphere(x, y, z, 8, block.DIAMOND_BLOCK, 0)


