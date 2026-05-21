import unittest
from utils.code_parser import detect_language
from utils.security_checker import check_security

class TestCodeReviewer(unittest.TestCase):
    def test_language_detection(self):
        self.assertEqual(detect_language("test.py"), "Python")
        self.assertEqual(detect_language("test.java"), "Java")

    def test_security_check(self):
        code = "password = '123'"
        vulnerabilities = check_security(code)
        self.assertTrue(len(vulnerabilities) > 0)
        self.assertEqual(vulnerabilities[0]['type'], "Hardcoded Credentials")

if __name__ == '__main__':
    unittest.main()
