import csv

class Contact(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

with open('contacts.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    contacts = []
    for row in reader:
        contact = Contact(row['first_name'], row['last_name'], row['email'])
        contacts.append(contact)