def main():
    i=0
    while i<3:
        print("meow")
        i=i+1

for _ in range(3):
    print("woof")

print("sniff\n"*3, end="")

j=0
while j<5:
    digite_a_senha = int(input("qual a senha? "))
    senha = int('1234')
    if digite_a_senha == senha:
        print('acesso permitido')
        break
    elif j==4:
        print('acesso bloqueado')
        break
    else:
        j=j+1




main()