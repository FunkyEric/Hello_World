import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
name = mc.getPlayerEntityId('Eric')

# 无限生成TNT
while True:
    pos = mc.entity.getTilePos(name)

    mc.setBlock(pos.x, pos.y-1, pos.z, 46)  # 炸弹
    mc.setBlock(pos.x, pos.y-2, pos.z, 51)  # 火焰
