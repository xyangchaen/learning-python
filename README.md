# learning-python
Now I begin to learn python,write down something which can be forgot easily.
# variable
Compared to other programing language,python's variables don't need to define types,and you can use '' to mean strings.
e.g. t1=5                     t1='5'
     t2=3                     t2='3'
     t3=t1+t2                 t3=t1+t2 
     and t3=8                 and t3='53'            
use type() can kown the type.
# while for if elif x if x<y else y
just like any other programing language,and 'for' in python is more convenient.
e.g.  l='abcde'
      for i in l
      print i
      for i in range(5)
      print i
# assert
It's a very useful checking function that can help you debugging.
# list & tuple & string
you can put anything into a list 
e.g list1=[1,1.22,[1,2],'yang']
    list1=[]
    len(list1)
a list is a object,there is some method:
  list1.append(1) put a new element after a list
  list1.extend([1,2,3]) put more 
  list1.insert(2,'yang') put a element in a position
  list1.remove('yang') remove the element 'yang'
  del list1[1] remove
  x=list1.pop() pop the last element
  list1[1:3]>>[1.22,[1,2]]  slice of a list
  list2=list1[:] is a copy of list1
Pay attention here，list2=list don't creat a new list,they are the same one!
  list3=list2+list1
  list.count('yang')
  list.index('yang',0,3)>>3
  list.reverse()
  list.sort()
1 in list1>>true 




a tuple can't be changed.





a string can be regarded as a list
str='i am a skywalker'
str[1]>>' '
and it has many method.
#function
print('there has %d apples' % result)

num1=list(set(num)) can make only one.

#file 
f=open('D:\\.txt','r')
f.read()
f.write(str)
f.close()
