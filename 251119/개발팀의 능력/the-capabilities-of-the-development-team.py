arr = list(map(int, input().split()))

def diff(i, j, k, l):
	# 세 번째 팀원의 합은 전체에서 첫 번째 팀원과 두 번째 팀원의 합을 빼주면 됩니다.
	sum1 = arr[i] + arr[j]
	sum2 = arr[k] + arr[l]
	sum3 = sum(arr) - sum1 - sum2
	
	# 세 팀의 차이 중 최댓값을 리턴합니다.
	ret = abs(sum1 - sum2)
	ret = max(ret, abs(sum2 - sum3))
	ret = max(ret, abs(sum3 - sum1))
	
	return ret


min_diff = 99999999999999

# 첫 번째 팀원을 만들어줍니다.
for i in range(5):
	for j in range(i + 1, 5):
		
		# 두 번째 팀원을 만들어줍니다.
		for k in range(5):
			for l in range(k + 1, 5):
				
				# 첫 번째 팀원과 두 번째 팀원이 겹치는지 여부를 확인합니다.
				if k == i or k == j or l == i or l == j:
					continue
				
				sum1 = arr[i] + arr[j]
				sum2 = arr[k] + arr[l]
				sum3 = sum(arr) - sum1 - sum2
				
				if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
					continue
				
				min_diff = min(min_diff, diff(i, j, k, l))
if min_diff == 99999999999999:
    min_diff=-1
print(min_diff)
