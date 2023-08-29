import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Use regular expressions to find all email addresses in the string
        email_addresses = re.findall(r'\S+@\S+', self.email_string)

        # Convert the list to a set to remove duplicates, then back to a sorted list
        unique_sorted_emails = sorted(list(set(email_addresses)))

        return unique_sorted_emails
