import os

x = "n"
#Variavel do while

while x != "y":

    print("Olá")
    print("")
    print("1-Registrar atleta")
    print("2-Alterar")
    print("3-Listar")
    print("4-Sair")
    op = int(input("Digite o numero equivalente a opção que deseja: "))
    #Opções do menu

    os.system("cls")

    if op == 1:
        na = int(input("Digite quantos atletas irão competir: "))

        atletas = []

        for i in range(na):        
            nome = input("Digite o nome do atleta: ")
            nome.append(atletas)

        saltos = []

        for j in range(5):
            salto = float(input(f"Digite o valor do {j+1}o salto: "))
            salto.append(saltos)
    
    elif op == 2:
        print("Não fiz essa opção")
    
    elif op == 3:
        print(atletas) and print(saltos)

        os.system("pause")


    elif op == 4:
        x = "y"
    else:
        print("Essa opção não consta na lista.")

    os.system("pause")


    