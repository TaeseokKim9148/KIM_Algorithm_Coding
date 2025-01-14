while True:
    data = input()
    if data == "#":
        break
    
    char, sentence = data[0], data[2:]  
    lower_sentence = sentence.lower()
    lower_char = char.lower()
    count = lower_sentence.count(lower_char)
    print(f"{char} {count}")