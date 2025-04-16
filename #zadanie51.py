#zadanie5.1
class BusinessCard:
    def __init__(self, name, surname, company, position, email):
        self.name=name
        self.surname=surname
        self.company=company
        self.position=position
        self.email=email
       
card1=BusinessCard(name="Brygida", surname="Sobczak", company="The Independent Planners", position="Education and training manager", email="BrygidaSobczak@armyspy.com")
card2=BusinessCard(name="Zofia", surname="Adamska", company="Channel Home Centers", position="Educator", email="ZofiaAdamska@armyspy.com")
card3=BusinessCard(name="Aleksy", surname="Król", company="Deco Refreshments", position="Clerk", email="AleksyKrol@rhyta.com")
card4=BusinessCard(name="Wiktor", surname="Wojciechowski", company="Infinite Wealth Planners", position="Operator", email="WiktorWojciechowski@jourrapide.com")
card5=BusinessCard(name="Bogumił", surname="Kwiatkowski", company="Red Fox Tavern", position="Woodworker", email="BogumilKwiatkowski@teleworm.us")

print(card1)
print(card1.surname)



   