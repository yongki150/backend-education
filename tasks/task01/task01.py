import random

def _isN(s):
    try:
        return s
    except ValueError:
        return -1

ans = random.randrange(0, 1000)

while(1):
    player = input()
    player = int(_isN(player))

    if player == -1:
        print("정수를 입력하세요")
    elif player == ans:
        break
    if player < ans:
        print("UP")
    else:
        print("DOWN")
print("정답입니다.")