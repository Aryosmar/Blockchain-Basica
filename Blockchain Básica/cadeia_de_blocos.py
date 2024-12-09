from bloco import Bloco
from transacao import Transacao
from carteira import Carteira

class CadeiaDeBlocos:
    def __init__(self, dificuldade=1, recompensa=50):
        self.dificuldade = dificuldade
        self.recompensa = recompensa
        self.saldos = {}  
        self.cadeia = [self.criar_bloco_genesis()]  

    def criar_bloco_genesis(self):
        remetente = Carteira.gerar_endereco()
        destinatario = Carteira.gerar_endereco()
        transacao_genesis = Transacao(remetente, destinatario, 1, transacao_genesis=True)
        self.saldos[remetente] = 1  
        return Bloco(0, [transacao_genesis], "0", self.dificuldade)

    def obter_ultimo_bloco(self):
        return self.cadeia[-1]

    def atualizar_saldos(self, bloco):
        for transacao in bloco.transacoes:
            if transacao.remetente != "Sistema":
                self.saldos[transacao.remetente] -= (transacao.valor + transacao.taxa)
            if transacao.destinatario in self.saldos:
                self.saldos[transacao.destinatario] += transacao.valor
            else:
                self.saldos[transacao.destinatario] = transacao.valor

    def validar_transacoes(self, transacoes):
        for transacao in transacoes:
            if transacao.remetente != "Sistema" and self.saldos.get(transacao.remetente, 0) < (transacao.valor + transacao.taxa):
                raise ValueError(f"Saldo insuficiente para o remetente: {transacao.remetente}")

    def adicionar_bloco(self, novas_transacoes, minerador):
        self.validar_transacoes(novas_transacoes)

        
        taxas_totais = sum(transacao.taxa for transacao in novas_transacoes)
        recompensa_total = self.recompensa + taxas_totais

        
        transacao_recompensa = Transacao("Sistema", minerador, recompensa_total, transacao_genesis=True)
        novas_transacoes.append(transacao_recompensa)

        
        ultimo_bloco = self.obter_ultimo_bloco()
        novo_bloco = Bloco(len(self.cadeia), novas_transacoes, ultimo_bloco.hash_atual, self.dificuldade)
        self.cadeia.append(novo_bloco)

        
        self.atualizar_saldos(novo_bloco)

        print(f"\n--- Bloco {novo_bloco.indice} adicionado ---")
        print(f"  Transações:")
        for transacao in novas_transacoes:
            print(f"    {transacao}")
        print(f"  Hash Atual: {novo_bloco.hash_atual}")
        print(f"  Hash Anterior: {novo_bloco.hash_anterior}")
        print(f"  Raiz Merkle: {novo_bloco.arvore_merkle.raiz}")
        print(f"  Nonce: {novo_bloco.nonce}")
        print("---------------------------")

    def adicionar_transacao(self, transacao):
        if not isinstance(transacao, Transacao):
            raise ValueError("Transação inválida.")
        if self.validar_transacoes([transacao]):
            return transacao
        else:
            raise ValueError("Transação inválida ou saldo insuficiente.")

    def sincronizar_bloco(self, bloco):
        if bloco.hash_anterior == self.obter_ultimo_bloco().hash_atual and bloco.hash_atual.startswith('0' * self.dificuldade):
            self.cadeia.append(bloco)
            self.atualizar_saldos(bloco)
        else:
            raise ValueError("Bloco inválido ou não sincronizado com a cadeia atual.")

    def mostrar_saldos(self):
        print("\n--- Saldos dos Endereços ---")
        for endereco, saldo in self.saldos.items():
            print(f"  {endereco}: {saldo}")
        print("---------------------------")

    def mostrar_cadeia(self):
        print("\n--- Cadeia de Blocos ---")
        for bloco in self.cadeia:
            print(f"\nBloco {bloco.indice}:")
            print(f"  Transações:")
            for transacao in bloco.transacoes:
                print(f"    {transacao}")
            print(f"  Hash Atual: {bloco.hash_atual}")
            print(f"  Hash Anterior: {bloco.hash_anterior}")
            print(f"  Raiz Merkle: {bloco.arvore_merkle.raiz}")
            print(f"  Nonce: {bloco.nonce}")
            print("---------------------------")
