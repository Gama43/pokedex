class NaoEhString(Exception):
    def __init__(self):
        super().__init__('Valor não é uma string')