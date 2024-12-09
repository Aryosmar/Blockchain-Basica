import random
import string

class Carteira:
    enderecos_gerados = set()  

    @staticmethod
    def endereco_valido(endereco):
        """
        Verifica se o endereço possui a estrutura desejada:
        - Começa com '2x'
        - Contém exatamente 48 caracteres alfanuméricos (A-Z, 0-9) após '2x'
        """
        return len(endereco) == 50 and endereco[:2] == "2x" and all(
            c in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in endereco[2:]
        )

    @staticmethod
    def gerar_endereco():
        """
        Gera um endereço único com a estrutura '2x' seguido de 48 caracteres alfanuméricos.
        Garante que o endereço não foi gerado anteriormente.
        """
        while True:
            endereco = "2x" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=48))
            if endereco not in Carteira.enderecos_gerados:
                Carteira.enderecos_gerados.add(endereco)
                return endereco
