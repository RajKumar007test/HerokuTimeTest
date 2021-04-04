import gspread as gsp
import pandas as pd
from os import environ
import datetime as dt
import time

gc = gsp.service_account(filename = 'Insert the JSON file that google provided to you')

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

