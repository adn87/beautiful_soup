from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", rel="noreferrer")
article_text = []
article_link = []
for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(article_text)
# print(article_link)
# print(article_score)
highest_number = max(article_score)
index_num = article_score.index(highest_number)
print(article_text[index_num])
print(article_link[index_num])





# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title.name)
# # print(soup)
#
# # print(soup.prettify())
#
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)