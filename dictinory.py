# python in dictionary is  a collection of  keys and values
# dictionaries are mutable
people = {"karthik":23, "hari":20, "vikas":24}
people_id = {
    1:"ford",
    2:"duke",
    3:"forbs",
    4:"bmw"}
people["karthik"]=45
print(f"peoples {people}")
print(f"people id's {people_id}")

# Creating Dictionaries Using dict()
people1 = dict( kt=20, john=80, sanjev=29, )
people1["ks"] = 36
print(f"Creating Dictionaries Using dict() function  {people1}")

#get method for the use if use cant find any contet it will show none

print(f' using get method {people1.get("kt")}')
  # there is no object in the dictionary nd giving different object it will returns  none
print(f' using get method out of dictionary {people1.get("ht")}')