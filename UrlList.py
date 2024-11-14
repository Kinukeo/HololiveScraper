import csv

talent_to_url = []

def get_talents():
    with open('./HololiveYoutubeUrls.csv', encoding='UTF-8', newline='') as file:
        csvreader = csv.DictReader(file)

        next(csvreader, None)
        for row in csvreader:
            talent_to_url.append(row)

def get_talent_urls():
    urls = []
    for i in talent_to_url:
        urls.append(i["Url"])
    print(urls)

get_talents()
get_talent_urls()