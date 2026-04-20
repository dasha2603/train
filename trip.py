class Trip:
    """
    Класс, представляющий поездку.

    Атрибуты:
        route_number (int): Номер маршрута
        full_name (str): ФИО пассажира
        route (list): Маршрут поездки [отправление, назначение]
        travel_time (int): Время поездки (в минутах)
        travel_cost (float): Стоимость поездки
    """

    def __init__(self, route_number, full_name, route, travel_time, travel_cost):
        self.route_number = route_number
        self.full_name = full_name
        self.route = route
        self.travel_time = travel_time
        self.travel_cost = travel_cost

    @staticmethod
    def can_travel(passenger, train, departure, arrival):
        """
        Проверяет, возможна ли поездка:
        - маршрут подходит
        - хватает денег (деньги + бонусы)
        """
        time = train.get_travel_time(departure, arrival)
        cost = train.get_ticket_price(departure, arrival)

        if time >= 1000 or cost >= 1000:
            return False, time, cost

        if passenger.total_funds() < cost:
            return False, time, cost

        return True, time, cost

    def __str__(self):
        return (f"Поездка:\n"
                f"  Маршрут №{self.route_number}\n"
                f"  Пассажир: {self.full_name}\n"
                f"  Путь: {self.route[0]} → {self.route[1]}\n"
                f"  Время: {self.travel_time} мин\n"
                f"  Стоимость: {self.travel_cost:.2f} руб.")