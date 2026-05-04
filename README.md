## QUOTES SCRAPER PROJECT

## OVERVIEW
This project is a Python web scraper that extracts quotes, authors, and tags from:
https://quotes.toscrape.com

The data is cleaned, structured, and exported into CSV and JSON formats, along with a summary report.

---

## FEATURES
- Fetches webpage data using `requests`
- Parses HTML using `BeautifulSoup`
- Extracts:
  - Quote text
  - Author
  - Tags
- Cleans data using regex and string methods
- Saves data to:
  - CSV file
  - JSON file
- Generates summary insights:
  - Total quotes
  - Most common author
  - Most common tag
  - Unique counts
  - Average quote length

---

##  TECHNOLOGIES USED
- Python
- Requests
- BeautifulSoup
- Pandas
- JSON

---

## HOW TO RUN IT

1. Clone the repository:
```bash
git clone https://github.com/kaziahmolefe/quotes-scraper-project.git
