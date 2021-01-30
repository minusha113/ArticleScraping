import nltk
import newspaper
import csv

news_bitcoin = newspaper.build('https://news.bitcoin.com/', memoize_articles=False)

urls = {}

csv_file = open('NewsBit_urls.csv', 'w')
for article in news_bitcoin.articles:
    urls[article.url] = False

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([article.url])

print(urls)

for category in news_bitcoin.category_urls():
    print(category)

csv_file = open('NewsBit_scrape.csv', 'w')
for article in news_bitcoin.articles:
    if not urls[article.url]:

        newsbit_article = article
        newsbit_article.download()
        newsbit_article.parse()
        nltk.download('punkt')
        newsbit_article.nlp()

        print(newsbit_article.authors)

        print(newsbit_article.publish_date)

        print(newsbit_article.top_image)

        print(newsbit_article.text)

        print(newsbit_article.keywords)

        print(newsbit_article.summary)

        urls[article.url] = True

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([newsbit_article.publish_date, newsbit_article.top_image, newsbit_article.text, newsbit_article.keywords, newsbit_article.summary])
