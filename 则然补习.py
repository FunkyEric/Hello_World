import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# 连接服务器和人物
mc = minecraft.Minecraft.create('192.168.1.101')
myname = mc.getPlayerEntityId('Eric')

pos = mc.entity.getTilePos(myname)
x, y, z = pos

while True:
    if -47<=x<=-46 and -38<=z<=-37:
        mc.entity.setTilePos(myname, (-39,-6,-45))
