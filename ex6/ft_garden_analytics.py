class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def __str__(self) -> str:
        blooming_status = "blooming" if self.is_blooming else "not blooming"
        outp = f"{self.name}: {self.height}cm, "
        outp += f"{self.color} flowers ({blooming_status})"
        return f"{outp}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def award_points(self, points: int) -> None:
        self.prize_points += points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0

        def record_plant_added(self, plant) -> None:
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def record_growth(self) -> None:
            self.total_growth += 1

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: object) -> None:
        self.plants.append(plant)
        self.stats.record_plant_added(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def calculate_score(self) -> int:
        total = 0
        for plant in self.plants:
            total += plant.height
            if isinstance(plant, FloweringPlant) and plant.is_blooming:
                total += 10
            if isinstance(plant, PrizeFlower):
                total += plant.prize_points * 2
        return total

    def show_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        print("")
        print(f"Plants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.regular_plants} regular, "
              f"{self.stats.flowering_plants} flowering, "
              f"{self.stats.prize_flowers} prize flowers")
        print("")

    @classmethod
    def show_total_gardens(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")

    alice_garden = GardenManager("Alice")
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    print("")

    rose.bloom()
    sunflower.bloom()
    alice_garden.grow_all()
    print("")
    alice_garden.show_report()

    print(f"Height validation test: {GardenManager.validate_height(100)}")

    bob_garden = GardenManager("Bob")
    pine = Plant("Pine", 80)
    tulip = FloweringPlant("Tulip", 12, "pink")
    bob_garden.add_plant(pine)
    bob_garden.add_plant(tulip)

    alice_score = alice_garden.calculate_score()
    bob_score = bob_garden.calculate_score()
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    GardenManager.show_total_gardens()
