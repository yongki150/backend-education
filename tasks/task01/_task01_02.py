#리스트에 들어있는 값을 활용해서 target값을 찾아내야함
#문제에서, list의 len이 10^5이므로, N^2 알고리즘으로 만들면, TO남.

#음,.. 값을 정렬해서 양 뒤 쪽으로 부터 비교하여, 가장 최선의 해를 찾으면 될 듯.

def _Fuc(_list, tg):
    i,j = 0, len(_list) - 1
    while(i < j):
        _sum = _list[i] + _list[j]
        print(i, " ", j, "  ", _sum)
        if(_sum == tg):
            ans = [i, j]
            return ans
        elif(_sum > tg): #더한 값이 더 클 경우
            j -= 1
        else:
            i += 1
    return False #불가능함 
        



#_list = []
_list = [3,10,20,40,4,7,9]
_list.sort()
print(_list)
_tar = int(input())
print(_Fuc(_list, _tar))
