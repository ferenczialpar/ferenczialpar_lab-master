from venv.Contact import *

class Phonebook_logical_part:
    def __init__(self):
        self._contacts = []

    def get_contacts(self):
        return self._contacts

    def set_contacts(self):
        self._contacts = self.getContactData_toCsv()

    #___Alapműveletek kontaktokkal
    def modify_contactData(self,contact):
        pass
        #Todo módosítani --> törölni jelenlegit és a _contactlistbe appendelni

    def addto_contactDatabase(self,contact):
        self._contacts.append(contact)
        pass
        # Todo hozzáadni egy új kontaktot

    def deletefrom_contactDatabase(self,contact):
        for element in self._contacts:
            if element.get_first_name()==contact.first_name() & element._phone()==contact._phone():
                del _contacts[index(element)]
                pass

    def searchPhone(self,contact):
        for element in self._contacts:
            if element.get_first_name()==contact.first_name() & element._phone()==contact._phone():
                return element.get_phone() #Todo keresztnév alapján keresés


    def commandContacts(self):
        print("")

    #___Adatok elérése
    def getContactData_toCsv(self):
        with open('Contact_list.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            contactdatabase = []
            for row in spamreader:
                localobjects = str(row).split(",")
                newItem=Contact(localobjects[0], localobjects[1],localobjects[2],localobjects[3],localobjects[4],localobjects[5],localobjects[6],localobjects[7],localobjects[8],localobjects[9],localobjects[10])
                contactdatabase.append(newItem)
            return contactdatabase

    def setContactData_toCsv(self,spamwriter):
        with open('Contact_list.csv', 'w', newline='') as csvfile:

            contact_writer  = csv.writer(csvfile, delimiter=',')
            for row in spamwriter:
                contact_writer.writerow([row.get_first_name(),row.get_last_name(),row.get_company_name(),row.get_address(),row.get_city(),row.get_county(),row.get_state(),row.get_zip(),row.get_phone1(),row.get_phone(),row.get_email()])


    #Alap megjelenítés

    def main(self):
        self.set_contacts()
        self.setContactData_toCsv(self._contacts)
        objName = Contact("","","","","","","","","","","")
        self.addto_contactDatabase(objName)
        print("t")



        #self.itemlist = self.getContactData_toCsv()

if __name__ == "__main__":
    objName = Phonebook_logical_part()
    objName.main()
        # objName = Contact("","","","","","","","","","","")
        # objName.main()


#Egyszerű parancssoros app 3 opció keresés