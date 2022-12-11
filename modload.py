
import modHero # 모듈 추가

querySkill = input("select weapon:") # 키입력

i = 0

for each_item in modHero.skill: # modHero.skill(모듈에 정의된 스킬을 꺼냄)
    if(each_item == querySkill): # 매치되는 것을 만나면,!
        modHero.printItem(querySkill, i) # 정보 추출후 출력.
    i = i+1 # 다음 레코드로

print("----------------------------------------")
print("\n")