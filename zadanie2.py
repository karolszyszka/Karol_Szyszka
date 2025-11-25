class Library:
    def __init__(self, city,street,zip_code,open_hours:str,phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def str(self):
        return f"City= {self.city}, Street= {self.street}, Zip Cpde = {self.zip_code}, Phone= {self.phone}"

biblioteka1 = Library("Berlin", "Lazurowa", "44-212", "7-18", 774980223)
biblioteka2 = Library("Warszawa", "Złota", "23-423", "8-16", 223445197)

class Employee:
    def __init__(self,first_name,last_name,hire_date,birth_date,city,street, zip_code,phone):
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

pracownik1 = Employee("Wiktor", "Szpak", "23.11.2024", "12.07.2000", "Warszawa", "Jesionowa","23-423",878234121)
pracownik2 = Employee("Hans", "Frank", "12.10.1999", "07.02.1942", "Berlin", "Powstancow", "44-212", 235666789)
pracownik3= Employee("Karol", "Dziubka", "05.05.2025", "12.01.2004", "Katowice", "Abażurowa", "42-721", 552978546)


class Book:
    def __init__(self,publication_date, author_name, author_surname, number_of_pages):

        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def str(self):
        return f"Publication date = {self.publication_date}, Author name= {self.author_name}, Author Surname= {self.author_surname}, Number of Pages = {self.number_of_pages}"
Wladca_pierscieni= Book("21.11.1970", "J.R.R","Tolkien", "612" )
Metro2033 = Book("2012", "Dmitry","Glukhovski", "701")
PrinciplesOfManagment = Book("1998", "Ricky", "Griffin", "539")
Biblia=Book("0","Natchniony","Autor","3219")
Mein_Kampf = Book("1920","Adolf","Hitler","242")

class Order:
    def __init__(self,employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = []
        self.order_date = order_date
    def ksiazki(self, booksy: Book):
        self.books.append(booksy)
    def __str__(self):
        return f"{self.student} wypozyczyl od {self.employee} ksiazke {self.books}, dnia {self.order_date}"
Zamowienie1 = Order("Karol", "Ania", "", "21.12.2025")
Zamowienie1.ksiazki(Wladca_pierscieni.author_surname)
Zamowienie2 = Order("Hans", "Emiliaa", "", "11.07.2025")
Zamowienie2.ksiazki(Metro2033.author_surname)
print(Zamowienie1)
print(Zamowienie2)