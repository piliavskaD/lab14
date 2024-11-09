from bs4 import BeautifulSoup
import json
import requests

def open_lang(lang_file):
    with open(lang_file, "r") as f:
       langs = f.read().splitlines()
    return langs

my_lang = open_lang("lang.txt")
    

def open_pages(pagea_file):
    with open(pagea_file, "r") as ff:
        pages = ff.read().splitlines()
    return pages


def count_lang_freq(pages, langs):
    res = {}

    for i in pages:
        response = requests.get(i)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text().lower()

        page_res = {}
        for lang in langs:
            page_res[lang] = page_text.count(lang.lower())

        res[i] = page_res

    return res

def save_json(data, name_json):
    with open(name_json, "w") as json_file:
        json.dump(data, json_file, indent=4)


langs = open_lang("lang.txt")
pages = open_pages("pages.txt")
frequwncy = count_lang_freq(pages, langs)
save_json(frequwncy, "popular.json")