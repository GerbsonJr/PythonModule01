class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        h = round(self.height / self.age, 1)
        if h == 0:
            h = 0.1
        self.height += h

    def agee(self) -> None:
        self.age += 1

    def update(self) -> None:
        self.grow()
        self.agee()

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    day = 2
    print("=== Day 1 ===")
    print(rose.show())
    while day < 8:
        print(f"=== Day {day} ===")
        rose.update()
        print(rose.show())
        day += 1
    growth = rose.height - initial_height
    print(f"Growth this week: +{round(growth, 1)}cm")
