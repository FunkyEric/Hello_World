from mcpi import minecraft
import mcpi.block as block
from mcpi.event import BlockEvent

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

def bomberMan(name):
    pos = mc.entity.getTilePos(name)
    x, y, z = pos
    mc.setBlock(x, y-1, z, block.TNT)

def build_fast(name):
    for blockhit in mc.events.pollBlockHits():
        # 如果是方块被敲击
        if blockhit.entityId == name and blockhit.type == BlockEvent.HIT:
            position.append(blockhit.pos)
            print(position)
            if len(position) == 2:
                print(position)
                mc.setBlocks(*position[0], *position[1], mc.getBlock(blockhit.pos))
                print(mc.getBlock(blockhit.pos))
                position.clear()


bomber_stu = False
bf_stu = False
position = []

while True:
    if bomber_stu:
        bomberMan(id)
    if bf_stu:
        build_fast(id)
    for chatpost in mc.events.pollChatPosts():
        if chatpost.entityId == id:
            if chatpost.message == 'tnt':
                mc.postToChat('Now, Eric is a bomberMan!')
                bomber_stu = not bomber_stu
            if chatpost.message == 'bf':
                bf_stu = not bf_stu
                if bf_stu:
                    mc.postToChat('Now, Eric is a fast builder!')
                else:
                    mc.postToChat('Now, stop build fast!')





