import mcpi.minecraft as minecraft
import minecraftstuff as stuff
import time
import datetime
import math


def findPointCircle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    x = int(round(x, 0))
    y = int(round(y, 0))
    return (x, y)


mc = minecraft.Minecraft.create()
pen = stuff.MinecraftDrawing(mc)

name = mc.getPlayerEntityId('Eric')
pos = mc.entity.getTilePos(name)

clockCenter = pos
clockCenter.y = clockCenter.y + 30

clock_radius = 20
hour_hand_length = 10
min_han_length = 18
sec_hand_length = 20

pen.drawCircle(clockCenter.x,
               clockCenter.y,
               clockCenter.z, clock_radius+3, 169)

while True:
    timeNow = datetime.datetime.now()
    hours = timeNow.hour % 12
    minutes = timeNow.minute
    seconds = timeNow.second

    hour_hand_angle = (360/12)*hours
    hour_hand_x, hour_hand_y = findPointCircle(clockCenter.x,
                                               clockCenter.y,
                                               hour_hand_length, hour_hand_angle)
    pen.drawLine(*clockCenter, hour_hand_x, hour_hand_y,clockCenter.z, 1)

    min_hand_angle = (360/60)*minutes
    min_hand_x, min_hand_y = findPointCircle(clockCenter.x,
                                               clockCenter.y,
                                               min_han_length, min_hand_angle)
    pen.drawLine(clockCenter.x, clockCenter.y, clockCenter.z+1,
                 min_hand_x, min_hand_y,clockCenter.z, 7)

    sec_hand_angle = (360/60)*seconds
    sec_hand_x, sec_hand_y = findPointCircle(clockCenter.x,
                                               clockCenter.y,
                                               sec_hand_length, sec_hand_angle)
    pen.drawLine(clockCenter.x, clockCenter.y, clockCenter.z+2,
                 sec_hand_x, sec_hand_y, clockCenter.z, 80)

    time.sleep(1)
    pen.drawLine(*clockCenter, hour_hand_x, hour_hand_y,clockCenter.z, 0)
    pen.drawLine(clockCenter.x, clockCenter.y, clockCenter.z+1,
                 min_hand_x, min_hand_y,clockCenter.z, 0)
    pen.drawLine(clockCenter.x, clockCenter.y, clockCenter.z+2,
                 sec_hand_x, sec_hand_y, clockCenter.z, 0)
