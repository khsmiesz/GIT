import logging
def greetings_by_name(imię_i_nazwisko):
    greetings = "Witaj %s" %imię_i_nazwisko
    logging.warning(imię_i_nazwisko)
    return greetings
if __name__ == "__main__":
    dane=input("Podaj proszę swoje imię i nazwisko")
    pytanie=greetings_by_name(dane)
    print(pytanie)

