import gspread as gsp
import pandas as pd
import datetime as dt
import time

gc = gsp.service_account(filename = 'E:\COMPUTER\Python 3\experiments\Google Sheets Automation\sage-reach-309201-06113ed6791b.json')

sh = gc.open('TestTimeHeroku')
worksheet1 = sh.sheet1

count = 1
while True:
	date_time = dt.datetime.now()
	if date_time.second == 0 and ((date_time.minute % 10) == 0):
		cell_add = 'A'+str(count)
		count = count + 1
		worksheet1.update(cell_add,date_time.strftime('%d-%m-%Y %H:%M:%S'))
		time.sleep(570)

