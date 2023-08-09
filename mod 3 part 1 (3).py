n=int(input())
summa_ziphr=0

while n>0:
 x=n%10
 summa_ziphr=summa_ziphr+x
 n=n//10
print("Cумма цифр : ",summa_ziphr)