import requests
import re
from bs4 import BeautifulSoup

MEGABOX = 'https://www.megaboxatacado.com.br'

def get_headers_homepage(soup: BeautifulSoup) -> List:
  
	headers = soup.find_all('h1')
	headers_names = []

	for h in headers:
		headers_names.append(h.text.strip())

	return headers_names


def get_links_from_menus(soup: BeautifulSoup) -> List:

	divs_menu = soup.find('div', 'submenu_left')
	links = divs_menu.find_all('a', href = True)

	all_links_extracted = [l['href'] for l in links]
	links_ready = [f'{MEGABOX}{l}' for l in all_links_extracted]

	return links_ready

def get_labels_products(links: list):
	
	data = {}

	for link in links:
		response = requests.get(link)
		html = response.text
		page = BeautifulSoup(html, 'html.parser')
		labels = page.find('div', 'content_select_list').find_all('label')

		extract_brand_class = re.search(r'/([^/]+)/ss', link)

		if extract_brand_class:
			brand_class = extract_brand_class.group(1)

		brands = []

		for brand in labels:
			pattern = r'^(.*?)\s*\(\d+\s*ítens\)'

			result = re.search(pattern, brand.getText())
			if result:
				brand_treated = result.group(1).strip()
				brands.append(brand_treated)

		data[brand_class] = brands
		
	return data


def main():
    return "Hello!!"

if __name__ == '__main__':
	main()