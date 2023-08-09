l=[1,4,1,6,"hello","a",5,"hello"]
double=[]
for i in l:
 if l.count(i)>1 and i not in double:
  double.append(i)
print ("Повторяющие элементы", double)