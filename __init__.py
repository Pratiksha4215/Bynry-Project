# customer_service/__init__.py

def some_function():
    from .models import ServiceRequest, Customer
    # Your code here

# Or inside a method of a class
class SomeClass:
    def some_method(self):
        from .models import ServiceRequest, Customer
        # Your code here

