import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

while True:
    pos = mc.entity.getTilePos(id)
    x = pos.x
    y = pos.y
    z = pos.z
    if mc.getBlock(x, y-2, z) == 46:
        mc.postToChat('Now,you are on the TNT')
    else:
        mc.postToChat('Fine, go ahead!')