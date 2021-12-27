from os import system, name
try:
    userinput = input("We will install an outside package that will make the loading animation work, are you sure you want to proceed? (Y/N): ")
    if userinput == "y" or "Y":
        if name == "nt":
            print("Installing packages please wait... \n\n")
            _ = system("pip install progress progressbar2 alive-progress tqdm")
            _ = system("cls")
        else:
            print("Installing packages please wait... \n\n")
            _ = system("pip install progress progressbar2 alive-progress tqdm")
            _ = system("cls")
        from progress.spinner import MoonSpinner
    else:
        print("Either input invalid or typed 'n'/'N'.")
        raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Keyboard Interrupt or Invalid input, therefore cancelling installation")

import time

class cusload:
    def __init__(self, cusrange, custime):
        self.cusrange = cusrange
        self.cusrange = int(cusrange)
        self.custime = custime
        self.custime = int(custime)

    def cusanimation(self):
        with MoonSpinner('Processing…') as bar:
            for i in range(self.cusrange):
                time.sleep(self.custime)
                bar.next()



class Item:
    def __init__(self, name: str):
        self.name = name


class Inventory:
    def __init__(self):
        self.items = set()

    def add_item(self, item: Item):
        self.items.add(item)

    def remove_item(self, item: Item):
        self.items.remove(item)
        


class Location:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.items = []
        self.actions = []

    def add_item(self, item: Item):
        self.items.append(item)
    

    def add_activity(self, action):
        self.actions.append(action)


class Transition:
    def __init__(self, old_location: Location, new_location: Location):
        self.old_location = old_location
        self.new_location = new_location


class Action:
    def __init__(self, name: str, required_items: set = None):
        self.name = name
        if required_items is None:
            required_items = []
        self.required_items = required_items

    def run(self, location: Location, inventory: Inventory) -> Transition:
        pass


class ItemAction(Action):
    def __init__(self, name: str, target_item: Item = None):
        super().__init__(name, None)
        self.target_item = target_item

    def run(self, location: Location, inventory: Inventory):
        print(f"You've chosen to {self.name}")
        location.items.remove(self.target_item)
        inventory.add_item(self.target_item)
        return None

class DropItem(Action):
    def __init__(self, name: str, target_item: Item = None):
        super().__init__(name, None)
        self.target_item = target_item

    def run(self, location: Location, inventory: Inventory):
        print(f"You've chosen to {self.name}")
        location.items.append(self.target_item)
        inventory.remove_item(self.target_item)
        return None

class TransitionAction(Action):
    def __init__(self, name: str, target_location: Location, required_items: set = None):
        super().__init__(name, required_items)
        self.target_location = target_location

    def run(self, location: Location, inventory: Inventory):
        print(f"You left {location.name} and went to {self.target_location.name}")
        return Transition(location, self.target_location)


class Game:
    def __init__(self, name: str):
        self.name = name
        self.locations = []
        self.inventory = Inventory()

    def add_location(self, location):
        self.locations.append(location)

    def start(self):
        print(self.name)
        current_location = self.locations[0]
        while True:
            print(f"You are in {current_location.name}")
            print(current_location.description)
            transition = self.handle_actions(current_location, self.inventory)

            if transition is not None:
                current_location = transition.new_location

            if current_location == self.locations[-1]:
                exit()

    def handle_actions(self, location: Location, inventory: Inventory) -> Transition:
        print("What do you want to do?")
        available_actions = self.get_available_actions(location)
        for idx, activity in enumerate(available_actions):
            if set(self.inventory.items).issuperset(activity.required_items):
                print(f"{idx + 1}) {activity.name}")
        player_choice = self.prompt_action_choice(available_actions)
        chosen_action = available_actions[player_choice - 1]
        return chosen_action.run(location, inventory)

    def get_available_actions(self, location):
        available_actions = []
        for action in location.actions:
            if isinstance(action, TransitionAction) and self.inventory.items.issuperset(action.required_items):
                available_actions.append(action)
            if isinstance(action, ItemAction) and action.target_item in location.items:
                available_actions.append(action)
            if isinstance(action, DropItem) and action.target_item in self.inventory.items:
                available_actions.append(action)

        return available_actions

    def prompt_action_choice(self, available_actions):
        while True:
            user_input = input()
            try:
                choice = int(user_input)
                if choice <= 0 or choice > len(available_actions):
                    raise ValueError
                return choice
            except ValueError:
                print("Enter a valid choice number")


