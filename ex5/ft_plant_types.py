class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        pass


class Flower(Plant):
    def __init__(self, name, height, age, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")

    def __str__(self) -> str:
        outp = f"{self.name.capitalize()} (Flower): "
        outp += f"{self.height}cm, {self.age} days, {self.color} color"
        return f"{outp}"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade: int) -> None:
        outp = f"{self.name.capitalize()} provides "
        outp += f"{shade} square meters of shade"
        print(f"{outp}")

    def __str__(self) -> str:
        outp = f"{self.name.capitalize()} (Tree): "
        outp += f"{self.height}cm, {self.age} days, "
        outp += f"{self.trunk_diameter}cm diameter"
        return f"{outp}"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest: str, nutri: str) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutri = nutri

    def __str__(self) -> str:
        outp = f"{self.name.capitalize()} (Vegetable): "
        outp += f"{self.height}cm, {self.age} days, "
        outp += f"{self.harvest} harvest\n"
        outp += f"{self.name.capitalize()} is rich in {self.nutri}"
        return f"{outp}"


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    print("=== Garden Plant Types ===")
    print("")
    print(rose)
    rose.bloom()
    print("")
    print(oak)
    oak.produce_shade(78)
    print("")
    print(tomato)
