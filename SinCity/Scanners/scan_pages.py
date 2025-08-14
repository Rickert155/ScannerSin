from SinCity.colors import RED, RESET, GREEN
from SinCity.Agent.header import header
from SinCity.Scanners.miniTools import get_domain, selectFile
import requests

def ListPages(doc:str):
    list_pages = set()

    with open(doc, 'r') as file:
        for line in file.readlines():
            page = line.strip()
            list_pages.add(page)
    
    return list_pages

def iterationPage(domain:str, doc:str):
    start_url = f'http://{domain}'
    
    list_pages = ListPages(doc=doc)

    number_page = 0
    
    divide_line = '-'*50
    
    success = 0
    for page in list_pages:
        url = f'{start_url}/{page}'
        head = header()
        try:
            response = requests.get(url, headers=head)
            status = response.status_code
            if status == 200:
                number_page+=1
                success+=1
                if success == 1:
                    print(
                            f'+{GREEN}{divide_line}{RESET}\n'
                            f'|{GREEN}\t\tОбнаруженные страницы {RESET}'
                            )
                print(
                        f'+{GREEN}{divide_line}{RESET}\n'
                        f'|{GREEN} [{number_page}] {page}{RESET} | {url}'
                        )
        except requests.exceptions.ConnectionError:
            print(f'{RED}Ошибка при подключении{RESET}')
    if success == 0:
        print(f'{RED}Страницы по словарю не обнаружены{RESET}')



"""Стартовая функция, с нее все начинается"""
def SearchPages():
    """Выбор файл со словарем, по которому будут искаться страницы"""
    start_file = selectFile(type_file=".txt")
    if start_file == None:
        print(f'{RED}Словарь не обнаружен!{RESET}')
        return
    
    """Получаем домен от пользователя"""
    domain = get_domain()
    
    if domain != None:
        """Если все ок - идем проверять страницы"""
        iterationPage(domain=domain, doc=start_file) 
    if domain == None:
        print(f'{RED}Проверь правильность введенных данных{RESET}')
        return

if __name__ == '__main__':
    try:
        SearchPages()
    except KeyboardInterrupt:
        print(f'{RED}\nBye Bye{RESET}')

