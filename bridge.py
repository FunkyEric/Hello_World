import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')

bridge = []

while True:
    pos = mc.entity.getTilePos(id)
    b = mc.getBlock(pos.x, pos.y - 2, pos.z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlocks(pos.x - 1, pos.y - 1, pos.z - 1, pos.x + 1, pos.y - 1, pos.z + 1, block.GLASS.id)
        coordinate = [pos.x - 1, pos.y - 1, pos.z - 1, pos.x + 1, pos.y - 1, pos.z + 1]
        bridge.append(coordinate)
    elif b != block.GLASS.id:
        if len(bridge) > 0:
            coordinate_del = bridge.pop()
            mc.setBlocks(coordinate_del[0], coordinate_del[1], coordinate_del[2], coordinate_del[3], coordinate_del[4], coordinate_del[5],
                         block.AIR)
            time.sleep(0.1)
