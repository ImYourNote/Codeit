from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    i = 1
    picked_numbers = []
    
    while(i <= 6):
        number = randint(1,45)
        if(number not in picked_numbers):
            picked_numbers.append(number)
        i += 1
        
    return picked_numbers

# 테스트 코드
print(generate_numbers(6))