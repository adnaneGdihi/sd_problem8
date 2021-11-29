import requests

def timezone_service(timezone_code):
  return requests.get(f'http://worldclockapi.com/api/json/{timezone_code}/now').json()