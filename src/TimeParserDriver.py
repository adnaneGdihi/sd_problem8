from .TimeParser import timezone_parser
from .TimeService import timezone_service
from requests.exceptions import HTTPError

def main():
  with open('data/sample.txt', 'r') as timezones_record:
    timezone_codes = timezones_record.read().split('\n')
    
    timezones_record.close()
    
  print(f"Code\tTimezone\t\t\t\t\tDate\t\t\t\tTime")
  
  for code in timezone_codes:
      try:
        timezone = timezone_parser(code, timezone_service)
        print(f"{timezone['code']}\t{timezone['timeZoneName']}\t\t\t\t\t{timezone['currentDate']}\t\t\t\t{timezone['currentTime']}")
      except Exception as e:
        print(f'{code} Error: {e}')
        
if __name__ == '__main__':
  main()