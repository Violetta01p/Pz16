from abc import ABC, abstractmethod

# Абстрактний інтерфейс для будь-якого сповіщення
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Реалізація сповіщення через email
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending email: {message}")

# Реалізація сповіщення через SMS
class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Sending SMS: {message}")

# Реалізація сповіщення через push
class PushNotifier(Notifier):
    def send(self, message):
        print(f"Sending push notification: {message}")

# NotificationService не залежить напряму від конкретного способу
# Він використовує будь-який об'єкт, що реалізує інтерфейс Notifier
class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message):
        self.notifier.send(message)

# Тестування:
email_service = NotificationService(EmailNotifier())
email_service.notify("Your order has been shipped!")

sms_service = NotificationService(SMSNotifier())
sms_service.notify("You have a new message.")
