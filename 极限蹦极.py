import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

while True:
    # 获得玩家位置
    pos = mc.entity.getTilePos(id)
    x, y, z = pos

    # 如果悬空，并且马上就要坠地
    if mc.getBlock(x, y-10, z) != 0 and mc.getBlock(x, y-1, z) == 0:
        # 在要坠落的位置生成水方块作为缓冲垫
        mc.setBlocks(x-1, y - 8, z-1, x+1, y - 8, z+1, block.WATER)
        time.sleep(5)
        mc.setBlocks(x-1, y-8, z-1, x+1, y-8, z+1, block.AIR)
        break

