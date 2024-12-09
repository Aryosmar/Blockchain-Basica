from cadeia_de_blocos import CadeiaDeBlocos
from transacao import Transacao
from carteira import Carteira

def sincronizar_estado_global(nos):
    
    saldo_global = {}
    cadeia_global = max(nos, key=lambda no: len(no.cadeia)).cadeia
    for no in nos:
        for endereco, saldo in no.saldos.items():
            saldo_global[endereco] = max(saldo_global.get(endereco, 0), saldo)
    for no in nos:
        no.saldos = saldo_global
        no.cadeia = cadeia_global

def propagar_transacao(nos, transacao):
    sincronizar_estado_global(nos)
    for no in nos:
        try:
            no.adicionar_transacao(transacao)
            print(f"Transação propagada para o nó {id(no)}.")
        except ValueError as e:
            print(f"Falha ao propagar transação para o nó {id(no)}: {e}")

def propagar_bloco(nos, bloco):
    sincronizar_estado_global(nos)
    for no in nos:
        try:
            no.sincronizar_bloco(bloco)
            print(f"Bloco propagado para o nó {id(no)}.")
        except ValueError as e:
            print(f"Falha ao propagar bloco para o nó {id(no)}: {e}")

def resolver_conflito(nos):
    sincronizar_estado_global(nos)
    print("\nConflito resolvido: Todos os nós agora possuem a mesma cadeia.")

if __name__ == "__main__":
    
    bloco_genesis = CadeiaDeBlocos(dificuldade=2, recompensa=50).cadeia[0]

    
    no1 = CadeiaDeBlocos(dificuldade=2, recompensa=50)
    no2 = CadeiaDeBlocos(dificuldade=2, recompensa=50)
    no1.cadeia = [bloco_genesis]
    no2.cadeia = [bloco_genesis]
    nos = [no1, no2]

    
    minerador = Carteira.gerar_endereco()
    remetente1 = Carteira.gerar_endereco()
    destinatario1 = Carteira.gerar_endereco()

    
    for no in nos:
        no.saldos[remetente1] = 100

    
    transacao = Transacao(remetente1, destinatario1, 30, taxa=2)
    propagar_transacao(nos, transacao)

    
    no1.adicionar_bloco([transacao], minerador)
    propagar_bloco(nos, no1.obter_ultimo_bloco())

    
    transacao2 = Transacao(remetente1, destinatario1, 40, taxa=3)
    no2.adicionar_bloco([transacao2], minerador)

    
    resolver_conflito(nos)

    
    print("\n--- Cadeia do Nó 1 ---")
    no1.mostrar_cadeia()
    print("\n--- Cadeia do Nó 2 ---")
    no2.mostrar_cadeia()

    
    print("\n--- Histórico de Transações ---")
    for endereco in Transacao.historico_transacoes:
        Transacao.mostrar_historico(endereco)
