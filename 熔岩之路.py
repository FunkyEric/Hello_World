import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('shadow')
time.sleep(5)
path = []
while True:
    pos = mc.entity.getTilePos(id)
    x, y, z = pos
    
    # mc.setBlock(x, y, z, block.FLOWER_YELLOW)
    path.append([x, y-1, z])
    if mc.getBlock(x, y-1, z) == block.GLASS.id:
        while len(path) > 10:
            mc.setBlock(path[0], block.LAVA)
            path.remove(path[0])
            time.sleep(0.1)