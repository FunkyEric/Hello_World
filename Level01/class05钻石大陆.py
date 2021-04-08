import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
name = mc.getPlayerEntityId('Eric')


pos = mc.entity.getTilePos(name)

mc.setBlocks(pos.x-30, pos.y-1, pos.z-30,
             pos.x + 30, pos.y - 1, pos.z + 30, 56)
