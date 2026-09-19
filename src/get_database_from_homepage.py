import requests
from bs4 import BeautifulSoup


def get_headers_homepage(soup: BeautifulSoup) -> List:
  
	headers = soup.find_all('h1')
	headers_names = []

	for h in headers:
		headers_names.append(h.text.strip())

	return headers_names


def main():
    return "Hello!!"

if __name__ == '__main__':
	main()