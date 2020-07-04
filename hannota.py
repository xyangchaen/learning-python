count=0
def han(n,x,y,z):
    global count
    if n==1:
        count+=1
    else:
        han(n-1,x,z,y)
        count+=1
        han(n-1,y,x,z)
han(2,'x','t','z')
print('需要移动%d次'% count)
