def equalFrequency(word):
        list = []
        list_freq = []
        list_freq2 = []
        count = 0
        x=0
        for i in range (len(word)):
            if word[i] not in list:
                list.append(word[i])
                list_freq.append(word.count(word[i]))
        for i in list_freq:
            list_freq2=list_freq
            list_freq2.pop(list_freq.index(i))
            if i in list_freq2:
                x = i
            else:
                y = i
                count += 1
        print(list)
        print(list_freq)
        print(count)
        flag=True
        if count == 1:
            if x-y == 1 or y-x == 1:
                return True
            else:
                return False
        else:
            for i in list_freq:
                if i != 1:
                    flag = False
            if flag == True:
                return True
            else:
                return False

a=input()
b=equalFrequency(a)
print(b)