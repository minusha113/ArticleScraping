# Import the libraries
import nltk
import newspaper
import csv

# Get the link to scrape articles from
news_bitcoin = newspaper.build('https://news.bitcoin.com/', memoize_articles=False)

urls = {}

# Creating a csv file to save urls of the articles
csv_file = open('NewsBit_urls.csv', 'a')

# Get all the article urls in the list 'urls' and write in csv file created
for article in news_bitcoin.articles:
    urls[article.url] = False

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([article.url])

print(urls)

# Get the categories
for category in news_bitcoin.category_urls():
    print(category)

# Create another csv files for storing the scraped info
csv_file = open('NewsBit_scrape.csv', 'a')

for article in news_bitcoin.articles:
    if not urls[article.url]:

        # Do some NLP (Natural Language Processes)
        newsbit_article = article
        newsbit_article.download()
        newsbit_article.parse()
        nltk.download('punkt')
        newsbit_article.nlp()

        # Get the details of articles, such as text, summary, etc.
        print(newsbit_article.authors)

        print(newsbit_article.publish_date)

        print(newsbit_article.top_image)

        print(newsbit_article.text)

        print(newsbit_article.keywords)

        print(newsbit_article.summary)

        urls[article.url] = True

        # Write all the scraped details into the csv file
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([newsbit_article.authors, newsbit_article.publish_date, newsbit_article.top_image, newsbit_article.text, newsbit_article.keywords, newsbit_article.summary])
