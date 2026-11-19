# LEAD GAME
## LINK: https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/LEADGAME

## CODE:
n = int(input())

p1 = p2 = 0

max_lead = winner = 0

for _ in range(n):
    s, t = map(int, input().split())

    p1 += s
    p2 += t

    diff = p1 - p2
    lead = abs(diff)

    if lead > max_lead:
        max_lead = lead
        winner = 1 if diff > 0 else 2

print(winner, max_lead)

## EXPLANATION:
"""
First line contains number of test cases.
Taking each players (1 and 2) score in P1 and P2.
For reach round (no of test cases), note down the each player score in s and t.
Keep a record in P1 and P2.
Take the diff and if diff > 0 then player 1 is winner and lead by diff.
Else if diff < 0 then player 2 is winner and lead by diff.
Max diff will be the value of max lead

Time: (O(N)) — one pass through all rounds.
Space: (O(1)) — only a few variables; no list or array is needed
"""
