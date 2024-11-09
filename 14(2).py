import requests
from bs4 import BeautifulSoup

def open_f(name_f):
    with open(name_f, "r") as f:
        pages = f.read().splitlines()
    return pages

def count_pic(pages):

    img_count = {}

    for page in pages:
        try:
            response = requests.get(page)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            images = soup.find_all("img")
            img_count[page] = len(images)

        except requests.exceptions.RequestException as e:
            print(f"Помилка при завантаженні сторінки {page}: {e}")
            img_count[page] = 0

    return img_count

if __name__ == "__main__":
    pages = open_f("webpages.txt")
    image_counts = count_pic(pages) 

    
    print("COUNTS:")
    for page, count in image_counts.items():
        print(f"{page}: {count} images")