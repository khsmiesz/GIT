print("Biblioteka filmów")
class Movies:
    def __init__(self, title, year, genre, played=0):
        self.title=title
        self.year=year
        self.genre=genre
        self.played=0
    def play(self, step=1):
        self.played+=step
    def __str__(self):
        return f"{self.title} {self.year}"
    
class Series(Movies):
    def __init__(self, episode_nr, season_nr, title, year, genre, played=0):
        super().__init__(title, year, genre, played)
        self.episode_nr=episode_nr
        self.season_nr=season_nr
    def __str__(self):
        return f"{self.title} S{self.season_nr}E{self.episode_nr}"
    

m1=Movies("Titanic", "1997", "Drama")
m2=Movies("Avatar", "2009", "SciFi")
m3=Movies("A Beautiful Mind", "2001", "Drama")
m4=Movies("Rain Man", "1988", "Drama")
m5=Movies("Sound of Metal", "2019", "Musical")
s1=Series("01", "01", "BoJack Horseman", "2017", "comedy")
s2=Series("02", "03", "The Office", "2008", "comedy")

Library=[]
Library.append(m1)
Library.append(m2)
Library.append(m3)
Library.append(m4)
Library.append(m5)
Library.append(s1)
Library.append(s2)
 

print(m3.played)
m3.play()
print(m3.played)
print(s2)

def get_movies():
    
    movies_list=[]
    for title in Library:
        if isinstance(title, Movies):
            movies_list.append(title)
    sorted(movies_list)
    print(movies_list)

def search():
    searched_title=input("Podaj szukany tytuł:")
    for i in Library:
        if title==searched_title:
            print(i) 
        else:
            pass

get_movies()
            
    