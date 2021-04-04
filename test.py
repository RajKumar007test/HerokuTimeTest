import gspread as gsp
import pandas as pd
from os import environ
from flask import Flask
import datetime as dt
import time

app = Flask(__name__)
app.run(debug=False, port=int(environ.get('PORT',5000)), host='0.0.0.0')

gc = gsp.service_account(filename = 'sage-reach-309201-06113ed6791b.json')

sh = gc.open('TestTimeHeroku')
worksheet1 = sh.sheet1

count = 1
while True:
	date_time = dt.datetime.now()
	if date_time.second == 0:
		print(date_time)
		cell_add = 'A'+str(count)
		count = count + 1
		worksheet1.update(cell_add,date_time.strftime('%d-%m-%Y %H:%M:%S'))
		time.sleep(50)

