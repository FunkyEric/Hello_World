feet = 34
heads = 12

chicken = 1

while True:
    rabbits = heads - chicken
    if chicken*2+rabbits*4 == feet:
        print('鸡有：', chicken, '兔子有:', rabbits)
        break
    else:
        chicken += 1


