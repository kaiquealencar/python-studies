from class_magic import Magia
import limpar_terminal as lt

m = Magia()
print("Escolha seu set de magia: ")
m.listar_magias()
set_select = str(input("selecione um set de magia: "))
nome_set = str(input("Qual será o nome do seu set? "))


m.inserir_item(nome_set, str(set_select))
lt.clear(str(input("Deseja limpar o terminal?  1 (sim) | 2 (não)")))

visulizar_magias = input("Deseja visulizar o nome do seu set e suas magias? 1 (sim) | 2 (não) ")


if visulizar_magias == '1':
    print(m)

m.salvar_em_arquivo()

alterar_nome_set = str(input("Deseja Alterar o nome do seu set? 1 (SIM) | 2 (NÃO) "))

if alterar_nome_set == '1':
    novo_nome_set = str(input("Informe o novo nome do seu set:  "))
    m.nome_set = novo_nome_set
    m.salvar_em_arquivo()
    print(m)    
elif input("Deseja ver seu arquivo com set de magias? SIM (1) NÃO (2)") == '1':
    lt.clear("1")
    m.carregar_de_arquivo()
else:
    print("Tchau!")
    exit()



