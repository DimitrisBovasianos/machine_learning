import csv

lines = []
with open('file4.txt','r') as f:
    i = 0
    for word  in f:
        x = list(word)
        lines.append([x[0],x[1],x[len(word)-3],x[len(word)-2],word])
for word in lines:
    for i in range(0,len(word)-1):
        word[i] = ord(word[i])

with open('test1.csv','w') as file:
    writer = csv.writer(file)
    for i in lines:
        writer.writerow(i)
