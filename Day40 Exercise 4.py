a = input("What you want code data Exercise word or decode: ")

if a == "code" or a == "Code":
    c = input("Enter your word: ")
    if len(c)==2:
        s = list(c)
        s.reverse()
        r1 = "abc"
        r2 = "def"
        m = "".join(s)
        print(r1+m+r2)
    elif len(c)>=3:
        m = list(c)
        m.append(c[0])
        m.pop(0)
        r1 = "abc"
        r2 = "def"
        j = "".join(m)
        print(r1 + j + r2)
    elif len(c) == 1 :
        r1 = "abc"
        r2 = "def"
        print(r1 + c + r2)
    elif len(c) == 0:
        print("No word to make code")

elif a == "decode":
    c = input("Enter your word: ")
    if len(c)>=9:
        s = list(c)
        n = s[3:-3]
        # print(n)
        n.insert(0,n[-1])
        # print(n)
        n.pop()
        # print(n)
        # n.insert(len(n),n[1])
        # print(n)
        # n.pop()
        # print(n)
        print("".join(n))
    elif  len(c) == 8:
        s = list(c)
        n = s[3:-3]
        n.reverse()
        print("".join(n))
    elif len(c) == 7 or len(c) == 6:
        s = list(c)
        n = s[3:-3]
        print(''.join(n))
    elif len(c) == 0:
        print("No word to decode")