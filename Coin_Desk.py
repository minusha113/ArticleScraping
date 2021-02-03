# Import the libraries
import nltk
import newspaper
import csv

# Get the link to scrape articles from
coin_desk = newspaper.build('https://www.coindesk.com/', memoize_articles=False)

urls = {}

# Creating a csv file to save urls of the articles
csv_file = open('coindesk_urls.csv', 'a')

# Get all the article urls in the list 'urls' and write in csv file created
for article in coin_desk.articles:
    urls[article.url] = False

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([article.url])

print(urls)

# Get the categories
for category in coin_desk.category_urls():
    print(category)

# Create another csv files for storing the scraped info
csv_file = open('coindesk_scrape.csv', 'a')

for article in coin_desk.articles:
    if not urls[article.url]:

        # Do some NLP (Natural Language Processes)
        coin_article = article
        coin_article.download()
        coin_article.parse()
        nltk.download('punkt')
        coin_article.nlp()

        # Get the details of articles, such as text, summary, etc.
        print(coin_article.authors)

        print(coin_article.publish_date)

        print(coin_article.top_image)

        print(coin_article.text)

        print(coin_article.keywords)

        print(coin_article.summary)

        urls[article.url] = True

        # Write all the scraped details into the csv file
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([coin_article.authors, coin_article.publish_date, coin_article.top_image, coin_article.text, coin_article.keywords, coin_article.summary])