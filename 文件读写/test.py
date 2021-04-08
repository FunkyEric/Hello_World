pen.color('white')              # 颜色
pen.down()                      # 放下画笔
for i in range(random(5, 25)):  # 循环5至25次
    y = y - 10                  # 向下移动10
pen.up()                        # 抬起画笔
while True:                     # 重复执行
    if touch('bat'):            # 如果碰到蝙蝠
        say('啊啊啊！')          # 说
        score = score + 1       # 分数加1
        del self                # 删除自己



