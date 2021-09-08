import base
import package
from otherpack import func

class Garage:
    def __init__(self, maxCars):
        self.cars = []

    def addCar(color, model, year):
        """Big car boi comment"""
        
        self.cars.append({color: color, model: model, year: year})


