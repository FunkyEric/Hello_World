import mcpi.minecraft as minecraft
import random
import time
mc = minecraft.Minecraft.create()
Eric = mc.getPlayerEntityId('Eric')

# mc.entity.setTilePos(Eric, 0, 0, 0)


# 创造场地
mc.setBlocks(-5, -1, -5, 5, 4, 5, 1)
mc.setBlocks(-4, 0, -4, 4, 4, 4, 0)

while True:
    # 清空场地
    mc.setBlocks(-4, 0, -4, 4, 3, 4, 0)
    time.sleep(5)
    # 铁砧雨
    for i in range(100):
        x = random.randint(-4, 4)
        y = 30
        z = random.randint(-4, 4)
        mc.setBlock(x, y, z, 145)




