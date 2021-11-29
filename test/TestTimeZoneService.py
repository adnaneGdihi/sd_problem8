import unittest
from src.TimeService import timezone_service

class TestTimeZoneService(unittest.TestCase):
  
  def test_serviceResponse(self):
    
    self.assertIsInstance(timezone_service('cst'), dict)
  
  def test_attribute_currentDateTime(self):
    self.assertTrue('currentDateTime' in timezone_service('cst').keys())
  
  def test_attribute_timeZoneName(self):
    self.assertTrue('timeZoneName' in timezone_service('cst').keys())
    
  