import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
name = mc.getPlayerEntityId('Eric')

# 无限生成TNT
while True:
    pos = mc.entity.getTilePos(name)
    time.sleep(5)  # 每过十秒钟
    mc.setBlock(pos.x, pos.y, pos.z, 50)  # 火把

