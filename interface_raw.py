from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None: pass

class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'Email message - {message}')

class SNSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'SMS message - {message}')

class Notification:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender
    
    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)

obj = Notification(EmailNotificationSender())

obj.send('Hello World')