import requests
from bs4 import BeautifulSoup
import testy
import wykres



f2 = open("MYtechLinki.txt", "a")
f3 = open('MYtechLISTA.txt', "a")
f4 = open('MYtechZUPA.txt', "a")



def fetch_search_name(soup):
    # Znajdź element <h1> z atrybutem data-test o wartości "header-title"
    header_title = soup.find('h1', {'data-test': 'header-title'})

    # Pobierz tekst z elementu
    if header_title:
        search_name = header_title.text
        return search_name




def fetch_job_salary(soup):
    salary_div = soup.find('div', {'class': 'offer-viewG5xQ1D'})
    
    if salary_div:
        salary_text = salary_div.get_text(separator=' ', strip=True)
        return salary_text
    else:
        return "N/A"


def fetch_job_links(soup):
        job_elements = soup.find_all('a', {'data-test': 'link-offer'})
        job_links = [job['href'] for job in job_elements]
            
        return job_links

def give_me_search_html_soup(url):
    response = requests.get(search_results_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

def give_me_job_html_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup


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




technologie = []
for x in range(1, 2):
    search_results_url = f"https://it.pracuj.pl/praca/rawa%20mazowiecka;wp?rd=30&its=backend"
    print(f" Przechodze do następnej strony: {search_results_url}")
    
    soup = give_me_search_html_soup(search_results_url)
    search_name = fetch_search_name(soup)
    
    job_links = fetch_job_links(soup)
    for job_link in job_links:
        
        technologies = fetch_technologies_from_class(job_link, "offer-viewEX0Eq-")
        technologie = technologie + technologies
        job_soup = give_me_job_html_soup(job_link)
        salary = fetch_job_salary(job_soup)
        print(f"Odczytywanie: {job_link}")
        print(technologies)
        print(salary)
        print()

        f2.write(f'{job_link}\n{technologie}\n')
        


print('Liczę i segreguje Technologie')


f3.write(str(technologie))
f3.close()
najlepsze_technologie = testy.policz_posegreguj_technologie(technologie)




print('Zapisuje do pliku')

f = open("MytechNajlepsze_technologie.txt", "a")
f.write(str(najlepsze_technologie))
f.close()
f2.close()

print('Zapisano do pliku')

for x in najlepsze_technologie:
    print(f'{x} : {najlepsze_technologie[x]}')

wykres.pokaz_na_wykresie(najlepsze_technologie, search_name)






