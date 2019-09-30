import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

mc.setBlocks(-155, 48, -63, -179, 48, -58, block.AIR)

mc.setBlocks(-185, 48, -59, -205, 48, -56, block.AIR)

mc.setBlocks(-243, 50, -52, -339, 50, -84, block.AIR)