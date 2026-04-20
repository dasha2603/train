import random

class Passenger:
    """
    Класс, представляющий пассажира.

    Атрибуты:
        name (str): Имя
        surname (str): Фамилия
        patronymic (str): Отчество
        money (float): Количество денежных средств на счёте
        bonus_points (int): Количество бонусных баллов (0–100)
        departure_station (str): Остановка отправления
        arrival_station (str): Остановка назначения
    """

    def __init__(self, name, surname, patronymic, money, departure_station, arrival_station):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.money = money
        self.bonus_points = random.randint(0, 100)
        self.departure_station = departure_station
        self.arrival_station = arrival_station

    def total_funds(self):
        """Возвращает деньги + бонусы."""
        return self.money + self.bonus_points

    def __str__(self):
        return (f"Пассажир: {self.surname} {self.name} {self.patronymic}\n"
                f"Денег: {self.money:.2f} руб.\n"
                f"Бонусов: {self.bonus_points}\n"
                f"Маршрут: {self.departure_station} → {self.arrival_station}")