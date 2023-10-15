disk_size = 1.44 * 1024 * 1024
bytes_char = 4
pages = 100
lines = 50
chars = 25
size_book = 100 * 50 * 25 * 4
number_of_books = int(disk_size // size_book)
print("Количество книг, помещающихся на дискету:", number_of_books)
