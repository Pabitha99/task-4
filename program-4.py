class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LED(TV):
    def __init__(self, brand,screen_thickness,energy_usage,lifespan,refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate


class Plasma(TV):
    def __init__(self, brand,screen_thickness,energy_usage,lifespan,refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
 
led_tv = LED("Onida","Thin", "Low", "10 years", "120 Hz")
led_tv.set_channel(5)
led_tv.increase_volume()
print(led_tv.status())  # Output: Sony at channel 5, volume 51

plasma_tv = Plasma("Sony","Thicker", "High", "8 years", "60 Hz")
plasma_tv.decrease_volume()
plasma_tv.reset_tv()
print(plasma_tv.status())  # Output: Samsung at channel 1, volume 50
