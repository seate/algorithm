options = [[list(w) for w in list(input().split())] for _ in range(int(input()))]
s = set()

for i in range(len(options)):
    opt = options[i]
    flag = False

    for j in range(len(opt)):
        word = opt[j]

        if word[0].lower() not in s:
            flag = True
            s.add(word[0].lower())
            options[i][j].insert(1, "]")
            options[i][j].insert(0, "[")
            break
    
    if not flag:
        for j in range(len(opt)):
            word = opt[j]
            flag = False
            
            for w in range(1, len(word)):
                if word[w].lower() not in s:
                    flag = True
                    s.add(word[w].lower())
                    options[i][j].insert(w + 1, "]")
                    options[i][j].insert(w, "[")
                    break
            
            if flag: break
    
    for word in opt: print("".join(word), end=" ")
    print()