class Train:
    """
    Класс, представляющий электричку.

    Атрибуты:
        route_number (int): Номер маршрута
        ticket_price (float): Стоимость билета
        route_stations (list): Список станций по порядку
        travel_times (list): Время между станциями (в минутах)
        station_prices (list): Стоимость до каждой станции от начальной
    """

    def __init__(self, route_number, ticket_price, route_stations, travel_times, station_prices):
        self.route_number = route_number
        self.ticket_price = ticket_price
        self.route_stations = route_stations
        self.travel_times = travel_times
        self.station_prices = station_prices

    def get_travel_time(self, departure, arrival):
        """Возвращает время в пути (минуты) или 1000, если станции нет или порядок неверный."""
        if departure not in self.route_stations or arrival not in self.route_stations:
            return 1000

        idx_dep = self.route_stations.index(departure)
        idx_arr = self.route_stations.index(arrival)

        if idx_arr <= idx_dep:
            return 1000

        time = 0
        for i in range(idx_dep, idx_arr):
            time += self.travel_times[i]
        return time

    def get_ticket_price(self, departure, arrival):
        """Возвращает стоимость билета или 1000, если станции нет или порядок неверный."""
        if departure not in self.route_stations or arrival not in self.route_stations:
            return 1000

        idx_dep = self.route_stations.index(departure)
        idx_arr = self.route_stations.index(arrival)

        if idx_arr <= idx_dep:
            return 1000

        return self.station_prices[idx_arr] - self.station_prices[idx_dep]

    def __str__(self):
        stations_str = " → ".join(self.route_stations)
        return (f"Маршрут №{self.route_number}: {stations_str}\n"
                f"Время между станциями: {self.travel_times}\n"
                f"Стоимость от начальной: {self.station_prices}")