import hashlib
from carteira import Carteira  

def calcular_hash(dado):
    return hashlib.sha256(dado.encode('utf-8')).hexdigest()

class ArvoreMerkle:
    def __init__(self, transacoes):
        self.transacoes = transacoes
        self.raiz = self.construir_arvore(transacoes)

    def construir_arvore(self, transacoes):
        if len(transacoes) == 0:
            return None
        if len(transacoes) == 1:
            return calcular_hash(str(transacoes[0]))

        
        hashes = [calcular_hash(str(transacao)) for transacao in transacoes]

        
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1]) 

            hashes = [calcular_hash(hashes[i] + hashes[i + 1]) for i in range(0, len(hashes), 2)]

        return hashes[0]

    def verificar_enderecos(self):
        for transacao in self.transacoes:
            if not Carteira.endereco_valido(transacao.remetente) or not Carteira.endereco_valido(transacao.destinatario):
                return False
        return True
