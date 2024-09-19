import unittest

import re

from pyhton_task.verify_email import validate_email


class test_validate_email(unittest.TestCase):

    def test__that_check_email_is_valid(self):
          valid_emails = [ "example@example.com", "user.name+tag+sorting@example.com", "user_name@example.co.in", "user-name@example.org", "user.name@sub.example.com" ]

          invalid_emails = [ "plainaddress", "@missingusername.com", "username@.com", "username@com", "username@domain..com" ]

          for email in valid_emails: assert is_valid_email(email), f"Valid email failed: {email}"

          for email in invalid_emails: assert not is_valid_email(email), f"Invalid email passed: {email}"

        print("All test cases passed!")

