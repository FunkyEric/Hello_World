import mcpi.minecraft as minecraft
import mcpi.block as blocks
import minecraftstuff as stuff
import time


mc = minecraft.Minecraft.create()
player_id = mc.getPlayerEntityId("Eric")
mcpen = stuff.MinecraftDrawing(mc)


def get_pos(id):
    pos = mc.entity.getTilePos(id)
    print(pos)
    return pos


def make_circleface(x, y, z, r, block):
    for i in range(r):
        mcpen.drawHorizontalCircle(x, y, z, i+1, block)
        time.sleep(0.1)


def make_wall(x, y, z, r, h, block):
    for i in range(h):
        if i < 2 or i > (h - 3):
            mcpen.drawHorizontalCircle(x, y+i, z, r, block)
        else:
            mcpen.drawHorizontalCircle(x, y + i, z, r, blocks.GLASS)
        time.sleep(0.1)


def make_door(x, y, z, r):
    mc.setBlocks(x-1, y+1, z-r-1, x+1, y+3, z-r+1, blocks.AIR)


def make_cylinder(x, y, z, r, h, block):
    make_circleface(x, y, z, r, block)
    make_wall(x, y, z, r+1, h+2, block)
    make_circleface(x, y+h+1, z, r, block)


def make_castle(data, x, y, z):
    add_y = 0
    for cylinder in data:
        make_cylinder(x, y+add_y, z, cylinder[0], cylinder[1], cylinder[2])
        make_door(x, y+add_y, z, cylinder[0])
        add_y += (cylinder[1] + 1)


data = [(75, 18, blocks.COBBLESTONE),
        (50, 14, blocks.COBBLESTONE),
        (25, 12, blocks.COBBLESTONE),
        (12, 10, blocks.COBBLESTONE)]

x, y, z = get_pos(player_id)
make_castle(data, x, y-30, z)
