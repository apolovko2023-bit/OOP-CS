from abc import ABC, abstractmethod

from google.adk.agents import Agent


# =========================
# Абстрактний клас
# =========================

class Transport(ABC):

    def __init__(
        self,
        route_number: str,
        departure: str
    ):
        self.route_number = route_number
        self.departure = departure

    @abstractmethod
    def get_schedule(self) -> dict:
        pass


# =========================
# Bus
# =========================

class Bus(Transport):

    def __init__(
        self,
        route_number: str,
        departure: str,
        stops: list[str]
    ):
        super().__init__(route_number, departure)

        self.stops = stops

    def get_schedule(self) -> dict:
        return {
            "type": "Bus",
            "route_number": self.route_number,
            "departure": self.departure,
            "stops": self.stops
        }


# =========================
# Train
# =========================

class Train(Transport):

    def __init__(
        self,
        route_number: str,
        departure: str,
        stations: list[str],
        travel_time_min: int
    ):
        super().__init__(route_number, departure)

        self.stations = stations
        self.travel_time_min = travel_time_min

    def get_schedule(self) -> dict:
        return {
            "type": "Train",
            "route_number": self.route_number,
            "departure": self.departure,
            "stations": self.stations,
            "travel_time_min": self.travel_time_min
        }


# =========================
# Schedule
# =========================

class Schedule:

    def __init__(self):

        # Інкапсуляція
        self.__routes: dict[str, Transport] = {}

    def add_route(
        self,
        transport: Transport
    ):

        self.__routes[
            transport.route_number
        ] = transport

    def find_route(
        self,
        route_number: str
    ):

        return self.__routes.get(route_number)

    def list_routes(self):

        # Поліморфізм
        return [
            route.get_schedule()
            for route in self.__routes.values()
        ]


# =========================
# TOOL
# =========================

def get_transport_schedule(
    route_number: str
) -> dict:

    schedule = Schedule()

    # Автобуси
    bus1 = Bus(
        "24A",
        "08:30",
        [
            "Центр",
            "Вокзал",
            "Автовокзал"
        ]
    )

    bus2 = Bus(
        "15B",
        "09:15",
        [
            "Сихів",
            "Університет",
            "Ринок"
        ]
    )

    # Потяги
    train1 = Train(
        "T101",
        "07:00",
        [
            "Львів",
            "Тернопіль",
            "Київ"
        ],
        320
    )

    train2 = Train(
        "T205",
        "13:40",
        [
            "Львів",
            "Стрий",
            "Ужгород"
        ],
        180
    )

    # Додаємо маршрути
    schedule.add_route(bus1)
    schedule.add_route(bus2)

    schedule.add_route(train1)
    schedule.add_route(train2)

    # Пошук маршруту
    route = schedule.find_route(route_number)

    if route:
        return route.get_schedule()

    return {
        "found": False
    }


# =========================
# AI AGENT
# =========================

root_agent = Agent(

    name="transport_agent",

    model="gemini-2.5-flash",

    description="""
    Агент громадського транспорту
    """,

    instruction="""
    Ти є помічником
    з громадського транспорту.

    Надавай інформацію
    про маршрути,
    зупинки
    та час у дорозі.

    Відповідай
    українською мовою.
    """,

    tools=[
        get_transport_schedule
    ]
)

