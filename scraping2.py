import requests
from bs4 import BeautifulSoup




def Find_Job_Title(url):
    # Wykonaj zapytanie HTTP GET do strony
    response = requests.get(url)

    # Sprawdź, czy zapytanie zakończyło się sukcesem (kod statusu 200)
    if response.status_code == 200:
        # Parsuj treść strony przy pomocy Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # # Znajdź element o podanej klasie
        # element = soup.find('ul', class_=class_name)
        #     # Znajdź element <h1> z odpowiednimi atrybutami
        job_title_element = soup.find('h1', {'data-scroll-id': 'job-title', 'data-test': 'text-positionName'})
        if job_title_element:
            job_title = job_title_element.text  # Pobierz tekst z elementu
            return job_title
        

        
        # Wydrukuj tekst znalezionego elementu
    #     if element:
    #         # Znajdź wszystkie elementy <li> wewnątrz znalezionego elementu
    #         technologies_elements = element.find_all('li')
            
    #         # Wyodrębnij tekst z każdego elementu <li> i zapisz go w liście
    #         technologies = [tech.text for tech in technologies_elements]
            
    #         print("Znalezione technologie:", technologies)
    #     else:
    #         print(f"Nie znaleziono elementu o klasie {class_name}.")
    # else:
    #     print(f"Błąd: Nie udało się pobrać strony (kod statusu: {response.status_code})")

# Test funkcji
# fetch_technologies_from_class("https://www.pracuj.pl/praca/python-developer-krakow,oferta,1002780902", "job-title"
print(Find_Job_Title("https://www.pracuj.pl/praca/python-developer-krakow,oferta,1002780902"))