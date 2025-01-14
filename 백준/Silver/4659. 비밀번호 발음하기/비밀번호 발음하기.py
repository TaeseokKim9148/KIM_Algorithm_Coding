while True:
    pw = input()
    if pw == 'end':
        break
    
    ok = False
    for i in pw:
        if i in 'aeiou':
            ok = True
            break
    
    if not ok:
        print(f'<{pw}> is not acceptable.')
        continue
    

    ok = True
    for i in range(len(pw)-2):
        three = pw[i:i+3]  
       
        vowel_cnt = 0
        for x in three:
            if x in 'aeiou':
                vowel_cnt += 1
        
        consonant_cnt = 0
        for x in three:
            if x not in 'aeiou':
                consonant_cnt += 1
        
        if vowel_cnt == 3 or consonant_cnt == 3:
            ok = False
            break
    
    if not ok:
        print(f'<{pw}> is not acceptable.')
        continue
    

    ok = True
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:  
            if pw[i] != 'e' and pw[i] != 'o':
                ok = False
                break
    
    if ok:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')