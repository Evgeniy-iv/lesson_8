import re


def email_parse(email_adress):
    email_parser = re.match(r'(?P<username>[0-9a-z._-]+)@(?P<domain>[0-9a-z]+\.[a-z]+)', email_adress)
    if email_parser is None:
        raise ValueError('Неверный формат адреса')
    d = email_parser.groupdict()
    print(d)




email_parse('admin11@mail.ru')
