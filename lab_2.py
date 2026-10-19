import csv
import random
from xml.dom import minidom

with open("books.csv", encoding="cp1251") as f:
    books = list(csv.DictReader(f, delimiter=";"))

print("Длинных названий:", sum(len(b["Название"]) > 30 for b in books))

# 2) поиск по автору, цена до 200 руб.
author = input("Автор: ").lower()
for b in books:
    price = float(b["Цена поступления"].replace(",", "."))
    if author in b["Автор"].lower() and price <= 200:
        print(b["Название"], "|", b["Автор"], "|", price)

# 3) 20 библиографических ссылок в файл
with open("references.txt", "w", encoding="utf-8") as f:
    for i, b in enumerate(random.sample(books, 20), 1):
        year = b["Дата поступления"][6:10]
        f.write(f"{i}. {b['Автор']}. {b['Название']} - {year}\n")

# XML: словарь NumCode - CharCode
codes = {}
for v in minidom.parse("currency.xml").getElementsByTagName("Valute"):
    num = v.getElementsByTagName("NumCode")[0].firstChild.data
    char = v.getElementsByTagName("CharCode")[0].firstChild.data
    codes[int(num)] = char
print(codes)

# доп 1: теги без повторений
tags = {t.strip() for b in books for t in b["Жанр книги"].split("#") if t.strip()}
print(sorted(tags))

# доп 2: 20 самых популярных книг
top = sorted(books, key=lambda b: int(b["Кол-во выдач"]), reverse=True)[:20]
for i, b in enumerate(top, 1):
    print(i, b["Название"], "-", b["Автор"], b["Кол-во выдач"])
