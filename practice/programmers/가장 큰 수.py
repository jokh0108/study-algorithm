def solution(numbers):
	answer = [str(numbers[0])]
	bigger = ["0"]
	for i in range(1, len(numbers)):
		each = str(numbers[i])
		for j in range( len(answer)+1):
			print("answer[0:j]", answer[0:j])
			print("[each]", [each])
			print("answer[j:]", answer[j:])
			new_lst = answer[0:j] + [each] + answer[j:]
			print("new_lst",new_lst)
			if int("".join(bigger)) < int("".join(new_lst)):
				bigger = new_lst[:]
			else:
				if int("".join(new_lst)) == 0:
					bigger = new_lst[:]
			print("bigger",bigger,"\n")
		answer = bigger
	answer = str(int("".join(answer)))
	print(answer)
	return answer


#solution([0,0,0,0] )
solution([3, 30, 34, 5, 9])
# solution([1000,0,0,0] )
# solution([0,0,1000,0] )
# solution([12, 121] )
# solution([21, 212] )