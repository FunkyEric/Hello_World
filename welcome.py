
import mcpi.minecraft as minecraft
# import time
mc = minecraft.Minecraft.create('192.168.1.3')
id = mc.getPlayerEntityId('Eric')

while True:
    pos = mc.entity.getTilePos(id)
    x = pos.x
    y = pos.y
    z = pos.z
    # time.sleep(0.5)

    if pos1 != pos2:
        mc.postToChat('find me, boy! This is my position: '+str(pos2.x) + ',' + str(pos2.y) + ',' + str(pos2.z))
