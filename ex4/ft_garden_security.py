class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 15.0
        self._age = 10
        print(f"Plant created: {self}\n")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days\n")

    def __str__(self) -> str:
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 25, 30)
    rose.set_height(-5)
    rose.set_age(-5)
    print(f"\nCurrent state: {rose}")
