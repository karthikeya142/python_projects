seta = {1,2,3,4,5,6,7}
setb = {4,5,6,7,8,9,10 }

#using union operator the duplicate values  will not be displayed.
print(f'using the union operator it displays the value {seta | setb }') 

# using Inter section  it will displays common values from both sets

print(f'common elements from the both sets {seta & setb}')

# differnce operator it takes the elemnet of set a and removes all the elements which are present in the set b

print(f' using the differnce operator a-b {setb - seta }')

#using symmetric  it takes all the elements of a and takes the all elements of b combines together and removes the elements which are common to them.

print(f'using symmetric which remove the both sets common elements {seta ^ setb}')

#using add operator in sets and we can add which is already element in the set it not raise an error. but it going to be remove as a duplicaten

seta.add(7)
seta.add(18)
print(f'using add method in set  operator {seta}  ')

#using remove method 