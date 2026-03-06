def geometriaplana():
    while True:
        print()
        print("-----Escolha um formato-----")
        print("1 - Quadrado")
        print("2 - Triângulo")
        print("3 - Circulo")
        print("4 - Losango")
        print("5 - Trapézio")
        print("6 - Retângulo")
        print("7 - Voltar")
        escolhafigura = int(input("Escolha: "))
        if escolhafigura == 1:
            quadrado()
        elif escolhafigura == 2:
            triângulo()
        elif escolhafigura == 3:
            circulo()
        elif escolhafigura == 7:
            break

def quadrado ():
    print()
    lado = int(input("Insira o valor do lado desse quadrado (cm): "))
    while True:
        print()
        print('-----Escolha um calculo-----')
        print("1 - Area")
        print("2 - Perimetro")
        print("3 - Voltar")
        escolhacalculo = int(input("Escolha: "))
        if escolhacalculo == 1:
            area = lado*lado
            print(f'A area deste quadrado será de {area}')
            print()
            continue
        if escolhacalculo == 2:
            perimetro = lado + lado
            print(f'O perimetro deste quadrado será de {perimetro}')
            print()
            continue
        elif escolhacalculo == 3:
            break

def triângulo():
    while True:
        print()
        print('-----Escolha um calculo-----')
        print("1 - Area")
        print("2 - Perimetro")
        print("3 - Voltar")
        escolhacalculo = int(input("Escolha: "))
        if escolhacalculo == 1:
            print()
            base = int(input("Insira a base deste triângulo (cm): "))
            altura = int(input("Agora insira a altura deste triângulo (cm): "))
            print(f'A area deste triangulo será de {base*altura}')
        elif escolhacalculo == 2:
            print()
            lado = int(input("Me de o primeiro lado (cm): "))
            lado2 = int(input("Me de o segundo lado (cm): "))
            lado3 = int(input("Me de o terceiro lado (cm): "))
            perimetro = lado+lado2+lado3
            print(f'O perimetro deste triângulo sera de {perimetro}')
        elif escolhacalculo == 3:
            break



def circulo():
    print()
    raio = int(input("Insira o raio deste circulo: "))
    pi = 3
    while True:
        print()
        print('-----Escolha um calculo-----')
        print('1 - Area')
        print('2 - Comprimento')
        print('3 - Voltar ')
        escolha = int(input("Escolha: "))
        if escolha == 1:
            area = pi*(raio*raio)
            print()
            print(f'A area deste circulo será de {area}')
        elif escolha == 2:
            comprimento = 2*pi*raio
            print()
            print(f'O comprimento deste circulo será de {comprimento}')
        elif escolha == 3:
            break



def losango():
    print()
    diagmaior = int(input("Insira a diagonal maior deste losango: "))
    diagmenor = int(input("Insira a diagonal menor deste losango: "))
    while True:
        print()
        print('-----Escolha um calculo-----')
        print('1 - Area')
        print('2 - Sair')
        escolha = int(input("Escolha: "))
        if escolha == 1:
            area = (diagmaior*diagmenor)/2
            print(f"A area deste losango é de {area}")
        elif escolha == 2:
            break


def trapezio():
    print()
    basemaior = int(input("Insira a base maior deste trapezio: "))
    basemenor = int(input("insira a base menor deste trapezio: "))
    altura = int(input("insira a altura deste trapezio: "))
    while True:
        print()
        print('-----Escolha um calculo-----')
        print('1 - Area')
        print('2 - Sair')
        escolha = int(input("Escolha: "))
        if escolha == 1:
            area = ((basemaior+basemenor)*altura)/2
            print(f"A area deste trapezio é de {area}")

        elif escolha == 2:
            break


def inicio():
    while True:
        print("-"* 28)
        print("1 - Geometria Plana")
        print("2 - Geometria Espacial")
        print("3 - Sair")
        print("-" * 28)
        escolha = int(input("Escolha: "))
        if escolha == 1:
            geometriaplana()
        elif escolha ==3:
            break




inicio()
