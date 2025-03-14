import csv

def get_talents():
    with open('./HololiveYoutubeUrls.csv', encoding='UTF-8', newline='') as file:
        csvreader = csv.DictReader(file)

        next(csvreader, None)
        talent_to_url = []
        for row in csvreader:
            talent_to_url.append(row)
        return talent_to_url
