import mcpi.minecraft as minecraft
import mcpi.block as block
# 导入time库
import time

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

while True:
    # 将位置转移到空中
    mc.entity.setTilePos(id, 0, 500, 0)

    # 如果脚下是空气，生成一个平台
    if mc.getBlock(0, 499, 0) == 0:
        mc.setBlock(0, 499, 0, block.GLASS)

    # 休眠30秒
    time.sleep(30)







