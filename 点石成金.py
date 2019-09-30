# 导入我的世界python控制器模块
import mcpi.minecraft as minecraft
# 导入方块模块
import mcpi.block as block

from mcpi.event import BlockEvent

# 与我的世界游戏建立连接
mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')


while True:
    # 循环所有的敲击世间
    for blockhit in mc.events.pollBlockHits():
        # 如果是方块被敲击
        if blockhit.type == BlockEvent.HIT:
            mc.setBlock(blockhit.pos, block.SEA_LANTERN)





















    #mc.setBlocks(pos.x-5, pos.y-2, pos.z-5, pos.x+5, pos.y-1, pos.z+5, block.GRASS.id)