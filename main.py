import eel
import pyowm

eel.init("web")

eel.start("main.html", size=(700, 700))


owm = pyowm.OWM("9fc8ea71fd7b3017951a4f06742d3c33")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return " В городе " + city + " сейчас " + str(temp) + " градусов!"

#eel.init("web")

#eel.start("main.html", size=(700, 700))
