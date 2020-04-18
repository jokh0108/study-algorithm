from collections import defaultdict
def solution(snapshots, transactions):
    answer = [[]]
    bank = defaultdict(int)
    for snapshot in snapshots:
        account, balance = snapshot
        bank[account] = int(balance)
    IDs = set()
    for row in transactions:
        ID, transaction, account, money = row
        if ID in IDs:
            continue
        IDs.add(ID)
        if transaction == 'SAVE':
            bank[account] += int(money)
            if bank[account] >= 100000:
                bank[account] = 99999
        else:
            bank[account] -= int(money)
    return sorted([[ID, str(balance)] for ID, balance in bank.items()], key=lambda x: x[0])

print(solution([["ACCOUNT1", "100"], ["ACCOUNT2", "150"]], [["1", "SAVE", "ACCOUNT2", "100"], ["2", "WITHDRAW", "ACCOUNT1", "50"], ["1", "SAVE", "ACCOUNT2", "100"], ["4", "SAVE", "ACCOUNT3", "500"], ["3", "WITHDRAW", "ACCOUNT2", "30"]]
))
