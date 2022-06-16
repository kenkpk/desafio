n=float(input("Digite seu salario"))
m=int(input("digite ano do reajuste"))
if m==2017:
    a=n/100.0*6.47
elif m==2016:
    a=n/100.0*11.67
elif m==2015:
    a=n/100.0*8.80
else:
    a=0
r=n+a
print("Seu salario reajustado é de:", r)
print("O aumento do seu salario foi de:", a)