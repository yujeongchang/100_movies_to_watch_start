import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")
movie_tags = soup.find_all(name="h3", class_="title")

# list 순서 거꾸로 정렬 (.reverse() 이용)
# list = []
# for movie in movie_tags:
#     movie_string = movie.getText()
#     list.append(movie_string)

title_list = [movie.getText() for movie in movie_tags]
title_list.reverse()
# txt 파일 작성하기 (for loop 안에서 작성하자)
for movie in title_list:
    with open(file="./100films.txt", mode="a") as file:
        file.write(f"{movie}\n")