num = 22

if num % 3 == 0:
    if num % 7 == 0:
        print(f"{num}은 3의 배수, 7의 배수")
    else:
        print(f"{num}은 3의 배수")
elif num % 7 == 0:
    print(f"{num}은 7의 배수")
else:
    print(f"{num}은 3의 배수도 아니고 7의 배수도 아님")
