import nltk
import newspaper
import csv

coin_telegraph = newspaper.build('https://cointelegraph.com/', memoize_articles=False)

urls = {}

csv_file = open('coinTele_urls.csv', 'w')
for article in coin_telegraph.articles:
    urls[article.url] = False

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([article.url])

print(urls)

for category in coin_telegraph.category_urls():
    print(category)

csv_file = open('coinTele_scrape.csv', 'w')
for article in coin_telegraph.articles:
    if not urls[article.url]:

        coin_article = article
        coin_article.download()
        coin_article.parse()
        nltk.download('punkt')
        coin_article.nlp()

        print(coin_article.authors)

        print(coin_article.publish_date)

        print(coin_article.top_image)

        print(coin_article.text)

        print(coin_article.keywords)

        print(coin_article.summary)

        urls[article.url] = True

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([coin_article.authors, coin_article.publish_date, coin_article.top_image, coin_article.text, coin_article.keywords, coin_article.summary])
