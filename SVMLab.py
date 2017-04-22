deli = ['(',')','-',',','/','.','<','>','"','[',']','{','}']
words = set()
read = False
category = ['건강과 의학','경제','과학','교육','문화와 종교','사회','산업','여가생활']
for n in [1,2,3,4]:
    fname = "D:/Lecture/4학년/데이터마이닝/한국일보(2000-40075)문서범주화실험문서집합.hkib-20000-40075/hkib-20000-40075/HKIB-20000/HKIB-20000_00{0}.txt".format(n)
    file = open(fname, "r", encoding='utf-8')
    for line in file:
        if line.__contains__("@DOCUMENT") or line.__contains__("<KW>"):
            read = False
            continue
        if line.__contains__("#TEXT"):
            read = True
            continue
        if read:
            for delimiter in deli:
                line = line.replace(delimiter, ' ')
            lineWords = line.split()
            for word in lineWords:
                words.add(word)
print("사용된단어의개수=", len(words))
#print(words)