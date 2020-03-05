import csv

class Contact:
  def __init__(self, first_name, last_name, company_name, address, city, county, state, zip, phone1, phone, email):
    self._first_name = first_name
    self._last_name = last_name
    self._company_name = company_name
    self._address = address
    self._city = city
    self._county = county
    self._state = state
    self._zip = zip
    self._phone1 = phone1
    self._phone = phone
    self._email = email
#getter
  def get_first_name(self):
      return self._first_name
  def get_last_name(self):
      return self._last_name
  def get_company_name(self):
      return self._company_name
  def get_address(self):
      return self._address
  def get_city(self):
      return self._city
  def get_county(self):
      return self._county
  def get_state(self):
      return self._state
  def get_zip(self):
      return self._zip
  def get_phone1(self):
      return self._phone1
  def get_phone(self):
      return self._phone
  def get_email(self):
      return self._email
#setter
  def set__first_name(self,value):
      self._first_name =value
  def set__last_name(self,value):
      self._last_name =value
  def set_company_name(self,value):
      self._company_name =value
  def set__address(self,value):
      self._address =value
  def set_city(self,value):
      self._city =value
  def set_country(self,value):
      self._country=value
  def set_state(self,value):
      self.state=value
  def set_zip(self,value):
      self._zip =value
  def set_phone1(self,value):
      self._phone1 =value
  def set_phone(self,value):
      self._phone =value
  def set_email(self,value):
      self._email =value

#Basic fgv
  def contact_info(self):
    print("Basic contact data: " + self.get_first_name(), " ", self.get_last_name(), " ", self.get_phone())


