from datetime import datetime
from dateutil.parser import parse
from requests.exceptions import HTTPError, ConnectionError

def timezone_parser(timezone_code, timezone_service):
  
  response = timezone_service(timezone_code)
  
  if response['serviceResponse']:
    raise Exception(f"{response['serviceResponse']}")
  
  parsed_datetime = parse(response['currentDateTime'])
  
  result = dict({'code': timezone_code, 'timeZoneName': response['timeZoneName'], 
                'currentDate': datetime.strftime(parsed_datetime, '%Y-%m-%d'),
                'currentTime': datetime.strftime(parsed_datetime, '%H:%M')})
  
  return result
