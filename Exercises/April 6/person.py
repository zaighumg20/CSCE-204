class Person:
    def _int_(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        slef.phone_number = phone_number
        
    def display(self):
        print(f"Hello {self.first_name} {self.last_name}: {self.phone_number")


friend = Person("Amy", "Smith")
friend.display()