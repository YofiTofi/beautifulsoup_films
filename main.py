from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
film_href_tags = soup.find_all(name="a")
films = reversed([film_href.text.split("Read Empire's review of ")[1] for film_href in film_href_tags if film_href.text.__contains__("Read Empire's review of")])
out_text = ""
for idx, film in enumerate(films):
    out_text += f"{idx + 1}. {film}\n"
with open("films.txt", "w", encoding="utf-8") as file:
    file.write(out_text)