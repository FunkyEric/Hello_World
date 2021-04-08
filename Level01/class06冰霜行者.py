import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
name = mc.getPlayerEntityId('Eric')

while True:
    pos = mc.entity.getTilePos(name)
    if mc.getBlock(pos.x, pos.y-2, pos.z) == 8:
        mc.setBlocks(pos.x-1, pos.y-1, pos.z-1,
                     pos.x + 1, pos.y - 1, pos.z + 1, 79)
