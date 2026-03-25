class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self) -> str:
        return f"{self.name} ({round(self.height, 1)}cm, {self.age} days)"


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
    print("")
    print(f"Total plants created: {count}")
