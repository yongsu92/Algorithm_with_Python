money = 1260
# 큰 화폐 부터 검사하기 위해서 정렬 형태로 지정
coins = [500,100,50,10]
number_of_coin = 0


# 시간 복잡도 O(화폐의 갯수)
for coin in coins:
    number_of_coin += money//coin
    money %= coin

print('number_of_coins : ',number_of_coin)