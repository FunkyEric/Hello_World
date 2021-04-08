import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')


























while True:

# 获得玩家位置
    pos = mc.entity.getTilePos(id)
    x, y, z = pos

    mc.setBlock(x, y+100, z, block.SNOW_BLOCK)
    mc.setBlock(x, y + 101, z, block.SNOW_BLOCK)
    mc.setBlock(x, y + 102, z, block.NUMPKIN_HEAD)






























