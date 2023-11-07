
class AttributeChangeError(Exception):
    """Исключение при попытке изменить значение защищенного атрибута"""
    def __init__(self, attr_name):
        super().__init__(f'access to the attribute change {attr_name!r} is closed')