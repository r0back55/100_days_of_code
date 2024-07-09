from bs4 import BeautifulSoup


with open(file="./website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")  # we might need lxml parser instead
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))


heading = soup.find_all(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)


company_url_id = soup.select_one(selector="#name")
print(company_url_id)

headings = soup.select(".heading")
print(headings)
