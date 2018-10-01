from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

import requests
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

class WeatherForm(FlaskForm):
	zipcode = StringField('Enter your zipcode', validators=[Required() ])
	submit = SubmitField()

	def validate_zipcode(self, field): #validate_nameofmyfield 
		if len(str(field.data)) != 5:
			raise ValidationError("Your zipcode is not valid because it is not 5 digits.")


@app.route('/weatherform', methods = ['GET,' 'POST'])
def weatherForm():
	weatherform = WeatherForm()
	if weatherform.validate_on_submit():
		zipcode = str(form.zipcode.data)
		params = {}
		params['zip'] = zipcode + ',us'
		params['appid'] = 'db8c448dd9187d3a4520f5275047c90a'
		baseurl = 'http://api.openweathermap.org/data/2.5/weather?'
		response = requests.get(baseurl, params = params)
		response_dict = json.loads(response.text)
		print(response_dict)

		description = response_dict['weather'][0]['description']
		city = response_dict['name']
		temp_kelvin = response_dict['main']['temp']

		return render_template('results.html', weather = description, city=city, temp=temp_kelvin)
	flash(form.errors)
	return render_template ('weather.html', form = weatherform)

if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)
   