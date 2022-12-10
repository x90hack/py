#story of "hong gil dong"

name = "Hong Gil Dong"
age = 18
weight = 69.3

skill = ["sword", "spear", "Bow", "axe"]
power = [98.5, 89.2, 100, 79.2]

querySkill = input("select weapon: ")

print("\n")
print("-------------------------------------------------------")
print("1.name: ",name)
print("2.age:",age)
print("3.weight:", weight)

i = 0

print(str(123))

for each_item in skill: 

  if(each_item == querySkill):

    print("4.armed weapon:",each_item,"[ power",power[1],"]")
    print(">>>i am ready to fight")
  i = i+1

print("-------------------------------------------------------")
print("\n")
