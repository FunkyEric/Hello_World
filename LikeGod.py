# 导入mcpi模块
import mcpi.minecraft as minecraft
# 导入方块模块
import mcpi.block as block
import time

# 与我的世界游戏建立连接
mc = minecraft.Minecraft.create()

# 获取玩家的游戏ID
id = mc.getPlayerEntityId('Eric')
# 获得玩家的坐标位置
pos = mc.entity.getTilePos(id)
x = pos.x
y = pos.y
z = pos.z

# 设定金字塔的边长
width1 = 50

# 金字塔的高度是边长的一半，所以循环width/2次
for i in range(int(width1/2)):
    time.sleep(0.5)
    # 每一层的范围
    mc.setBlocks(x + 40 + i, y + i, z + 40 + i, x + (width1 - i) - 1, y + i, z + (width1 - i) - 1, block.GOLD_BLOCK.id)

width2 = 30
# 金字塔的高度是边长的一半，所以循环width/2次
for i in range(int(width2/2)):
    time.sleep(0.5)
    # 每一层的范围
    mc.setBlocks(x - 40 + i, y + i, z - 40 + i, x + (width2 - i) - 1, y + i, z + (width2 - i) - 1, block.GOLD_BLOCK.id)

for i in range(20):
    time.sleep(0.5)
    mc.setBlocks(x - 40, y + (2*i), z + 40, x - 20, y + (2*i), z + 40, block.GLASS.id)
    time.sleep(0.5)
    mc.setBlocks(x - 40, y + (2*i + 1), z + 40, x - 20, y + (2*i + 1), z + 40, block.STONE.id)

for i in range(30):
    time.sleep(0.5)
    mc.setBlocks(x - 60, y + (2*i), z, x - 50, y + (2*i), z + 10, block.GLASS.id)
    time.sleep(0.5)
    mc.setBlocks(x - 60, y + (2*i + 1), z, x - 50, y + (2*i + 1), z + 10, block.GOLD_BLOCK.id)


while True:
	# 获取玩家当前位置的空间坐标
    pos = mc.entity.getTilePos(id)
    # 在玩家脚下创造玻璃模块
    mc.setBlock(pos.x, pos.y-1, pos.z, block.FIRE.id)