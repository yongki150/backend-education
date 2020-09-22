import random

def _isN(s):
    try:
        return s
    except ValueError:
        return -1

ans = random.randrange(0, 1000)
print(ans)
#test print(type(ans) == type(pp))
while(1):
    player = input()
    player = int(_isN(player))
    #print("player_type", type(player), "player_val", player ,"ans_type", type(ans))
    if(player == -1):
        print("정수를 입력하세요")
    elif( player == ans ):
        break
print("정답입니다.")




