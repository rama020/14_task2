'''
DATE:07TH DEC 2022
DAY: WEDNESDAY
TOPIC: TASK
AUTHOR: rama bhargavi
'''
#elements exists list or not
n=[int(x) for x in input('enter some integers:').split()]#4 2 6 7 8
f=int(input('which element you want to find? :'))#5
for i in n:
   if(f in n): 
    print('the value',f, 'is found')
    break
else:
    print('the value',f,'is not found')#the value 5 is not found
 
    
