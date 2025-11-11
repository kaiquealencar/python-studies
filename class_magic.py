import json
from pathlib import Path
class Magia:

    def __init__(self):
        self.__lista_magia_1 = ["Estupefaça", "Expelliarmus", "Petrificus Totalus"]
        self.__lista_magia_2 = ["Wingardium Leviosa", "Alohomora", "Lumos", "Nox"] 
        self.__lista_magias_trevas = ["Avada Kedavra", "Crucio", "Imperio"]      
        self.__lista_magia = []
        self.__nome_set_jogador = ''

        
    def listar_magias(self, imprimir=True):
       sets = {
            '1': self.__lista_magia_1,
            '2': self.__lista_magia_2,
            '3': self.__lista_magias_trevas

       }  
       if imprimir:
        for num, lista in sets.items():
            print("-"*30)
            print(f"Set de magia {num}: ")
            for magia in lista:
                print(f"  -  {magia}")
        return sets


    def inserir_item(self, nome_set, set_select):
        sets = {
            "1": self.__lista_magia_1,
            "2": self.__lista_magia_2,
            "3": self.__lista_magias_trevas
        }
        self.__lista_magia = sets.get(set_select, [])
        self.__nome_set_jogador = nome_set    

    def salvar_em_arquivo(self, nome_arquivo="set_magia.json"):
        caminho = Path(nome_arquivo)
        dados = {
            "nome_set": self.__nome_set_jogador,
            "magias": self.__lista_magia
        }

        caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=4), encoding='utf-8')

#        with open(nome_arquivo, 'w', encoding='utf-8') as f:
#            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Set de magias salvo com sucesso!")

    def carregar_de_arquivo(self, nome_arquivo="set_magia.json"):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.__nome_set_jogador = dados.get("nome_set", "")
                self.__lista_magia = dados.get("magias", [])
            print(f"Set de magias {self.__nome_set_jogador} carregado com sucesso!")
            
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")            
            return True
        except FileNotFoundError:
            print("Arquivo não encontrado. Nenhum set foi carregado!")
            return False

    def __str__(self):
        return f"Seu set se chama: {self.nome_set} e suas magias são: {','.join(self.__lista_magia)}"        
        

    @property
    def magias(self):
        return self.__lista_magia.copy()
    

    @property    
    def nome_set(self):
        return self.__nome_set_jogador.upper()

    @nome_set.setter
    def nome_set(self, novo_nome):
        self.__nome_set_jogador = novo_nome

        


        
        






        
