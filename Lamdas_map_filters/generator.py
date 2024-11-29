# generators like lists and could consider generator functions just like regular
# def function():
#      counter =0
#      while counter<=10:
#          yield counter
#          counter =counter+1
#
# print(list(function()))


def evn_generator(x):
    for i in range(x):
       if i %2 ==0:
           yield i

print(list(evn_generator(10)))