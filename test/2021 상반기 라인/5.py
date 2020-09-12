# J, Q, K == 11, 12, 13 => 10
# A => 1 or 11 ([1, 6] => [11, 6] => 17, [1, 5, 10] => 16)
# 1은 11로 치환할 때 17 이상 21미만이면 11로 사용([5, 1, 1] => [5, 11, 1]). 추후를 고려하지 않는다
# if 플레이어 WIN
#   if not 딜러 블랙잭(21이 아니면): 
#       플레이어 WIN
#       3원
# if 

import collections

def solution(cards):

    def handle_ace(player):
        new_player = player[:]
        if 1 in new_player:
            one_pos = new_player.index(1)
            if 17 <= sum(new_player) + 10 <= 21:
                new_player[one_pos] += 10
        return new_player
    
    answer = 0
    cards = collections.deque([card - card % 10 if card > 10 else card for card in cards])

    while len(cards) >= 4:
        player=[]
        dealer=[]
        player.append((cards.popleft()))
        dealer.append((cards.popleft()))
        player.append((cards.popleft()))
        dealer.append((cards.popleft()))
        reward = 0

        player = handle_ace(player)
        print('player', player, 'cards: ', cards)
        dealer = handle_ace(dealer)
        print('dealer', dealer, 'cards: ', cards)
        
        while cards:
            # player turn
            if sum(player) < 21:
                if dealer[-1] == 1 or dealer[-1] >= 7:
                    while sum(player) < 17:
                        player.append(cards.popleft())
                        print('player', player, 'cards: ', cards)
                        player = handle_ace(player)
                elif 2 <= dealer[-1] <= 3:
                    while sum(player) < 12:
                        player.append(cards.popleft())
                        print('player', player, 'cards: ', cards)
                        player = handle_ace(player)
            elif sum(player) > 21:
                reward = -2
                break
            else: 
                reward = 3
                break

            # dealer turn
            while sum(dealer) < 17:
                dealer.append(cards.popleft())
                dealer = handle_ace(dealer)
                print('dealer', dealer, 'cards: ', cards)

            if sum(dealer) > 21:
                reward = 2
                break
            elif sum(dealer) == 21:
                reward = -2
                
        if abs(sum(player) - 21) > abs(sum(dealer) - 21):
            reward = -2
        elif abs(sum(player) - 21) < abs(sum(dealer) - 21):
            reward = 2
        answer += reward

        print(answer, player, dealer, 'cards: ', cards)
    return answer

# print(solution([12, 7, 11, 6, 2, 12]) == 2)
print(solution([1, 4, 10, 6, 9, 1, 8, 13]) == 1)
# print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]) == -1)
# print(solution([12, 7, 11, 6, 2, 12]) == -1)