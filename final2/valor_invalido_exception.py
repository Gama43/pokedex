class ValorInvalidoException(Exception):
    def __init__(self):
        super().__init__('Valor inválido')