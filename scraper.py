#Part 1.1: Imports
print("Script is running")
import requests #used to send requests to web
from bs4 import BeautifulSoup #used to read and navigate HTML
import csv #used to save data as CSV format
import json #used to save data as JSON format
import re #used for cleaning text (regex)
from collections import Counter #count occurances for summary

URL = "https://quotes.toscrape.com" #site being scraped

#Part 1.2: fetch data safely
try:
    response = requests.get(URL) 
    response.raise_for_status() #raises error if not 200 (request unsuccessful)
    print("Successfully fetched the page")
except requests.exceptions.RequestException as e:
    print("Error fetching page:", e)
    exit()

#Save raw HTML into raw.html
with open("raw.html", "w", encoding="utf-8") as file:
    file.write(response.text)

#Part 2.1: Data Extraction

#parse HTML into something readable
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = [] #create empty list to store all quotes

quotes = soup.find_all("div", class_="quote") #find all quote blocks on page

#loop through each quote
for q in quotes:
    #extract all fields (quote text, author, tags)
    text = q.find("span", class_="text").get_text()
    author = q.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]

    #Part 2.2: Regex cleaning to remove quotation marks
    text = re.sub(r"['']", "", text)

    #Part 3: Clean data
    text = text.strip()
    author = author.strip()
    tags= [t.strip() for t in tags if t.strip() != ""] #clean and join tags into a single string

    #store clean data in dictionary
    quotes_data.append({
        "quote": text,
        "author": author,
        "tags": ", ".join(tags)
    })

#Part 4.1: Save CSV
with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    writer.writerows(quotes_data)
    print("📊Data saved as CSV file sucessfully!")

#Part 4.2: Save JSON
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(quotes_data, file, indent=4, ensure_ascii=False)
    print("📁Data saved as JSON file successfully!")

#Part 5: Summary Report
#total number of quotes
num_quotes = len(quotes_data)

#extract authors and tags
authors = [q["author"] for q in quotes_data]
tags_list = []

for q in quotes_data:
    tags_list.extend(q["tags"].split(", "))

#Remove empty tags
tags_list = [t for t in tags_list if t]

#count occurrences
author_count = Counter(authors)
tag_count = Counter(tags_list)

#most common values
most_common_author = author_count.most_common(1)[0][0]
most_common_tag = tag_count.most_common(1)[0][0] if tag_count else "None"

#unique counts
unique_authors = len(set(authors))
unique_tags = len(set(tags_list))

#average quote length
quote_lengths = [len(q["quote"]) for q in quotes_data]
avg_length = sum(quote_lengths) / num_quotes if num_quotes > 0 else 0

#print summary
print("\n***** SUMMARY REPORT *****")
print("=============")
print(f"Total quotes scraped: {num_quotes}")
print(f"Most common author: {most_common_author}")
print(f"Most common tag: {most_common_tag}")
print(f"Unique authors: {unique_authors}")
print(f"Unique tags: {unique_tags}")
print(f"Average quote length: {avg_length:.2f}")
print("\n ✅Scraping complete!")