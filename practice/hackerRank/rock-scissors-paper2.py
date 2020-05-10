# Enter your code here. Read input from STDIN. Print output to STDOUT

def do_tournament(participants):
    formations = []
    while participants != "X":
        next_participants = ""
        for i in range(0, len(participants), 2):
            fight = participants[i:i+2]
            next_participants += winner_of[fight]
            if "X" != fight and "X" in fight:
                formations.append(X_formation[fight])
        participants = next_participants
    return formations

def get_num_of_changes(formations):
    count = 0
    for i in range(len(formations)-1):
        if formations[i+1] != formations[i]:
            count += 1
    return count

winner_of = {
    "PR": "P", "RP": "P", "SP": "S", "PS": "S", "RS": "R", "SR": "R",
    "PP": "", "RR": "", "SS": "",
    "XS": "X", "SX": "X", "XP": "X", "PX": "X", "XR": "X", "RX": "X",
    "X": "X", "P": "P", "S": "S", "R": "R"
}
X_formation = {
    "XS": "R", "SX": "R", "XP": "S", "PX": "S", "XR": "P", "RX": "P",
}
n = int(input())
a = int(input())
participants = input()
participants = participants[:a] + "X" + participants[a:]
X_formations = do_tournament(participants)
change_num = get_num_of_changes(X_formations)
print(change_num)
