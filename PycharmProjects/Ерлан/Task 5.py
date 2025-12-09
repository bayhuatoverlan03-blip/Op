from abc import ABC, abstractmethod

# --- SINGLETON CONFIG ---
class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {"currency": "KZT"}
        return cls._instance


# --- STRATEGY ---
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"💳 Card: {amount} {AppConfig().settings['currency']}")


class KaspiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"📱 Kaspi: {amount} {AppConfig().settings['currency']}")


class QiwiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"🟠 QIWI: {amount} {AppConfig().settings['currency']}")


# --- FACTORY ---
class PaymentFactory:
    @staticmethod
    def create(method):
        m = method.lower()
        if m == "card":
            return CardPayment()
        if m == "kaspi":
            return KaspiPayment()
        if m == "qiwi":
            return QiwiPayment()
        raise ValueError("Unknown payment method")


# --- DEMO ---
if __name__ == "__main__":
    config = AppConfig()
    config.settings["currency"] = "KZT"

    p1 = PaymentFactory.create("kaspi")
    p1.pay(15000)

    p2 = PaymentFactory.create("card")
    p2.pay(7990)
