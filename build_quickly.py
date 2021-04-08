# 导入我的世界python控制器模块
import mcpi.minecraft as minecraft
# 导入方块模块
import mcpi.block as block

from mcpi.event import BlockEvent
# 与我的世界游戏建立连接
mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

position = []
while True:
    # 循环所有的敲击世间
    for blockhit in mc.events.pollBlockHits():
        # 如果是方块被敲击
        if blockhit.entityId == id and blockhit.type == BlockEvent.HIT:
            position.append(blockhit.pos)
            if len(position) == 2:
                mc.setBlocks(*position[0], *position[1], blockhit.type)
                position.clear()
                continue

