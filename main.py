import requests
from bs4 import BeautifulSoup
import pprint
from datetime import date


today = date.today()
day_text = today.strftime("%B %d, %Y")
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')  # convert the txt into parseable object
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories(news):
    return sorted(news, key = lambda k:k['votes'], reverse = True)  # sorts the news according to the highest votes


def custom_hackernews(links, subtext):
    print(f'\t\t Date: {day_text}')
    print()
    print('\t***Custom Top Stories From Hacker News***')
    print()
    news = []
    for index, _ in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))  # gets the votes from the link and turns it into int
            if points > 99:
                news.append({'title': title, 'link':href, 'votes': points})
    return sort_stories(news)


pprint.pprint(custom_hackernews(links, subtext))