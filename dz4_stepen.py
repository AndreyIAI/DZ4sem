from random import randint as rd

k=int(input("Введите К: "))
for i in range(k,0,-1):
    x=rd(-100, 100)
    if x>0:
        print(f"+{x}x^{i}",end=" ")
    else:
        print(f"{x}x^{i}",end=" ")
print(rd(-100,100),end=" ")
rd=open('dz4Base.txt', 'w')
rd.write(k)
