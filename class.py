
class Hero:
     def __init__(self, name, age, weight):
          self.name = name
          self.age = age
          self.weight = weight
     def printHero(self):
          print("\n")
          print("------------------------------------------")
          print("1.name:", self.name)
          print("2.age:", self.age)
          print("3.weight:", self.weight)

class MyHero(Hero):
      def __init__(self, inSkill, inPower, idx):
           Hero.__init__(self, "hong gil dong", 18, 69.3)
           self.skill = inSkill
           self.power = inPower
           self.idx = idx
      def printSkill(self):
           print("4.armed weapon:", self.skill +
                    "[ power:", self.power[self.idx], "]")
skill = ["sword", "spear", "bow", "axe"]
power = [98.5, 89.2, 100, 79.2]

querySkill = input("select weapon: ")
i = 0

for each_item in skill:
     if(each_item == querySkill):
         myHero = MyHero(querySkill, power, i)
         myHero.printHero()
         myHero.printSkill()
     i = i+1

print("------------------------------------------")
print("\n")

