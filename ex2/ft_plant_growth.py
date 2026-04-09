class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self) -> None:
        h = round(self.height / self.plant_age, 1)
        if h == 0:
            h = 0.1
        self.height += h

    def age(self) -> None:
        self.plant_age += 1

    def update(self) -> None:
        self.grow()
        self.age()

    def show(self) -> str:
        return (
            f"{self.name}: {round(self.height, 1)}cm,"
            f" {self.plant_age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    day = 1
    print(rose.show())
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.update()
        print(rose.show())
        day += 1
    growth = rose.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")
