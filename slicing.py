item = ['karthik', 'mango','hari', 'vikas','sanjeev','pavani']
#+ve slicing
print(item[2:6])
#-ve slicing
print(item[-3:])

#in operator
print('karthik' in item)
#not in operator
print('karthi' not in item)
#append
#item.append(["karthikeya","mirai"])
#print(item)

#extened
item.extend(["karthikeya","mirai"])
print(item)
#pop
#item.pop()

print(item.index('sanjeev'))

scores =[1,34,8999,9888,1023,23,4,4,5,66,]
print(min(scores))