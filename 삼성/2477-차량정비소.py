from collections import deque
T =int(input())

def solution(N, M, K, A, B, a, b, c):
    a_history = {} # { 고객번호: 접수 창구 번호}
    b_history = {} # { 고객번호: 정비 창구 번호}

    def window_update():
        # 현재 기준, 창구에서 끝난 고객들 정리
        for i in range(M):
            if b_window[i][0] > 0 and b_window[i][1] == b[i]:
                b_history.update({b_window[i][0]: i+1})
                b_window[i] = [0, 0]
        arr = []
        for i in range(N):
            if a_window[i][0] > 0 and a_window[i][1] == a[i]:
                a_history.update({a_window[i][0]: i+1})
                arr.append([a_window[i][0], i]) # [고객번호, 이용 했던 접수 창구 번호] 
                a_window[i] = [0, 0]
        # print(123, arr)
        b_wait.extend(sorted(arr, key= lambda x: x[1]))
    
    def waitlist_update():
        # 대기중인 고객들 정리
        empty_window = deque([i for i, pair in enumerate(b_window) if pair[0] == 0 ])
        # print("empty_window and b_wait", empty_window, b_wait)
        while empty_window and b_wait:
            window_idx = empty_window.popleft()
            c_num , _ = b_wait.popleft() 
            b_window[window_idx] = [c_num, 0]
        
        empty_window = deque([i for i, pair in enumerate(a_window) if sum(pair) == 0 ])
        while c and c[0][1] == 0:
            a_wait.append(c.popleft())
        # print("empty_window and a_wait", empty_window, a_wait)
        while empty_window and a_wait:
            window_idx = empty_window.popleft()
            c_num , _ = a_wait.popleft() 
            a_window[window_idx] = [c_num, 0]
        

    def time_update():
        # 창구에 있는 사람들 시간 증가, 도착한 고객 시간 감소
        for i in range(M):
            if b_window[i][0] > 0:
                b_window[i][1] += 1
        for i in range(N):
            if a_window[i][0] > 0:
                a_window[i][1] += 1
        for i in range(len(c)):
            c[i][1] -= 1

    # def debug(msg):
        # print(f'======================={msg}=============================')
        # print("a_wait, a, a_window", a_wait, a, a_window, sep='\n')
        # print("b_wait, b, b_window", b_wait, b, b_window, sep='\n')
        # print("c", c)
        
    a_window = [[0, 0]] * len(a)
    b_window = [[0, 0]] * len(b)
    a_wait = deque()
    b_wait = deque()
    t=0
    while len(b_history) < K:

        # print(f'-------------------{t}sec-----------------')
        t+=1
        window_update()
        # debug("window_update")
        waitlist_update()
        # debug("waitlist_update")
        time_update()
        # debug("time_update")
        # print(a_history, b_history)
    s1 = set([k for k, v in a_history.items() if v == A])
    s2 = set([k for k, v in b_history.items() if v == B])
    # print(s1, s2)
    return sum(s1 & s2)
    

for i in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = deque([[i+1, n] for i, n in enumerate(map(int, input().split()))])
    ans = solution(N, M, K, A, B, a, b, c)
    print(f"#{i}", ans if ans !=0 else -1)