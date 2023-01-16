from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions_and_testsuites import AssertionsTests, SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {      
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

