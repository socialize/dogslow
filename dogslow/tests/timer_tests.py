'''
Created on Nov 2, 2012

@author: Jason Polites
'''
import unittest
from dogslow import timer
import time

class TimerTests(unittest.TestCase):

    def test_timer_with_milliseconds(self):
        runAt = 1.5
        test_timer = timer.Timer()
        test_timer.start();
        
        value = {}
        value['start'] = time.time();
        
        test_timer.run_later(self._test_callable, runAt, value);
        
        test_timer.join(2);
        
        diff = value['end'] - value['start']
        
        # It MAY not run exactly at 1.5 seconds, but should be less that 1.6
        self.assertTrue(diff >= runAt and diff < runAt + 0.1)
        
        test_timer.shutdown();

    def _test_callable(self, value):
        value['end'] = time.time()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()