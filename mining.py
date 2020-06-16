import random
myprecious=random.randint(1,100)
print('开始挖矿！！！！')
position=input('请选择挖矿的角度～')
guess=int(position)
while guess!=myprecious:
    position=input('没挖到！再挖一次吧～')
    guess=int(position)
    if guess==myprecious:
        print('挖到宝贝啦！！！')
    else:
        if guess>myprecious:
            print('挖过头啦！！')
        else:
            print('还没挖到呢！！')
