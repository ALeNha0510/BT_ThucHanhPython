a = int(input("Nhập một số nguyên: "))

a1 = int("%i" %a)
a2 = int("%i%i" %(a, a))
a3 = int("%i%i%i" %(a, a, a))
an = a1 + a2 + a3

print(f"{a1} + {a2} + {a3} = {an}")