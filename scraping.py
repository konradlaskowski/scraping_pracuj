import requests
from bs4 import BeautifulSoup
import testy

def fetch_job_title(html):
    job_title_element = html.find('h1', {'data-scroll-id': 'job-title', 'data-test': 'text-positionName'})
    if job_title_element:
        job_title = job_title_element.text  # Pobierz tekst z elementu
        return job_title
    
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

def give_me_html_soup(url):
    response = requests.get(search_results_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def fetch_job_links(soup):
        job_elements = soup.find_all('a', {'data-test': 'link-offer'})
        job_links = [job['href'] for job in job_elements]
            
        return job_links




# Pobierz linki do ofert pracy z wyników wyszukiwania
search_results_url = "https://it.pracuj.pl/praca?itth=37"

job_links = fetch_job_links(give_me_html_soup(search_results_url))




# Dla każdej oferty pracy pobierz wymagane technologie i zapisz w liście
technologie = []
for job_link in job_links:
    technologies = fetch_technologies_from_class(job_link, "offer-viewEX0Eq-")
    technologie = technologie + technologies
    print(f"Odczytywanie: {job_link}")

najlepsze_technologie = testy.policz_posegreguj_technologie(technologie)
    


# print(technologie)


f = open("technologie.txt", "a")
f.write(str(najlepsze_technologie))
f.close()