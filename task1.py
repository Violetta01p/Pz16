class Book:
   def __init__(self, title, author):
       self.title = title
       self.author = author


class BookDisplay:
   def display(self, book):
       print(f"Назва: {book.title}, Автор: {book.author}")


class BookPersistence:
   def save(self, book):
       print(f"Книга '{book.title}' збережена у базі даних (імітація).")


class BookUpdater:
   def update_info(self, book, title, author):
       book.title = title
       book.author = author
       print(f"Інформацію оновлено: нова назва — '{title}', новий автор — '{author}'")
# Створення об'єкта книги
book = Book("Місто", "Валер'ян Підмогильний")


# Вивід
display = BookDisplay()
display.display(book)


# Оновлення
updater = BookUpdater()
updater.update_info(book, "Тіні забутих предків", "Михайло Коцюбинський")


# Вивід оновленої книги
display.display(book)


# Збереження
saver = BookPersistence()
saver.save(book)
