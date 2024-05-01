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

    def feed(self, amount):
        """Feed the pet to increase its food level, and check its health impact."""
        self.food = min(5, self.food + amount)
        self.check_health()

    def play(self, amount):
        """Play with the pet to increase its happiness, and check its health impact."""
        self.happiness = min(5, self.happiness + amount)
        self.check_health()

    def sleep(self, current_hour):
        """Manage the pet's sleep based on the current hour (24-hour format)."""
        print(f"Current Hour: {current_hour}")

        if 20 <= current_hour <= 22:
            self.happiness = 5  # Fully restores happiness if sleeping is done at the right time
            self.sleep_timer = 0  # Resets sleep timer
            self.is_asleep = True  # Set sleep state
            print("Sleep within 8-10 PM: Happiness fully restored.")
        elif 22 < current_hour <= 24:
            self.happiness = max(0, self.happiness - 1)  # Slightly decreases happiness if late
            self.is_asleep = True
            print("Late sleep (10 PM - 12 AM): Happiness decreased by 1.")
        else:
            self.happiness = max(0, self.happiness - 2)  # More severe penalty for happiness
            self.health = max(0, self.health - 1)  # Health penalty for very late sleep
            self.sleep_timer += 1  # Increment sleep timer for missed sleep
            self.is_asleep = True
            print("Very late sleep or no sleep: Happiness decreased by 2 and health by 1.")

    def wake_up(self):
        """Wake the pet up from sleep."""
        self.is_asleep = False  # Reset sleep state
        print(f"{self.name} is awake.")

    def check_auto_wake_up(self):
        """Automatically wake the pet if it is asleep and the current hour is 9 AM."""
        current_hour = datetime.datetime.now().hour
        if self.is_asleep and current_hour == 9:
            self.wake_up()

    def update_hourly(self):
        """Decrement food and happiness hourly, check health impacts, and handle sleep."""
        current_time = datetime.datetime.now()
        current_hour = current_time.hour  # Current hour in 24-hour format

        print(f"Before Update - Food: {self.food}, Happiness: {self.happiness}, Health: {self.health}")

        self.food = max(0, self.food - 1)
        self.happiness = max(0, self.happiness - 1)

        self.sleep(current_hour)  # Manage sleep based on the current hour
        self.check_health()  # Check and adjust health after sleep checks
        self.check_auto_wake_up()  # Check and handle auto wake-up at 9 AM

        print(f"After Update - Food: {self.food}, Happiness: {self.happiness}, Health: {self.health}")

    def check_health(self):
        """Adjust the pet's health based on its food and happiness levels."""
        if self.food == 0 or self.happiness == 0:
            self.health = max(0, self.health - 1)  # Health decreases if either is zero
        elif self.food == 5 or self.happiness == 5:
            self.health = min(10, self.health + 1)  # Health improves if either is at maximum
        self.check_evolution()  # Check for possible evolution

    def check_evolution(self):
        """Determine if the pet evolves based on its health status."""
        if self.health == 10:
            self.days_at_max_health += 1  # Increment days at max health
            if self.days_at_max_health >= 3:
                self.evolve()  # Evolve if at max health for 3 consecutive days
        else:
            self.days_at_max_health = 0  # Reset the counter if health drops below 10

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
        if self.level < 3:   #Maximum Level
            self.level += 1
            print(f"{self.name} has evolved to level {self.level}!")

    def set_name(self, name):
        """Set the pet's name."""
        self.name = name
