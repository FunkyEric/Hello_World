from mcpi import minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create('192.168.43.109')
id = mc.getPlayerEntityId('Eric')

def bomberMan():
    pos = mc.entity.getTilePos(id)
    x, y, z = pos
    mc.setBlock(x, y-1, z, block.TNT)

stu = False
while True:
    for chatpost in mc.events.pollChatPosts():
        if chatpost.entityId == id:
            if chatpost.message == 'tnt':
                mc.postToChat('Now, Eric is a bomberMan!')
                stu = not stu
                while stu:
                    bomberMan()





