#zadanie4.4
import logging
def kalkulator():
    działanie=input("Podaj działanie, którego oczekujesz, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    if działanie=="1":
        składnik1=input("Podaj pierwszy składnik:")
        składnik2=input("Podaj drugi składnik:")
        suma=float(składnik1)+float(składnik2)
        print(f"Dodaję {składnik1} i {składnik2} \nWynik to {suma}")
    if działanie=="2":
        odjemna=input("Podaj odjemną:")
        odjemnik=input("Podaj odjemnik:")
        różnica=float(odjemna)-float(odjemnik)
        logging(f"Odejmuję {odjemnik} od {odjemna} \nWynik to {różnica}")
    if działanie=="3":
        czynnik1=input("Podaj pierwszy czynnik:")
        czynnik2=input("Podaj drugi czynnik:")
        iloczyn=float(czynnik1)*float(czynnik2)
        print(f"Mnożę {czynnik1} przez {czynnik2} \nWynik to {iloczyn}")
    if działanie=="4":
        dzielna=input("Podaj dzielną:")
        dzielnik=input("Podaj dzielnik:")
        if dzielnik=="0":
            print("Nie można dzielić przez zero")
            good_dzielnik=input("Podaj prawidłowy dzielnik:")
            iloraz=float(dzielna)/float(good_dzielnik)
            print(f"Dzielę {dzielna} przez {good_dzielnik} \nWynik to {iloraz}")
        else:
            iloraz=float(dzielna)/float(dzielnik)
            print(f"Dzielę {dzielna} przez {dzielnik} \nWynik to {iloraz}")


kalkulator()


