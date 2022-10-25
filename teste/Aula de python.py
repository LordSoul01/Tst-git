print("Programa de Concessão de aposentadoria")

idade = input("Qual a sua idade? ")
sexo = input("Qual o seu sexo ? \n Digite M para masculino e F para feminino ")

if sexo.upper() == 'M':
    if int(idade) >= 65:
         print("Aposentadoria concedida")
    else:
        print(f"Ainda não foi concedida a sua aposentadoria. \n Aguarde mais {65 - int(idade)} anos")

elif sexo.upper() == 'F':
    if int(idade) >= 60:
        print("Aposentadoria concedida")

    else:
        print(f"Ainda não foi concedida a sua aposentadoria. \n Aguarde mais {60 - int(idade)} anos")

else:
    print("Opção Inválida! \n  Por favor, tente novamente")