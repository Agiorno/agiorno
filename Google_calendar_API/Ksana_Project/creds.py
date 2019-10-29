import pickle
import os.path
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
creds = pickle.load(open('token_calendar.pickle','rb'))
with open('token_calendar.pickle', 'wb') as token_calendar:
    pickle.dump(creds, token_calendar)
service = build('calendar', 'v3', credentials=creds)
