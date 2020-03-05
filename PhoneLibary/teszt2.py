import unittest

from venv.Contact import *
from venv.Phonebook_logical_part import *

class FirstTestCase(unittest.TestCase):
    def test_phonebook_length(self):
        self.phonebook = Phonebook_logical_part()
        self.phonebook.set_contacts()
        listdata= self.phonebook.get_contacts()
        self.assertEqual(len(listdata), 100)

    def add_newcontact_csv(self):
        newperson = Contact("James","Buttino", "Veilslide Co Inc", "6311 Ref Night St", "Texas", "Texas", "TX", "70116",
                          "505-622-8927", "507-855-1777", "jbuttino@freemail.com")
        self.phonebook = Phonebook_logical_part()
        self.phonebook.set_contacts()
        listdata = self.phonebook.get_contacts()
        size = len(listdata)
        listdata.append(newperson)
        self.assertEqual(len(listdata), 20)

    def get_contact_name(self):
        newperson = Contact("Simona","Morasca","Chapman Ross E Esq","3 Mcauley Dr","Ashland","Ashland","OH","44805","419-503-2484","419-800-6759","simona@morasca.com")
        self.phonebook = Phonebook_logical_part()
        self.phonebook.set_contacts()
        listdata = self.phonebook.get_contacts()
        self.assertEqual(self.searchPhone(newperson),"Simona")


if __name__ == '__main__':
    unittest.main()
