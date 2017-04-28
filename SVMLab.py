import time
from collections import OrderedDict
start_time = time.time()
deli = ['(' , ')' , '-' , ',' , '/' , '.' , '<' , '>' , '"' ,"'", '[' , ']' , '{' , '}']
articles = list()
article = ""
test_article= list()
read = False
categories = {'건강과 의학':0,'경제':1,'과학':2,'교육':3,'문화와 종교':4,'사회':5,'산업':6,'여가생활':7}
count = [0]*8
all = 0
test_all = 0
feature = dict()
file_num = 0;
def insertArticle(cate,arti):
    for delimiter in deli:
        arti = arti.replace(delimiter,' ')
    articleWords = arti.split()
    words = set(articleWords) #기사내에 중복제거
    if n !=5:
        articles.append([category,words])
        for word in words:
            if word in feature: # 이미 존재하는 피쳐이면 카이스퀘어테이블 값수 정
                feature.get(word)[category] += 1
            else: # 존재하지 않으면 피쳐와 카이스퀘어테이블 추가
                table = [0] * 8
                table[category] += 1
                feature.update({word : table})
    else:
        test_article.append([category,words])
def writeOutput(file, article):
    output = open(file, "w", encoding='utf-8')
    for art in article:
        output.write(str(art[0] + 1) + " ")
        words = dict()
        for word in art[1]:
            if word in sorted_feature:
                words.update({feature_index[word]: sorted_feature[word]})
        for k, v in sorted(words.items()):
            output.write(str(k) + ":" + str(v) + " ")
        output.write("\n")
    output.close()
for n in [1,2,3,4,5]:
    file_num = n
    fname = "D:/Lecture/4학년/데이터마이닝/한국일보(2000-40075)문서범주화실험문서집합.hkib-20000-40075/hkib-20000-40075/HKIB-20000/HKIB-20000_00{0}.txt".format(n)
    file = open(fname, "r", encoding='utf-8')
    while True:
        line = file.readline()
        if line =="":
            if len(article) > 1:
                insertArticle(category,article)
                article = ""
            break;
        if line.__contains__("@DOCUMENT") or line.__contains__("<KW>"):
            if len(article) > 1:
                insertArticle(category, article)
            article =""
            read = False
            continue
        if line.__contains__("#CAT'03"):
            for cate in categories:
                if cate in line:
                    category = categories[cate]
            if file_num != 5:
                count[category] += 1
                all+=1
            else:
                test_all +=1
        if line.__contains__("#TEXT"):
             read = True
             continue
        if read:
            article += line
    file.close()
feature2 = dict()
for k,v in feature.items():
    max = 0
    for cate in range(8):
        a = v[cate]
        b = count[cate] - a
        c = 0
        d = 0
        for n in range(8):
            c += v[n]
        c -= a
        d = all - a -b -c
        temp = all*(a*d-c*b)*(a*d-c*b) / ((a+c)*(b+d)*(a+b)*(c+d))
        if(temp > max):
            max = temp;
    feature2.update({k : max})
sorted_feature = OrderedDict(sorted(feature2.items(), key = lambda  x:x[1], reverse=True))
feature_index = dict()
count = 0
for fea in sorted_feature.keys():
    feature_index[fea] = count
    count += 1
writeOutput("train.txt",articles)
writeOutput("test.txt",test_article)
print("--- %s seconds ---" % (time.time() - start_time))
