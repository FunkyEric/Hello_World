import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')
# 海晶灯id  169
i = 0
while i<=100:
    time.sleep(0.2)
    mc.setBlock(-84, i, -159, 169)
    i = i + 1