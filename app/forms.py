from wtforms import Form, StringField, validators

class WeatherForm(Form):
	city = StringField("City", validators=[validators.DataRequired()])
	country_code = StringField("Country Code")