import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

def pos(id):
    position = mc.entity.getTilePos(id)
    x = position.x
    y = position.y
    z = position.z
    return x, y, z

def tellPos(x, y, z):
    mc.postToChat(str(x)+':' + str(y)+':' + str(z))

def tellBlockBlow(distance):
    mc.postToChat(mc.getBlock(x, y-distance, z))

def clearBlockAround():
    mc.setBlocks(x-1, y, z-1, x+1, y+2, z+1, block.AIR)

def creatUntilGround(blockType):
    for i in range(345):
        mc.setBlock(x, y-i, z, blockType)
        if mc.getBlock(x, y-1-i, z) == 1:
            break
def allTorch():

    mc.setBlocks(x-9, y, z-9, x+9, y, z+9, block.TORCH)

def railWay():
    # mc.setBlocks(x, y-1, z-1, x, y-1, z+1, block.GOLD_ORE)
    mc.setBlocks(x-1, y-1, z, x+1, y-1, z, block.GOLD_ORE)
    mc.setBlock(x, y, z, block.POWERED_RAIL)
    # mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block.AIR)


while True:
    x, y, z = pos(id)
    # railWay()
    # allTorch()
# creatUntilGround(block.SEA_LANTERN)
# tellPos(x, y, z)
# tellBlockBlow(1)
# mc.setBlock(x, y, z-1, block.TORCH)
#     clearBlockAround()
    mc.setBlocks(x-10, y, z-10, x+10, y+10, z+10, block.AIR)