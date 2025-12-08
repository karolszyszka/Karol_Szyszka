class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def str(self):
        return f"City= {self.city}, Street= {self.street}, Zip Cpde = {self.zip_code}, Phone= {self.phone}"





class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def str(self):
        return f"First name = {self.first_name}, Last Name = {self.last_name}, Hire date= {self.hire_date}, Birth date= {self.birth_date}, city = {self.city}, Street= {self.street}, Zip Code= {self.zip_code}, Phone= {self.phone}"



class Book:
    def __init__(self, publication_date, author_name, author_surname, number_of_pages):

        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def str(self):
        return f"Publication date = {self.publication_date}, Author name= {self.author_name}, Author Surname= {self.author_surname}, Number of Pages = {self.number_of_pages}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = []
        self.order_date = order_date

    def ksiazki(self, booksy: Book):
        self.books.append(booksy)

    def __str__(self):
        return f"{self.student} wypozyczyl od {self.employee} ksiazke {self.books}, dnia {self.order_date}"


