from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()
name = mc.getPlayerEntityId('Eric')
pos = mc.entity.getPos(name)
x, y, z = pos

id_list = mc.getPlayerEntityIds()
id_list.remove(name)
print(id_list)

a = mc.getEntityTypes()
print(a)

# sleep(5)
# mc.saveCheckpoint()
# mc.postToChat('start')
# sleep(15)
# mc.postToChat('restore')
# mc.restoreCheckpoint()
while True:
    mc.spawnEntity(x, y, z+0.5, 10, 1)

#     pass
        # if event.originName == name:
        #     print(123)