import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
name = mc.getPlayerEntityId('Eric')

# 无限生成TNT
while True:
    pos = mc.entity.getTilePos(name)
    time.sleep(1)  # 每过1秒钟
    mc.setBlock(pos.x, pos.y+1, pos.z, 0)  # 空气

