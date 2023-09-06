from importlib.util import spec_from_file_location, module_from_spec
from utils import load_file, Path, path, modules

def ask_for_file() -> 'module':
    """
        Функция запрашивает путь к файлу и копирует этот файл
        Возвращает объект модуля, созданного при импортировании файла
    """
    
    while True:
        user_path = input(' > Введите путь к файлу: ')
        file_path = Path(path[0]) / user_path

        if file_path.is_file():
            break
        else:
            print('Файл не найден!')

    module_path = load_file(file_path)
    module_name = module_path.name[:-3]

    spec = spec_from_file_location(module_name, module_path)
    module_import = module_from_spec(spec)
    modules[module_name] = module_import
    spec.loader.exec_module(module_import)
    
    return module_import
    
# >>> config_module = ask_for_file()
#  > Введите путь к файлу: D:\temp\home\2023.09.03\data\None
# Файл не найден!
#  > Введите путь к файлу: D:\temp\home\2023.09.03\data\conf.py
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
