from django.test import TestCase
from restaurant.models import *

#TestCase class
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=40, inventory=120)
        Menu.objects.create(title="Fried Rice", price=20, inventory=10)
    
    def test_get_all(self):
        # Query Menu objects with title "Pizza" and "Fried Rice"
        pizza = Menu.objects.get(title="Pizza")
        rice = Menu.objects.get(title="Fried Rice")
        
        # Compare the attributes of the Menu objects with the expected values
        self.assertEqual(pizza.title, "Pizza")
        self.assertEqual(pizza.price, 40)
        self.assertEqual(pizza.inventory, 120)
        
        self.assertEqual(rice.title, "Fried Rice")
        self.assertEqual(rice.price, 20)
        self.assertEqual(rice.inventory, 10)
        