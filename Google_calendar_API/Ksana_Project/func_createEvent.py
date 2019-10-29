import datefinder
from creds import service
from datetime import timedelta

def create_event(start_time_str, summary, duration, description, location, timezone, calendarIdd):
    matches=list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)

    event = {
      'summary': summary,
      'location': location,
      'description': description,
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      }, #'recurrence': [
         #'RRULE:FREQ=DAILY;COUNT=1'
       #],
      # 'attendees': [
     #    {'email': 'agiorno@me.com'},
     #    {'email': 'azarovanadin@yahoo.com.ua'},
      # ],
       #'reminders': {
         #'useDefault': False,
         #'overrides': [
          # {'method': 'email', 'minutes': 24 * 60},
           #{'method': 'popup', 'minutes': 10},
         #],
       #},
    }

    return service.events().insert(calendarId=calendarIdd, body=event).execute(), print("That event has created")
