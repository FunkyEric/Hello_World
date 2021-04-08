import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

name = mc.getPlayerEntityId('Eric')


while True:
    # 循环所有的mc敲击事件
    for event in mc.events.pollBlockHits():
        if event.entityId == name:
            # 获取敲击点位置
            pos = event.pos
            x, y, z = pos
            while True:
                # 设置玩家位置
                if mc.getBlock(x, y+1, z) == 0:
                    mc.entity.setPos(name, x, y+1, z)
                    for i in range(10):  # 0-9
                        time.sleep(1)
                        if i > 6:
                            mc.postToChat(10-i)
                    break
                else:
                    y = y + 1
