# "CinePython"
class FabricaDeProdutos:
    def eras(self, ingressos):
        self.ingressos = ingressos

    def FabricaRetro(self):
        print("Você escolheu o estilo retrô!")
        print("Ingresso de papel + combo clássico com pipoca e refrigerante.")
        return None

    def FabricaModerna(self):
        print("Você escolheu o estilo moderno!")
        print("Ingresso com QR code + pipoca gourmet + suco natural.")
        return None

print("Bem-vindo ao CinePython!")
opcao = int(input("Escolha o tipo de ingresso que deseja comprar:\n1 - Retrô ('Ingresso de papel + combo clássico com pipoca e refrigerante.')\n2 - Moderna ('Ingresso com QR code + pipoca gourmet + suco natural')\n→ "))

meu_ingresso = FabricaDeProdutos()
meu_ingresso.eras(opcao)

if opcao == 1:
    meu_ingresso.FabricaRetro()
elif opcao == 2:
    meu_ingresso.FabricaModerna()
else:
    print("Opção inválida!")

        

