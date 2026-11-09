
class Scooter:
    PER_MINUTE = 1
    def __init__(self, scooter_id, battery):
        self.scooter_id = scooter_id
        self.battery = battery

    def in_use(self):
        used = False
        return used

    def price(self, minutes):
        price_minutes = minutes * Scooter.PER_MINUTE
        return price_minutes + 5