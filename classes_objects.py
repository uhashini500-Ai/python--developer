# Define the Avenger class[span_2](start_span)[span_2](end_span)
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, is_team_leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.is_team_leader = is_team_leader

    # Method to get information about each superhero[span_3](start_span)[span_3](end_span)
    def get_info(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Super Power: {self.super_power}\n"
            f"Weapon: {self.weapon}\n"
            f"Leader Status: {'Leader' if self.is_leader() else 'Not Leader'}"
        )

    # Method to tell if the superhero is a leader or not[span_4](start_span)[span_4](end_span)
    def is_leader(self):
        return self.is_team_leader


# Create the six superheroes using the Avenger class[span_5](start_span)[span_5](end_span)
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super strength", "Shield", is_team_leader=True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 45, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 40, "Male", "Fighting skills", "Bow and Arrows")
]

# Display information for each superhero
for hero in super_heroes:
    print("----------------------------------------")
    print(hero.get_info())
print("----------------------------------------")