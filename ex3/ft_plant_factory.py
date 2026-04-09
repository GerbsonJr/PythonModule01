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
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    plants = []
    count = 0
    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        count += 1
        print(f"Created: {plant.show()}")
