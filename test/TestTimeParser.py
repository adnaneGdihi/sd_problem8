import unittest
from src.TimeParser import timezone_parser
from requests.exceptions import HTTPError, ConnectionError
from dateutil.parser import parse
import json

class TestTimeParser(unittest.TestCase):
  
  maxDiff = None
  
  def setUp(self):
    self.timezone_service_payload = dict({'code': 'cst', 'timeZoneName': 'Central Standard Time', 
                                          'currentDateTime': "2021-11-28T15:23-06:00", 'serviceResponse': None})
    
    
  def test_canary(self):
    self.assertTrue(True)
  
  def test_timezone_parser_reponse_has_currentDate(self):
    timezone_service = lambda timezone_code: self.timezone_service_payload

    self.assertEqual('2021-11-28', timezone_parser('cst', timezone_service)['currentDate'])
  
  def test_timezone_parser_reponse_has_timeZoneName(self):
    timezone_service = lambda timezone_code: self.timezone_service_payload
    
    self.assertEqual('Central Standard Time', timezone_parser('cst', timezone_service)['timeZoneName'])
      
  def test_raise_exception(self):
    self.timezone_service_payload['serviceResponse'] = 'pdt is not a valid Time Zone. Check the Time Zone Service for a list of valid time zones.'
    
    timezone_service = lambda timezone_code: self.timezone_service_payload
    
    with self.assertRaises(Exception) as context:
      timezone_parser('pdt', timezone_service)
      
      self.assertEqual('pdt is not a valid Time Zone. Check the Time Zone Service for a list of valid time zones.', context.exception.msg)
    
  def test_timezone_parser_reponse_is_correct(self):
    timezone_service = lambda timezone_code: self.timezone_service_payload
    
    result = dict({"currentDate": "2021-11-28", "currentTime": "15:23", "code": "cst", "timeZoneName": "Central Standard Time"})
    
    self.assertEqual(result, timezone_parser('cst', timezone_service))