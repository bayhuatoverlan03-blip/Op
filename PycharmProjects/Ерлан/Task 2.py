from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate(self, weight):
        pass


class FreeDelivery(DeliveryStrategy):
    def calculate(self, weight):
        return 0


class StandardDelivery(DeliveryStrategy):
    def calculate(self, weight):
        return 500 + weight * 50


class ExpressDelivery(DeliveryStrategy):
    def calculate(self, weight):
        return 1500 + weight * 80


def get_delivery_cost(weight, strategy: DeliveryStrategy):
    return strategy.calculate(weight)


# DEMO
if __name__ == "__main__":
    weight = 12

    print("Free:", get_delivery_cost(weight, FreeDelivery()))
    print("Standard:", get_delivery_cost(weight, StandardDelivery()))
    print("Express:", get_delivery_cost(weight, ExpressDelivery()))
