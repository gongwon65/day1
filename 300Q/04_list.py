
nums = [1, 2, 3, 4, 5]
nums_avr=(sum(nums)/len(nums))
print(nums_avr)



price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[1::2])
print(nums[::-1])



interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])



interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))
print('/'.join(interest))
print('\n'.join(interest))


string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)



data = [2, 4, 3, 1, 5, 10, 9]
#data_up = data.sort()
# 리스트의 메서드를 사용할 때 새로 이름짓지 않는 것을 주의
#이름 짓고 싶을 경우는 data_up = sorted(data)
#내림차순의 경우 ,reverse = True 추가가
data.sort()
print(data)



