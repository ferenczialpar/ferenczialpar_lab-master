from venv.Contact import *
from venv.Phonebook_logical_part import *

class Program:
    def main(self):
        self.set_contacts()
        self.setContactData_toCsv(self._contacts)
        #objName = Contact("James,Buttino","Veilslide Co Inc","6311 Ref Night St","Texas","Texas","TX","70116","505-622-8927","507-855-1777","jbuttino@freemail.com")
        #self.addto_contactDatabase(objName)

if __name__ == "__main__":
    objName = Phonebook_logical_part()
    objName.main()