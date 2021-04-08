# 导入mcpi模块
import mcpi.minecraft as minecraft
# 导入方块模块
import mcpi.block as block
# 导入时间模块
import time

# 与我的世界游戏建立连接
mc = minecraft.Minecraft.create()

id = mc.getPlayerEntityId('Eric')
# 获得玩家的坐标位置
pos = mc.entity.getTilePos(id)
x = pos.x
y = pos.y
z = pos.z

# 设定金字塔的边长
width = 100

# 金字塔的高度是边长的一半，所以循环width/2次
for i in range(int(width/2)):
    # 每0.2秒建一层金字塔
    time.sleep(0.2)
    # 每一层的范围
    mc.setBlocks(x + i, y + i, z + i,
                 x + (width - i) - 1, y + i, z + (width - i) - 1,
                 block.GOLD_BLOCK.id)










