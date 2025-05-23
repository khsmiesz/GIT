#zadanie5.2

from faker import Faker
fake = Faker('pl_PL')

#Klasa podstawowa

class BusinessCard:
    def __init__(self, name, surname, company, position, email):
        self.name=name
        self.surname=surname
        self.company=company
        self.position=position
        self.email=email

    def __str__(self):
        return f'{self.name} {self.surname} {self.position}'
    def contact(self):
        return f'Kontaktuję się z {self.name} {self.surname} adres e-mail: {self.email}'
    
    @property
    def label_length(self): 
        length=len(self.name)+len(self.surname)+1
        return length
    
card1=BusinessCard(name="Brygida", surname="Sobczak", company="The Independent Planners", position="Education and training manager", email="BrygidaSobczak@armyspy.com")
card2=BusinessCard(name="Zofia", surname="Adamska", company="Channel Home Centers", position="Educator", email="ZofiaAdamska@armyspy.com")
card3=BusinessCard(name="Aleksy", surname="Król", company="Deco Refreshments", position="Clerk", email="AleksyKrol@rhyta.com")
card4=BusinessCard(name="Wiktor", surname="Wojciechowski", company="Infinite Wealth Planners", position="Operator", email="WiktorWojciechowski@jourrapide.com")
card5=BusinessCard(name="Bogumił", surname="Kwiatkowski", company="Red Fox Tavern", position="Woodworker", email="BogumilKwiatkowski@teleworm.us")

#drukuję wizytówkę
print(card1)

#sortuję
cards=[card1, card2, card3, card4, card5]
by_name=sorted(cards, key=lambda BusinessCard: BusinessCard.name)
for card in by_name:
    print(card)

by_surname=sorted(cards, key=lambda BusinessCard: BusinessCard.surname)
for card in by_surname:
    print(card)

#używam funkcji klasy
print(card1.contact())

print(card2.label_length)

#podklasa1

class BaseContact(BusinessCard):
    def __init__(self, phone_number, name, surname, company, position, email):
        super().__init__(name, surname, company, position, email)
        self.phone=phone_number

    def create_contacts(how_many):
        contacts=[]
        for i in range(how_many):
            full_name = fake.name().split()
            name = full_name[0]
            surname = full_name[-1]
            onecontact = BaseContact(
            phone_number=fake.phone_number(),
            name=name,
            surname=surname,
            company=fake.company(),
            position=fake.job(),
            email=fake.email()
            )
            contacts.append(onecontact)
        return contacts
    

    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}.'

#*jezujaksięnamęczyłamzfakerem* tworzę wizytówki
FakeList = BaseContact.create_contacts(3)
for person in FakeList:
    print(person)

#korzystam z funkcji obu klas
print(BaseContact.contact(FakeList[1]))
print(FakeList[0].label_length)

#podklasa2
       
class BusinessContact(BusinessCard):
    def __init__(self, work_phone, name, surname, company, position, email):
        super().__init__(name, surname, company, position, email)
        self.work_phone=work_phone

    def create_contacts2(how_many):
        contacts2=[]
        for i in range(how_many):
            full_name = fake.name().split()
            name = full_name[0]
            surname = full_name[-1]
            onecontact = BusinessContact(
            work_phone=fake.phone_number(),
            name=name,
            surname=surname,
            company=fake.company(),
            position=fake.job(),
            email=fake.email()
            )
            contacts2.append(onecontact)
        return contacts2
    
    def contact(self):
        return f'Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}'
    
FakeList2=BusinessContact.create_contacts2(88)

print(BusinessContact.contact(FakeList2[44]))

        
