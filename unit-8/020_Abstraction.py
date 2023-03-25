from abc import ABC , abstractmethod

# > The Price class is an abstract class that defines the interface for the price of a movie.
class Price(ABC):
    def print_slip(self,amount):
        print("Payment amount $",amount)
    
    # A decorator that is used to define an abstract method.
    @abstractmethod
    def payment(self):
        print("This is important from abstractMethod.")
        
class CreditCardPayment(Price):
    def payment(self, amount):
        print("Pay with creditCardPayment $",amount)

class MobileBanking(Price):
    def payment(self, amount):
        print("Pay with MobileBanking $",amount)
        # Calling the abstract method.
        super().payment()

obj = CreditCardPayment()
obj.payment(1000)
obj.print_slip(3000)

obj1 = MobileBanking()
obj1.payment(4000)
obj1.print_slip(5000)

