from carteira import Carteira

class Transacao:
    
    enderecos_gerados = set()
    historico_transacoes = {}

    def __init__(self, remetente, destinatario, valor, taxa=0, transacao_genesis=False):
        
        if remetente != "Sistema" and not Carteira.endereco_valido(remetente):
            raise ValueError(f"Endereço de remetente inválido: {remetente}")
        if not Carteira.endereco_valido(destinatario):  # Validar destinatário
            raise ValueError(f"Endereço de destinatário inválido: {destinatario}")
        
        
        if valor <= 0 and not transacao_genesis:
            raise ValueError(f"Valor inválido: {valor}. O valor deve ser positivo.")
        
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
        self.taxa = taxa

        
        Transacao.adicionar_ao_historico(remetente, self)
        Transacao.adicionar_ao_historico(destinatario, self)

    def __str__(self):
        return f"{self.remetente} envia {self.valor} para {self.destinatario} (Taxa: {self.taxa})"

    @staticmethod
    def adicionar_ao_historico(endereco, transacao):
        
        if endereco in Transacao.historico_transacoes:
            Transacao.historico_transacoes[endereco].append(transacao)
        else:
            Transacao.historico_transacoes[endereco] = [transacao]

    @staticmethod
    def mostrar_historico(endereco):
        if endereco in Transacao.historico_transacoes:
            print(f"\n--- Histórico de Transações para o endereço {endereco} ---")
            for transacao in Transacao.historico_transacoes[endereco]:
                print(f"  {transacao}")
            print("-------------------------------")
        else:
            print(f"Nenhuma transação encontrada para o endereço {endereco}.")
