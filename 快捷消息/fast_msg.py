import mcpi.minecraft as minecraft
import mcpi.event

mc = minecraft.Minecraft.create()
id = mc.getPlayerEntityId('Eric')
file = open('msgs.txt', 'r')
msg_list = []

line = True
while line:
    line = file.readline()
    msg_list.append(line)
file.close()

while True:
    for chatpost in mc.events.pollChatPosts():
        if chatpost.entityId == id and 0 <= int(chatpost.message) < len(msg_list)-1:
            mc.postToChat(msg_list[int(chatpost.message)])



