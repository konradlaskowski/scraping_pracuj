import requests
from bs4 import BeautifulSoup

def fetch_job_salary(soup):
    salary_div = soup.find('div', {'class': 'offer-viewG5xQ1D'})
    
    if salary_div:
        salary_text = salary_div.get_text(separator=' ', strip=True)
        return salary_text
    else:
        return "N/A"

# Przykładowe użycie
url = "https://www.pracuj.pl/praca/technical-product-owner-olsztyn,oferta,1002785250"  # Zastąp prawdziwym adresem URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    salary = fetch_job_salary(soup)
    print(f"Salary: {salary}")
else:
    print("Failed to fetch the webpage.")
