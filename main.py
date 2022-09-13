N = int(input())
K = N // 3600
N = N % 3600
Р = N // 60
N = N % 60
print (K,':',Р,':',N,)