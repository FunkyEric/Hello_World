import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

while True:
    pos = mc.entity.getTilePos(id)
    x = pos.x
    y = pos.y
    z = pos.z
    if x == 10 and y == 0 and z == 0:
        mc.postToChat('welcome to the room for baby')
    if x == 0 and y == 0 and z == 0:
        mc.postToChat('this is 0,0,0')
    if x >-11 and x<11 and z > -11 and z < 11:
        mc.postToChat('you are in')
    else:
        mc.postToChat('you are out')




