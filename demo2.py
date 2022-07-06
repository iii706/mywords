f1 = open('topwords3.txt','r',encoding='utf-8')
f2 = open('topwords4.txt','a+',encoding='utf-8')

content_set = set()
for content in f1.readlines():
    content_set.add(content)


for i in content_set:
    f2.write(i)

f1.close()
f2.close()