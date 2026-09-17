# Investigación de Herencia Múltiple

class Phone:
    def make_call(self, number):
        print(f"Calling {number}...")


class Camera:
    def take_photo(self):
        print("Taking a photo...")


class Smartphone(Phone, Camera):
    def use_apps(self):
        print("Opening an application...")


phone = Smartphone()

phone.make_call("8888-8888")
phone.take_photo()
phone.use_apps()