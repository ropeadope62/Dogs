foods = {"dry": {"kibble": 50, "cookies": 10}}


class Dog:
    def __init__(
        self,
        name: str,
        breed: str,
        color: str,
        age: int,
        weight: int,
        health=100,
        energy=100,
        happiness=75,
        anxiety=25,
        hunger=50,
        thirst=50,
        heartrate=60,
        b_bpm=30,
    ):
        # todo flesh out the bod and relationships mechanics
        self.bond = {"Name": 0}
        self.relationships = {"Dog": 0}

        self.commands = {
            "sit": {"progress": 0, "level": 0},
            "stay": {"progress": 0, "level": 0},
            "down": {"progress": 0, "level": 0},
            "come": {"progress": 0, "level": 0},
            "heel": {"progress": 0, "level": 0},
            "jump": {"progress": 0, "level": 0},
            "spin": {"progress": 0, "level": 0},
            "crawl": {"progress": 0, "level": 0},
            "hop": {"progress": 0, "level": 0},
            "speak": {"progress": 0, "level": 0},
            "whisper": {"progress": 0, "level": 0},
            "go": {"progress": 0, "level": 0},
            "fetch": {"progress": 0, "level": 0},
            "bang": {"progress": 0, "level": 0},
            "rollover": {"progress": 0, "level": 0},
            "scuba": {"progress": 0, "level": 0},
            "shoomshoom": {"progress": 0, "level": 0}
        }
        self.abilities = {
            "retrieving": {"progress": 0, "level": 0},
            "swimming": {"progress": 0, "level": 0},
            "sniffing": {"progress": 0, "level": 0},
            "tracking": {"progress": 0, "level": 0},
            "agility": {"progress": 0, "level": 0},
            "loose_leash_walking": {"progress": 0, "level": 0}
        }
        self.name = name
        self.state = "standing"
        self.breed = breed
        self.color = color
        self.age = age
        self.weight = weight
        self.anxiety = anxiety
        self.hunger = hunger
        self.thirst = thirst
        self.health = health
        self.energy = energy
        self.happiness = happiness
        self.mood = (
            "happy"
            if self.happiness >= 75
            else "content"
            if self.happiness >= 50
            else "sad"
            if self.happiness >= 25
            else "depressed"
        )
        self.learning_rate = 1
        self.heartrate = heartrate
        self.b_bpm = b_bpm
        self.toys = []

    def has_ability(self, ability, required_level=1):
        """
        Check if the dog has the required level of a given ability.

        :param ability: The ability to check.
        :param required_level: The required level of the ability to perform an action.
        :return: A tuple (can_perform: bool, message: str).
        """
        current_level = self.abilities.get(ability, {}).get("level", 0)
        if current_level < required_level:
            return (
                False,
                f"{self.name} is bad at {ability} (level {current_level}). Do some training!",
            )
        return True, f"{self.name}'s {ability} is at level {current_level}!"

    def knows_command(self, command, required_level=1):
        """
        Check if the dog knows a command at the required level.

        :param command: The command to check.
        :param required_level: The required level of the command for the dog to respond.
        :return: A tuple (can_perform: bool, message: str).
        """
        current_level = self.commands.get(command, {}).get("level", 0)
        if current_level < required_level:
            return (
                False,
                f"{self.name} does not know the command '{command}' well enough (level {current_level})!",
            )
        return True, f"{self.name}'s {command} is at level {current_level}!."

    def bark(self):
        barks = {
            10: "high pitched, yappy bark. Woof! Woof!",
            25: "high pitched bark. Woof! Woof!",
            50: "loud bark. Woof! Woof!",
            100: "loud, deep bark. Woof! Woof!",
            200: "low pitched, floor rumbling bark. Woof! Woof!",
        }
        for weight, bark in barks.items():
            if self.weight <= weight:
                print(f"{self.name} lets out a {bark}")
                break

    def fetch(self, item):
        if item not in self.toys:
            print(
                f"You don't have a {item} to throw for {self.name}! Get him one first"
            )
            return
        if self.energy <= 25:
            print(f"{self.name} is too tired to fetch the {item}!")
            return
        # Only decrement energy once
        self.energy = max(0, self.energy - 25)
        self.thirst = min(100, self.thirst + 25)
        self.hunger = min(100, self.hunger + 25)
        self.anxiety = max(0, self.anxiety - 25)

        retrieving_level = self.abilities["retrieving"]["level"]
        if retrieving_level == 0:
            print(f"{self.name} Takes the {item}, runs away and drops it somewhere!")
            self.abilities["retrieving"]["progress"] += 10
        elif retrieving_level == 1:
            print(
                f"{self.name} runs after the {item} and grabs it but doesn't bring it back! Oh no!"
            )
            self.abilities["retrieving"]["progress"] += 10
        elif retrieving_level == 2:
            print(f"{self.name} fetched the {item} but didn't bring it back!")
        else:  # assuming level 3 is the max level
            print(
                f"{self.name} fetched the {item} and drops it at your feet. What a good dog!"
            )

            if self.abilities["retrieving"]["level"] == 1:
                print(
                    f"{self.name} runs after the {item} and grabs it but doesn't bring it back! Oh no!"
                )
                self.energy = max(0, self.energy - 25)
                self.thirst = min(100, self.thirst + 25)
                self.hunger = min(100, self.hunger + 25)
                self.anxiety = max(0, self.anxiety - 25)
                self.abilities["retrieving"]["progress"] += 10
                return
            if self.abilities["retrieving"]["level"] == 2:
                print(f"{self.name} fetched the {item} but didn't bring it back!")
                return
            if self.abilities["retrieving"]["level"] == 3:
                print(
                    f"{self.name} fetched the {item} and drops it at your feet. What a good dog!"
                )
                self.energy = max(0, self.energy - 25)
                self.thirst = min(100, self.thirst + 25)
                self.hunger = min(100, self.hunger + 25)
                self.anxiety = max(0, self.anxiety - 25)

    def come(self):
        if self.commands["come"]["level"] == 0:
            print(f"You call to {self.name} and he looks at you with a blank stare!")
            return
        if self.commands["come"]["level"] == 1:
            print(f"{self.name} comes to you but doesn't sit!")
            return
        if self.commands["come"]["level"] == 2:
            print(f"{self.name} comes to you and sits!")
            return
        if self.commands["come"]["level"] == 3:
            print(f"{self.name} comes to you and sits perfectly!")
            return

    def train(self, ability):
        if ability not in self.abilities:
            print(f"{self.name} doesn't know how to {ability}! You start from scratch!")
            self.abilities[ability]["progress"] += 10
            return
        self.abilities[ability]["progress"] += 10
        print(f"{self.name} practiced {ability} and gained progress!")
        self.energy -= 20
        print(f"{self.name} spent some energy training!")
        self.happiness += 25
        print(f"{self.name} gained feels happier!")
        if self.abilities[ability]["progress"] >= 100:
            self.abilities[ability]["progress"] = 0
            self.abilities[ability]["level"] += 1
            print(
                f"{self.name} learned {ability}! He is now level {self.abilities[ability]['level']} at {ability}!"
            )
            return

    def eat(self, foodtype, food):
        if self.hunger == 0:
            print(f"{self.name} is not hungry!")
            return
        else:
            self.hunger -= foodtype[food]
            print(f"{self.name} ate the {food}!")

    def drink(self):
        if self.thirst <= 0:
            print(f"{self.name} is not thirsty!")
            return
        else:
            self.thirst -= 10
            print(f"{self.name} drank some water!")

    def nap(self):
        if self.energy >= 100:
            print(f"{self.name} is not tired!")
            return
        self.energy += 25
        print(f"{self.name} took a nap!")

    def sleep(self):
        if self.energy >= 100:
            print(f"{self.name} is not tired!")
            return
        self.energy += 75
        print(f"{self.name} had a great sleep!")

    def play(self, toy):
        if toy not in self.toys:
            print(f"{self.name} doesn't have a {toy}!")
            return
        self.happiness += 10
        self.energy -= 10
        print(f"{self.name} played with the {toy}!")

    def praise(self):
        self.happiness = min(100, self.happiness + 10)
        self.anxiety = max(0, self.anxiety - 10)
        print(f"{self.name} id encouraged by your praise!")
        print(f"{self.name}'s happiness increased!")
        print(f"{self.name}'s anxiety decreased!")

    def walk(self):
        can_walk, message = self.has_ability("loose_leash_walking")
        if not can_walk:
            print(f"{message}. You manage to get the walk done anyway.")
            self.anxiety -= 10
            self.energy = max(0, self.energy - 25)
            self.thirst += 50
            print(f"{self.name}'s walk completed! - Anxiety, -- Energy, ++ Thirst'")
            return
        if self.energy <= 25:
            print(f"{self.name} lays down and wont budge! He is too tired to walk!")
            return
        if self.abilities["loose_leash_walking"]["level"] == 1:
            print(f"{self.name} pulls a little bit but you get the walk done!")
            self.anxiety -= 25
            self.energy = max(0, self.energy - 25)
            self.happiness += 15
            self.thirst += 50
            print(
                f"{self.name}'s walk completed! - Anxiety, -- Energy, + Happiness, ++ Thirst'"
            )
            return
        if self.abilities["loose_leash_walking"]["level"] == 2:
            print(f"{self.name} walks almost perfectly on the leash!")
            self.anxiety -= 50
            self.energy = max(0, self.energy - 25)
            self.happiness += 20
            self.thirst += 50
            print(
                f"{self.name}'s walk completed! -- Anxiety, -- Energy, + Happiness, ++ Thirst'"
            )
            return
        if self.abilities["loose_leash_walking"]["level"] == 3:
            print(f"{self.name} walks perfectly on the leash!")
            self.anxiety -= 20
            self.energy = max(0, self.energy - 25)
            self.happiness += 25
            print(
                f"{self.name}'s walk completed! -- Anxiety, -- Energy, + Happiness, ++ Thirst'"
            )
            return
        if self.energy <= 50:
            print(
                f"{self.name} reluctantly goes for a walk, dragging on the leash the whole time!"
            )
            self.anxiety -= 10
            self.energy = max(0, self.energy - 25)
            print(
                f"{self.name}'s walk completed! -- Anxiety, -- Energy, + Happiness, ++ Thirst'"
            )
            return

        print(f"{self.name} went for a walk and spent some energy! Good dog!")

    def swim(self, ability="swimming"):
        can_swim, message = self.has_ability("swimming")
        print(message)
        if not can_swim:
            self.health -= 50
            return
        if self.energy <= 25:
            print(f"{self.name} is too tired to swim!")
            return
        if self.abilities[ability]["level"] >= 1:
            print(f"{self.name} went for a swim! Good dog!")
            self.energy -= 25
            self.hunger += 25
            self.thirst += 25
            self.anxiety -= 25
            self.happiness += 25
            return

    def teach(self, command: str):
        if self.is_tired(energy_required=20) is True:
            print(f"{self.name} is too tired to train!")
            return
        if command not in self.commands:
            print(f"{self.name} doesn't know that command!")
            return
        self.commands[command]["progress"] += 10
        print(f"{self.name} practiced {command} and gained progress!")
        self.energy -= 20
        print(f"{self.name} spent some energy training!")
        self.happiness += 5
        if self.commands[command]["progress"] >= 100:
            self.commands[command]["progress"] = 0
            self.commands[command]["level"] += 1
            print(
                f"{self.name} learned {command}! He is now level {self.commands[command]['level']} at {command}!"
            )
            return

    def giveitem(self, item):
        if item in self.toys:
            print(f"They already have a {item}!")
            return
        self.toys.append(item)
        print(f"{self.name} takes the {item}!")

    def takeitem(self, item):
        if item in self.toys:
            self.toys.remove(item)
            print(f"You take the {item} from Finnegan {self.name}!")
        else:
            print(f"{self.name} doesn't have a {item}!")
            return

    def command(self, command):
        if command not in self.commands:
            print(f"{self.name} doesn't know what you want!")
            return
        if self.commands[command]["level"] == 0:
            print(f"{self.name} tried to {command} but doesn't get it!")
            return
        if self.commands[command]["level"] == 1:
            print(f"{self.name} {command}s!")
            return
        if self.commands[command]["level"] == 2:
            print(f"{self.name} {command}s perfectly!")
            return
        if self.commands[command]["level"] == 3:
            print(f"{self.name} {command}s flawlessly!")
            return

    def play_with(self, other_dog):
        if self.energy <= 20:
            print(f"{self.name} is too tired to play right now.")
            return
        if other_dog.energy <= 20:
            print(f"{other_dog.name} is too tired to play right now.")
            return
        print(f"{self.name} and {other_dog.name} are playing together!")
        self.energy -= 10
        self.happiness += 10
        other_dog.energy -= 10
        other_dog.happiness += 10
