# abstract interface.
class ShippingStrategy:
    def calculate(self, weight):
        pass

# shipping types are encapsulated strategies.
class ExpressShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 10

class StandardShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 5

# strategy object is passed.
def get_shipping_cost(strategy, weight):
    # call the right method
    return strategy.calculate(weight)

print(get_shipping_cost(ExpressShipping(), 3))  # 30
# print(get_shipping_cost(StandardShipping(), 3))  # 30