from email_address_parser import EmailAddressParser

def test_parses_emails_with_commas_and_spaces_and_non_emails():
    '''finds emails with commas and spaces in between and removes non-email strings.'''
    parser = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
    assert(parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"])
