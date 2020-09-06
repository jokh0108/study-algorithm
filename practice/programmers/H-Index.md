# [H-Index](https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3)

## 문제 설명

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과[1](https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3#fn1)에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이고 나머지 논문이 h번 이하 인용되었다면 `h`가 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

## 제한사항

- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

## 입출력 예

| citations       | return |
| --------------- | ------ |
| [3, 0, 6, 1, 5] | 3      |

## 입출력 예 설명

이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

## 문제 풀이 과정

1. 문제는 간단하지만 생각보다 어려웠던 문제임. 주어진 조건대로 풀면 되는데 각 변수들이 무엇을 의미하는지 빠르게 파악하는게 필요함. 만약 틀렸다면 다음과 같은 케이스들을 체크하는게 필요함
   - `[0]*1`, `[0]*1000`, `[10000]*1`, `[10000]*1000` 등의 극단적인 케이스
   - `[1,1,1,2,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7]`과 같이 element 값이 중복되는 케이스

```python
def solution(citations):
    citations = sorted(citations)
    H_Index = 0
    i=0
    length = len(citations)
    for h in range(citations[-1]+1):
        if length - i >= h:
            H_Index = h
        if h == citations[i]:
            while i < length and h == citations[i] :
                i+=1
         
    print(H_Index)
    return H_Index
    ## 중복 생각하기!!!!
```

## 팁

- 
