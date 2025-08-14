from SinCity.colors import RED, RESET, GREEN
import os, sys

def get_domain():
    domain = input("Domain: ")
    if '//' in domain:domain = domain.split('//')[1]
    if '/' in domain:domain = domain.split('/')[0]
    if 'www.' in domain:domain = domain.split('www.')[1]
    if '@' in domain:domain = domain.split('@')[1]
    if '.' not in domain:domain = None
    try:
        a, b = domain.split('.')
        if len(a) <= 1 and len(b) <= 1:domain = None
    except:domain = None

    return domain

def selectFile(type_file:str):
    list_files = []
    
    for doc in os.listdir():
        if type_file in doc and 'requirements' not in doc \
                and doc != 'package.txt':
            list_files.append(doc)
    
    if len(list_files) == 0:
        return None
    
    divide_line = '-'*50
    if len(list_files) > 0:
        number_doc = 0
        for doc in list_files:
            number_doc+=1
            print(
                    f'+{GREEN}{divide_line}{RESET}\n'
                    f'|{GREEN}[{number_doc}] {doc}{RESET}'
                    )

        selectItem = input(
            f'+{GREEN}{divide_line}{RESET}\n'
            f'{GREEN}Выбери документ с твоим словарем: {RESET}'
            )
        try:
            selectItem = int(selectItem)
        except:
            print(f'{RED}Необходимо ввести цифру{RESET}')
            sys.exit()

        if 1 <= selectItem and selectItem <= len(list_files):
            file = list_files[selectItem-1]
            return file
        else:
            print(f'{RED}Некорректный выбор!{RESET}')

