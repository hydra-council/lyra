import ast
import importlib
import os
import sys


def verify_imports(script_path):
    allowed_modules = {'requests', 'json', 'bs4.BeautifulSoup', 'enum.Enum'}

    with open(script_path, 'r') as file:
        tree = ast.parse(file.read())

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ''
            for alias in node.names:
                imports.add(module + '.' + alias.name)

    result = imports - allowed_modules

    if not len(result) == 0:
        raise Exception(f'You are not allowed to import {result}')


def get_module_path(file_path):
    return f'{os.path.basename(os.path.dirname(file_path))}.{os.path.basename(file_path)}', file_path


class ScriptLoader:
    __module = None

    def is_loaded(self) -> bool:
        return self.__module is not None

    def load_script(self, path: str, module_name: str) -> tuple[bool, str]:
        try:
            verify_imports(path)
            spec = importlib.util.spec_from_file_location(module_name, path)
            self.__module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = self.__module
            spec.loader.exec_module(self.__module)
            return True, 'Success'

        except Exception as e:
            print(f'Error: {e}')
            return False, str(e)

    def unloadScript(self):
        self.__module = None

    def get_book(self, book_link):
        module = self.__module
        res = module.get_book_metadata(book_link)
        assert isinstance(res, dict)
        return res

    def get_chapter(self, chapter_link):
        module = self.__module
        res = module.get_chapter_images(chapter_link)
