# Абстрактний клас (інтерфейс) для всіх платежів
class Payment:
    def pay(self, amount):
        raise NotImplementedError  # Метод має бути перевизначений у нащадках

# Платіж кредитною карткою
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплачено {amount} грн кредитною карткою.")

# Платіж через PayPal
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплачено {amount} грн через PayPal.")

# Платіж криптовалютою
class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплачено {amount} грн криптовалютою.")

# Функція, яка приймає будь-який тип платежу
def process_payment(payment: Payment, amount):
    payment.pay(amount)

# Тестування:
process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(), 200)
process_payment(CryptoPayment(), 300)

