
import Classes.zadanie1 as zad1
import Classes.zadanie2 as zad2
import Classes.zadanie3 as zad3

student1 = zad1.Student("Karol", 75)
student2 = zad1.Student("Emily", 44)
def zadanie1(st):
    return st.is_passed()
print(f"Zadanie 1: {zadanie1(student1)}, {zadanie1(student2)}")

###ZADANIE 2
biblioteka1 = zad2.Library("Berlin", "Lazurowa", "44-212", "7-18", 774980223)
biblioteka2 = zad2.Library("Warszawa", "Złota", "23-423", "8-16", 223445197)
pracownik1 = zad2.Employee(
    "Wiktor",
    "Szpak",
    "23.11.2024",
    "12.07.2000",
    "Warszawa",
    "Jesionowa",
    "23-423",
    878234121,
)
pracownik2 = zad2.Employee(
    "Hans",
    "Frank",
    "12.10.1999",
    "07.02.1942",
    "Berlin",
    "Powstancow",
    "44-212",
    235666789,
)
pracownik3 = zad2.Employee(
    "Karol",
    "Dziubka",
    "05.05.2025",
    "12.01.2004",
    "Katowice",
    "Abażurowa",
    "42-721",
    552978546,
)

Wladca_pierscieni = zad2.Book("21.11.1970", "J.R.R", "Tolkien", "612")
Metro2033 = zad2.Book("2012", "Dmitry", "Glukhovski", "701")
PrinciplesOfManagment = zad2.Book("1998", "Ricky", "Griffin", "539")
Biblia = zad2.Book("0", "Natchniony", "Autor", "3219")
Mein_Kampf = zad2.Book("1920", "Adolf", "Hitler", "242")

order1 = zad2.Order(pracownik1.first_name, "Karol", "Wladca_pierscieni", "12.07.2024")
print(f"Zadanie 2: {order1}")
###ZADANIE 3

Property1 = zad3.Property("Centrum", "15", "13400", "Katowicka 12")
House1 = zad3.House("Katowice", "12", "12330", "Koszutka", 123)
Flat1 = zad3.Flat(3, "Kraków", "2", "210002", "Studencka 7")
print(f"Zadanie 3: {Flat1}, {House1}")