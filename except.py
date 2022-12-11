
try:
    a = 10 / 0 # 0으로 나누기는 예외를 발생시킨다.
except:
    print("1. [exception] devided by zero")

print("\n")

try:
    a = 10 / 0
    print("value of a:", a)
except ZeroDivisionError: # 특정 예외이름으로 예외를 처리.
    print("2.[exception] devided by zero")

print("\n")

try:
    a = 10
    b = "a"
    c = a / b # 타입 오류를 발생시킴.
except (TypeError, ZeroDivisionError): #TypeError 상위 예외처리 이름.
    print("3.[exception] type error occured")
else: # 타입이 타당할 때.
    print("4.type is proper")
finally: # 무조건 실행
    print("5.end of test program")