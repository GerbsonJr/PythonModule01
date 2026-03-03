class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def agee(self) -> None:
        self.age += 1

    def update(self) -> None:
        self.grow()
        self.agee()

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Day 1 ===")
    print(rose.get_info())
    day = 1
    while day < 7:
        rose.update()
        day += 1
    print("=== Day 7 ===")
    print(rose.get_info())
    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")
