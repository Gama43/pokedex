class Duplicado(Exception):
    def __init__(self):
        super().__init__('Item duplicado')