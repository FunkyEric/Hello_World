import mcpi.minecraft as minecraft
import mcpi.block as block

import time

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

pos = mc.entity.getTilePos(id)
x, y, z = pos

l = 0
while l < 200:
    mc.setBlocks(x-1+l, y+l, z-1, x+1+l, y+l, z+1, block.GOLD_BLOCK)
    l = l + 1
    time.sleep(0.2)
