#zadanie5.2
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
    def name_len(self): 
        length=len(self.name)+len(self.surname)+1
        return length
card1=BusinessCard(name="Brygida", surname="Sobczak", company="The Independent Planners", position="Education and training manager", email="BrygidaSobczak@armyspy.com")
card2=BusinessCard(name="Zofia", surname="Adamska", company="Channel Home Centers", position="Educator", email="ZofiaAdamska@armyspy.com")
card3=BusinessCard(name="Aleksy", surname="Król", company="Deco Refreshments", position="Clerk", email="AleksyKrol@rhyta.com")
card4=BusinessCard(name="Wiktor", surname="Wojciechowski", company="Infinite Wealth Planners", position="Operator", email="WiktorWojciechowski@jourrapide.com")
card5=BusinessCard(name="Bogumił", surname="Kwiatkowski", company="Red Fox Tavern", position="Woodworker", email="BogumilKwiatkowski@teleworm.us")

print(card1)

cards=[card1, card2, card3, card4, card5]
by_name=sorted(cards, key=lambda BusinessCard: BusinessCard.name)
for card in by_name:
    print(card)

by_surname=sorted(cards, key=lambda BusinessCard: BusinessCard.surname)
for card in by_surname:
    print(card)

print(card1.contact())

print(card2.name_len)

class BaseContact(BusinessCard):
    def __init__(self, name, surname, email):
        super().__init__(name, surname, company, position, email)
        
class BusinessContact(BusinessCard):
    def __init__(self, name, surname, company, position, email):
        super().__init__(name, surname, company, position, email)
print(card1.contact)