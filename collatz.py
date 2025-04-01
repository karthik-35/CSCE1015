for i in range(1,1001):
 a=0
 n=i
 while n-1:a+=1;n=n//2 if n%2<1 else 3*n+1
 print(a)
