from flask import render_template, request, flash

from app import app
from app.forms import WeatherForm
from app.open_weather_api import OpenWeatherAPI

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current", methods=["GET", "POST"])
def current_weather():
	weather_form = WeatherForm(request.form)
	weather_item = None

	if request.method == "POST" and weather_form.validate():
		#Do stuff with the valid form
		city = weather_form.city.data
		country_code = weather_form.country_code.data
		
		try:
			api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"], weather_form.units.data)
			weather_item = api.get_current_weather(city, country_code)
		except ValueError as e:
			flash(str(e), "warning")
			return redirect ("/")

	return render_template("current.html", weather_form=weather_form, weather_item=weather_item)

@app.route("/forecast", methods=["GET", "POST"])
def forecast_weather():
	weather_form = WeatherForm(request.form)

	return render_template("forecast.html", weather_form=weather_form)