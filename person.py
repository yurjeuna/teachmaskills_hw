from _datetime import datetime
class Passport:
    def __init__(self, id, date_of_issue: datetime, dep_of_issue):
        self.id = id
        self.date_of_issue = date_of_issue
        self.dep_of_issue = dep_of_issue

class Car:
    def __init__(self, mark, color, max_speed: int, cost):
        self.mark = mark
        self.color = color
        self.max_speed = max_speed
        self.cost = cost

class Work:
    def __init__(self, company):
        self.company = company

class Person(Passport, Car, Work):
    def __init__(self, name: str, surname: str, date_of_birth: datetime, sex, money: int, father=None, mother=None):
        self.name = name
        self.surname = surname
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        self.sex = sex
        self.money = money
        self.father = father
        self.mother = mother

    @property
    def age(self):
        age = datetime.today() - self.date_of_birth
        return age.days // 365

    @property
    def full_name(self):
        return f'{self.surname} {self.name}'

    def after14(self, *args):
        if self.age >= 14:
            self.passport = Passport(*args)

    def after18(self, *args):
        if self.age >= 18:
            self.work = Work(*args)
            self.position = Position(*args)

    def earn_money(self, position, money):
        now = datetime.today()
        if now.day == 10:
            self.money += self.position.salary
        return self.money

    def buy_a_car(self, age, money, *args):
        if self.age >= 18 and self.money >= Car.cost:
            self.money -= Car.cost
            self.car = Car(*args)

    def make_a_baby(self, age, sex, another_person, *args):
        if self.age >= 18 and another_person.age >= 18:
            if self.sex != another_person.sex:
                baby_name = input("Now you're a parent! How to name a child?")
                baby_sex = input("Is it boy or girl? (male / female")
                baby_money = 0
                if self.sex == 'male':
                    baby_surname = self.surname
                    baby_father = self
                    baby_mother = another_person
                else:
                    baby_surname = another_person.surname
                    baby_father = another_person
                    baby_mother = self
                self.baby = Person(self, baby_name, baby_surname, datetime.today(), baby_sex, baby_money,  baby_father, baby_mother)


class Position():
    def __init__(self, name_of_position, salary):
        self.name_of_position = name_of_position
        self.salary = salary



