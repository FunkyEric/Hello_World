# 导入我的世界python控制器模块
import mcpi.minecraft as minecraft
# 导入方块模块
import mcpi.block as block

# 与我的世界游戏建立连接
mc = minecraft.Minecraft.create()

# 获取玩家当前位置的空间坐标
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x - 1, y, z -1, block.GOLD_BLOCK.id)
mc.setBlock(x , y, z -1, block.GOLD_BLOCK.id)
mc.setBlock(x + 1, y, z -1, block.GOLD_BLOCK.id)
mc.setBlock(x - 1, y, z, block.GOLD_BLOCK.id)
mc.setBlock(x + 1, y, z, block.GOLD_BLOCK.id)
mc.setBlock(x - 1, y, z + 1, block.GOLD_BLOCK.id)
mc.setBlock(x, y, z + 1, block.GOLD_BLOCK.id)
mc.setBlock(x + 1, y, z + 1, block.GOLD_BLOCK.id)




