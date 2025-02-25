n = int(input())

A_cards = []
for i in range(n):
    card = int(input())
    A_cards.append(card)

B_cards = []
for i in range(1, 2*n+1):
    if i not in A_cards:
        B_cards.append(i)


table = 0  
is_A_turn = True 

# 게임 진행
while len(A_cards) > 0 and len(B_cards) > 0:  
    if is_A_turn:
        possible_cards = []
        for card in A_cards:
            if table == 0 or card > table:
                possible_cards.append(card)
        
        if len(possible_cards) > 0:
            card_to_play = min(possible_cards)
            A_cards.remove(card_to_play)
            table = card_to_play
        else:

            table = 0  
        
        is_A_turn = False  
    
    else:
        possible_cards = []
        for card in B_cards:
            if table == 0 or card > table:
                possible_cards.append(card)
        
        if len(possible_cards) > 0:
            card_to_play = min(possible_cards)
            B_cards.remove(card_to_play)
            table = card_to_play
        else:
            table = 0  
        
        is_A_turn = True  

A_score = len(B_cards)  
B_score = len(A_cards) 

print(A_score)
print(B_score)      