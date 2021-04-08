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
    mc.setBlocks(x-100, y, z-100, x+20, y+100, z+100, block.AIR)

def creatUntilGround(blockType):
    for i in range(345):
        mc.setBlock(x, y+i, z, blockType)
        if mc.getBlock(x, y+i+1, z) != 0:
            break
def creatBridgeUntilGround(blockType):
    for i in range(345):
        mc.setBlock(x-i-1, y, z, blockType)
        if mc.getBlock(x-2-i, y, z) != 0:
            break

def allTorch():

    mc.setBlocks(x-9, y, z-9, x+9, y, z+9, block.TORCH)

def railWay():
    mc.setBlocks(x, y-1, z-1, x, y-1, z+1, block.GOLD_ORE)
    # mc.setBlocks(x-1, y-1, z, x+1, y-1, z, block.GOLD_ORE)
    mc.setBlock(x, y, z, block.POWERED_RAIL)
    # mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block.AIR)
# x, y, z = pos(id)
# creatBridgeUntilGround(block.SEA_LANTERN)
# mc.setBlocks(x-30, y, z-30, x+30, y+3, z+30, block.AIR)
while True:
    x, y, z = pos(id)
    print(x, y, z)
    # a = mc.getBlock(x, y-1, z)
    # print(a)
    # railWay()
    # allTorch()
    # creatUntilGround(block.YELLOW_STAINED_GLASS)
# tellPos(x, y, z)a
# tellBlockBlow(1)sssssssss
#     mc.setBlock(x, y-1, z, block.SAND)
#     clearBlockAround()
# l = 39
    mc.setBlocks(x-2, y-1, z-2, x+2, y-5, z+2, block.AIR)
    # mc.setBlocks(x - 2, y - 5, z - 2, x + 2, y - 50, z + 2, block.AIR)
# mc.setBlocks(x-l, y, z-l, x+l, y, z+l, block.AIR)

