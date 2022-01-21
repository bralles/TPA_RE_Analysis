'''
This is a module to write into a Google Sheet stored under Alex > Python in google drive.

Need to pip install gspread

Need to place a json file under re_env/gspread. Ask me where that is located.

'''

import gspread
from datetime import date, datetime

today_ = date.today()

g_ = gspread.service_account(filename='/Users/alexsalas/Documents/github/TPA_RE_Analysis/service_account.json')
sh = g_.open_by_key('1Xwk3uTFUnuWfUt0ysdv5gNbrt9wJNil8WJBEasK0WKU')

worksheet = sh.get_worksheet(0)
worksheet.update_cell(2,2, today_)