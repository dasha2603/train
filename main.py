from passenger import Passenger
from train import Train
from trip import Trip


def create_trains():
    """Создаёт массив из 5 электричек."""
    return [
        Train(101, 0, ["Москва", "Тверь", "Бологое", "Санкт-Петербург"],
              [90, 60, 120], [0, 500, 800, 1200]),
        Train(102, 0, ["Москва", "Владимир", "Нижний Новгород"],
              [120, 150], [0, 600, 1100]),
        Train(103, 0, ["Москва", "Калуга", "Брянск"],
              [150, 120], [0, 550, 1000]),
        Train(104, 0, ["Санкт-Петербург", "Новгород", "Москва"],
              [180, 210], [0, 700, 1300]),
        Train(105, 0, ["Москва", "Рязань", "Тамбов"],
              [180, 200], [0, 650, 1150])
    ]


def main():
    print("=== СИСТЕМА ПОКУПКИ БИЛЕТОВ НА ЭЛЕКТРИЧКУ ===\n")

    print("Введите данные пассажира:")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    money = float(input("Бюджет (руб.): "))
    departure = input("Станция отправления: ")
    arrival = input("Станция назначения: ")

    passenger = Passenger(name, surname, patronymic, money, departure, arrival)
    print(f"\nБонусные баллы: {passenger.bonus_points}")
    print(f"Доступно средств (деньги + бонусы): {passenger.total_funds()} руб.")

    trains = create_trains()
    best_train = None
    best_time = float('inf')
    best_cost = 0

    for train in trains:
        possible, time, cost = Trip.can_travel(passenger, train, departure, arrival)
        if possible and time < best_time:
            best_time = time
            best_cost = cost
            best_train = train

    if best_train:
        print(f"\n Найдена подходящая электричка!")
        print(f"   Маршрут №{best_train.route_number}")
        print(f"   Время в пути: {best_time} минут")
        print(f"   Стоимость билета: {best_cost} руб.")

        if passenger.money >= best_cost:
            passenger.money -= best_cost
        else:
            total = passenger.money + passenger.bonus_points
            passenger.money = 0
            passenger.bonus_points = total - best_cost

        print(f"\nОстаток на счете: {passenger.money:.2f} руб.")
        print(f"Остаток бонусов: {passenger.bonus_points}")

        trip = Trip(best_train.route_number,
                    f"{surname} {name} {patronymic}",
                    [departure, arrival],
                    best_time,
                    best_cost)

        print("\n=== ДЕТАЛИ ПОЕЗДКИ ===")
        print(trip)

    else:
        print("\n Подходящая электричка не найдена.")
        print("Возможные причины:")
        print("- Нет рейса с указанными станциями")
        print("- Не хватает денег (даже с бонусами)")
        print("- Станция отправления находится позже станции назначения")


if __name__ == "__main__":
    main()