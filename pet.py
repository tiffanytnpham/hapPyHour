import datetime


class Pet:
    def __init__(self):
        """Initialize the pet with default values, starts at max."""
        self.name = ""
        self.food = 5
        self.happiness = 5
        self.health = 10
        self.sleep_timer = 0
        self.days_at_max_health = 0
        self.is_asleep = False
        self.level = 1
        self.earliest_sleep_hour = 20  # Pet cannot sleep before 8 PM
        self.wake_up_hour = 9  # Pet wakes up at 9 AM

    def feed(self, amount):
        """Feed the pet to increase its food level, and check its health impact. Cannot feed if food is full or asleep."""
        if self.is_asleep:
            print(f"{self.name} is asleep and cannot eat right now.")
            return
        if self.food >= 5:
            print(f"{self.name} is already full. Cannot feed more.")
            return
        self.food = min(5, self.food + amount)
        self.check_health()
        print(f"Feeding {self.name} increases food by {amount}.")

    def play(self, amount):
        """Play with the pet to increase its happiness, and check its health impact. Cannot play if happiness is full or asleep."""
        if self.is_asleep:
            print(f"{self.name} is asleep and cannot play right now.")
            return
        if self.happiness >= 5:
            print(f"{self.name} is already happy. Cannot increase happiness further.")
            return
        self.happiness = min(5, self.happiness + amount)
        self.check_health()
        print(f"Playing increases {self.name}'s happiness by {amount}.")

    def sleep(self, current_hour):
        """Manage the pet's sleep based on the current hour (24-hour format)."""
        print(f"Current Hour: {current_hour}")

        if current_hour < self.earliest_sleep_hour:
            hours_until_sleep = self.earliest_sleep_hour - current_hour
            print(f"Too early to sleep. {hours_until_sleep} hour(s) until sleep time.")
            return  # Do not modify sleep status or other attributes

        # Sleep logic only applies if it's the right time
        if 20 <= current_hour <= 22:
            self.happiness = 5
            self.is_asleep = True
            print("Sleep within 8-10 PM: Happiness fully restored.")
        elif 22 < current_hour <= 24:
            self.happiness = max(0, self.happiness - 1)
            self.is_asleep = True
            print("Late sleep (10 PM - 12 AM): Happiness decreased by 1.")
        else:
            self.happiness = max(0, self.happiness - 2)
            self.health = max(0, self.health - 1)
            self.is_asleep = True
            print("Very late sleep or no sleep: Happiness decreased by 2 and health by 1.")

        # Calculate hours until wake-up if asleep
        if self.is_asleep:
            hours_until_wake = (self.wake_up_hour + 24 - current_hour) % 24
            print(f"{hours_until_wake} hour(s) until wake-up time.")

    def wake_up(self):
        """Wake the pet up from sleep."""
        self.is_asleep = False
        print(f"{self.name} is awake.")

    def check_auto_wake_up(self):
        """Automatically wake the pet if it is asleep and the current hour is the wake-up hour."""
        current_hour = datetime.datetime.now().hour
        if self.is_asleep and current_hour == self.wake_up_hour:
            self.wake_up()
        elif self.is_asleep:
            hours_until_wake = (self.wake_up_hour + 24 - current_hour) % 24
            print(f"Pet is still asleep. {hours_until_wake} hour(s) until wake-up time.")

    def update_hourly(self):
        """Decrement food and happiness hourly, check health impacts, and handle sleep."""
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        print(f"Before Update - Food: {self.food}, Happiness: {self.happiness}, Health: {self.health}")

        self.food = max(0, self.food - 1)
        self.happiness = max(0, self.happiness - 1)

        self.sleep(current_hour)
        self.check_health()
        self.check_auto_wake_up()

        print(f"After Update - Food: {self.food}, Happiness: {self.happiness}, Health: {self.health}")

    def check_health(self):
        """Adjust the pet's health based on its food and happiness levels."""
        if self.food == 0 or self.happiness == 0:
            self.health = max(0, self.health - 1)
        elif self.food == 5 or self.happiness == 5:
            self.health = min(10, self.health + 1)
        self.check_evolution()

    def check_evolution(self):
        """Determine if the pet evolves based on its health status."""
        if self.health == 10:
            self.days_at_max_health += 1
            if self.days_at_max_health >= 3:
                self.evolve()
        else:
            self.days_at_max_health = 0

    def determine_state(self):
        """Determine the current visual state of the pet based on its stats."""
        if self.is_asleep:
            return "asleep"
        if self.happiness == 5 and self.health == 10 and self.food == 5:
            return "happy"
        elif self.happiness <= 2 or self.health <= 6 or self.food <= 2:
            return "unhappy"
        else:
            return "idle"

    def evolve(self):
        """Handle the pet's evolution process."""
        if self.level < 3:  # Maximum Level
            self.level += 1
            print(f"{self.name} has evolved to level {self.level}!")

    def set_name(self, name):
        """Set the pet's name."""
        self.name = name
