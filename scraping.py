import requests
# from bs4 import BeautifulSoup




# def fetch_technologies_from_class(url, class_name):
#     # Wykonaj zapytanie HTTP GET do strony
#     response = requests.get(url)

#     # Sprawdź, czy zapytanie zakończyło się sukcesem (kod statusu 200)
#     if response.status_code == 200:
#         # Parsuj treść strony przy pomocy Beautiful Soup
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Znajdź element o podanej klasie
#         element = soup.find('ul', class_=class_name)
        
#         # Wydrukuj tekst znalezionego elementu
#         if element:
#             # Znajdź wszystkie elementy <li> wewnątrz znalezionego elementu
#             technologies_elements = element.find_all('li')
            
#             # Wyodrębnij tekst z każdego elementu <li> i zapisz go w liście
#             technologies = [tech.text for tech in technologies_elements]
            
#             print("Znalezione technologie:", technologies)
#         else:
#             print(f"Nie znaleziono elementu o klasie {class_name}.")
#     else:
#         print(f"Błąd: Nie udało się pobrać strony (kod statusu: {response.status_code})")

# # Test funkcji
# fetch_technologies_from_class("https://www.pracuj.pl/praca/python-developer-krakow,oferta,1002780902", "offer-viewEX0Eq-")

# fetch_technologies_from_class("https://www.pracuj.pl/praca/junior-python-developer-mazowieckie,oferta,10102249?sug=oferta_bottom_bd_5_tname_179_tgroup_A", "offer-viewEX0Eq-")import requests
from bs4 import BeautifulSoup

def fetch_technologies_from_class(url, class_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find('ul', class_=class_name)
        if element:
            technologies_elements = element.find_all('li')
            technologies = [tech.text for tech in technologies_elements]
            return technologies
    return []

# def fetch_job_title(html):
#             job_title_element = html.find('h1', {'data-scroll-id': 'job-title', 'data-test': 'text-positionName'})
#             if job_title_element:
#                 job_title = job_title_element.text  # Pobierz tekst z elementu
#                 return job_title

def fetch_job_links(search_results_url):
    response = requests.get(search_results_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_elements = soup.find_all('a', {'data-test': 'link-offer'})
        job_links = [job['href'] for job in job_elements]
        job_title_element = soup.find('h1', {'data-scroll-id': 'job-title', 'data-test': 'text-positionName'})
        
        
        if job_title_element:
            job_title = job_title_element.text  # Pobierz tekst z elementu
            
        return [job_links + job_title]
    return []

# Pobierz linki do ofert pracy z wyników wyszukiwania
search_results_url = "https://it.pracuj.pl/praca?itth=37"
job_links = fetch_job_links(search_results_url)

technologie = []
# Dla każdej oferty pracy pobierz wymagane technologie
for job_link in job_links:
    technologies = fetch_technologies_from_class(job_link, "offer-viewEX0Eq-")
    technologie.append(technologies)
    # print(f"Technologie dla oferty {job_link}: {technologies}")

f = open("technologie.txt", "a")
f.write("Now the file has more content!")
f.close()