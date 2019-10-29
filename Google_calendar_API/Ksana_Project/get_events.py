import datetime
from creds import service

now = datetime.datetime.utcnow().isoformat() + 'Z'
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='qnsbctripq4rvakgbvo26riubg@group.calendar.google.com', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
