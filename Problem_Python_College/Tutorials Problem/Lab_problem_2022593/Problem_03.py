from datetime import datetime
date=input()
format_input="%Y-%m-%d"

date = datetime.strptime(date, format_input)
print(date.strftime("%A"))