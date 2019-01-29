
def solution(numbers):
    nums = [str(n) for n in numbers]
    longest = max([len(n) for n in nums], default=0)
    nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
    return str(int(''.join(nums)))
        
#solution([0,0,0,0] )
solution([3, 30, 34, 5, 9])
# solution([1000,0,0,0] )
# solution([0,0,1000,0] )
# solution([12, 121] )
# solution([21, 212] )