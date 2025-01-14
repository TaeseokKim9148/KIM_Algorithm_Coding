n = int(input())


gomgom = 0


for _ in range(n):
    
    chat = input()
    
    
    if chat == "ENTER":
        chatted_users = set()  
    
    
    else:
        if chat not in chatted_users:
            gomgom = gomgom + 1
            chatted_users.add(chat)


print(gomgom)