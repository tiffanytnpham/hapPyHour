class Pet:
    def __init__(self):
        """Initialize the pet with default values, starts at max."""
        self.name = ""
        self.food = 5
        self.happiness = 5
        self.health = 5
        self.sleep_timer = 0
        self.days_at_max_health = 0

    def feed(self, amount):
        """Feed the pet to increase its food level, and check its health impact."""
        self.food = min(5, self.food + amount)
        self.check_health()

    def play(self):
        """Play with the pet to increase its happiness, and check its health impact."""
        self.happiness = min(5, self.happiness + 1)
        self.check_health()

    def sleep(self, current_time):
        """Manage the pet's sleep based on the current time."""
        if 20 <= current_time <= 22:
            self.happiness = 5  # Fully restores happiness if sleeping is done at the right time
        elif 22 < current_time < 24:
            self.happiness = max(0, self.happiness - 1)  # Slightly decreases happiness if late
        else:
            self.happiness = max(0, self.happiness - 2)  # More severe penalty for happiness
            self.health = max(0, self.health - 1)  # Health penalty for very late sleep

    def update_hourly(self):
        """Decrement food and happiness hourly and check health impacts."""
        print(f"Before Update - Food: {self.food}, Happiness: {self.happiness}, Health: {self.health}")
        self.food = max(0, self.food - 1)
        self.happiness = max(0, self.happiness - 1)
        self.check_health()
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
        if self.happiness == 5 and self.health == 5 and self.food == 5:
            return 'happy'
        elif self.happiness <= 2 or self.health <= 2 or self.food <= 2:
            return 'unhappy'
        else:
            return 'idle'

    def evolve(self):
        """Handle the pet's evolution process."""
        print(f"{self.name} has evolved!")
        # DO: evolution mechanics

    def set_name(self, name):
        """Set the pet's name."""
        self.name = name
