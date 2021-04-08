from mcpi import minecraft
from random import randint
from random import choice

mc = minecraft.Minecraft.create()


class TpStone:
    def __init__(self):
        self.type = (3, 5, 6, 10)
        self.pos = (randint(-10, 10), randint(0, 10), randint(-10, 10))

    def blink(self):
        x = self.pos[0]
        y = self.pos[1]
        z = self.pos[2]
        mc.setBlock(x, y, z, choice(self.type))

    def teleport(self, names):
        for name in names:
            name_id = mc.getPlayerEntityId(name)
            x = self.pos[0]
            y = self.pos[1]
            z = self.pos[2]
            if mc.entity.getTilePos(name_id) == (x, y+1, z):
                r_x = randint(-1000, 1000)
                r_z = randint(-1000, 1000)
                mc.entity.setTilePos(name_id, r_x, y, r_z)

s1 = TpStone()
names = ('Eric', 'Ant')
while True:
    s1.blink()
    s1.teleport(names)