class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_available=True
class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_book=[]
class Library:
    def __init__(self,name):
        self.name=name
        self.book=[]
        self.member=[]
    def add_book(self,book):
        self.book.append(book)

    def register_member(self,member):
        self.member.append(member)
    def lend_book(self,member_id,isbn):
        member=next((m for m in self.member if m.member_id==member_id),None)
        book=next((b for b in self.book if b.isbn==isbn and b.is_available),None)
        if member and book:
            member.borrowed_book.append(book)
            book.is_available=False
            print(f"{book.title} lent to {member.name}")
library=Library("xxx library")
b1=Book("pyhthon progarming","john smith","124578")
b2=Book("java progarming","david","235689")
m1=Member("john","M1245")
library.add_book(b1)
library.add_book(b2)
library.register_member(m1)
library.lend_book("M1245","124578")

