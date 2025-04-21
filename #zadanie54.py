#zadanie5.4
import random
import datetime

class Videos:
    def __init__(self, title, year, genre, played):
        self.title=title
        self.year=year
        self.genre=genre
        self.played=played

    def play(self, step=1):
        self.played+=step

class Movies(Videos):
    def __init__(self, title, year, genre, played):
        super().__init__(title, year, genre, played)
    def __str__(self):
        return f"{self.title} {self.year}"
    
class Series(Videos):
    def __init__(self, episode_nr, season_nr, title, year, genre, played):
        super().__init__(title, year, genre, played)
        self.episode_nr=episode_nr
        self.season_nr=season_nr    
    def __str__(self):
        return f"{self.title} S{self.season_nr}E{self.episode_nr}"
    

m1=Movies("Titanic", "1997", "Drama", 0)
m2=Movies("Avatar", "2009", "SciFi", 0)
m3=Movies("A Beautiful Mind", "2001", "Drama", 0)
m4=Movies("Rain Man", "1988", "Drama", 0)
m5=Movies("Sound of Metal", "2019", "Musical", 0)
s1=Series("01", "01", "BoJack Horseman", "2017", "comedy", 0)
s2=Series("02", "03", "The Office", "2008", "comedy", 0)

Library=[]
Library.append(m1)
Library.append(m2)
Library.append(m3)
Library.append(m4)
Library.append(m5)
Library.append(s1)
Library.append(s2)
 

def get_movies():
    movies_list=[]
    for title in Library:
        if isinstance(title, Movies):
            movies_list.append(title)
    for movie in movies_list:
        print(movie)

def get_series():
    series_list=[]
    for title in Library:
        if isinstance(title, Series):
            series_list.append(title)
    for serie in series_list:
        print(serie)

def generate_views():
    views=[x for x in range(1,101)]
    random_movie=random.choice(Library)
    random_number=random.choice(views)
    random_movie.played += random_number
    return print (f'{random_movie.title} Ilość odtworzeń: {random_movie.played}')

def TenGenerate():
    for i in range(10):
        generate_views()

def search(tytuł):
    for movie in Library:
        if tytuł==movie.title:
            print(movie)

def top_titles(n):
    by_views=sorted(Library, key=lambda movie: movie.played, reverse=True)
    top_n=by_views[:n]
    for movie in top_n:
        print(movie)
    return top_n


        
print("Biblioteka filmów")
TenGenerate()
top_3=top_titles(3)
top_3_str=[str(movie) for movie in top_3]
print(f'Trzy filmy z największą liczbą wyświetleń to {top_3_str}.')
search("Avatar")
data=datetime.date.today()
print(f'Najpopularniejsze filmy i seriale dnia {data.strftime("%d.%m.%Y")} to: {top_3}')