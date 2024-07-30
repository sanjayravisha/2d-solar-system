from solar_system import SolarSystem, Star, Planet

solar_system = SolarSystem(width=1400, height=900)

sun = Star(solar_system, mass=10000)

planets = (
    Planet(solar_system, mass=1, position=(-350, 0), velocity=(0, 5)),
    Planet(solar_system, mass=2, position=(-270, 0), velocity=(0, 7))
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()

import turtle

turtle.done()
