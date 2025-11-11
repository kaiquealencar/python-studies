from class_magic import Magia
import limpar_terminal

m = Magia()

print("Escolha seu set de magia: ")
m.listar_magias()
set_select = str(input("selecione um set de magia: "))
nome_set = str(input("Qual será o nome do seu set? "))


m.inserir_item(nome_set, str(set_select))
limpar_terminal.clear(str(input("Deseja limpar o terminal?  1 (sim) | 2 (não)")))

visulizar_magias = input("Deseja visulizar o nome do seu set e suas magias? 1 (sim) | 2 (não) ")


if visulizar_magias == '1':
    print(m)

alterar_nome_set = str(input("Deseja Alterar o nome do seu set? 1 (SIM) | 2 (NÃO) "))

if alterar_nome_set == '1':
    novo_nome_set = str(input("Informe o novo nome do seu set:  "))
    m.nome_set = novo_nome_set
    print(m)
else:
    print("Tchau!")