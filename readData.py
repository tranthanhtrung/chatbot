import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getData():
	scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name("Chatbot-a318511364f3.json", scope)

	gc = gspread.authorize(credentials)

	wks = gc.open("Untitled form (Responses)").sheet1

	return wks.get_all_records()