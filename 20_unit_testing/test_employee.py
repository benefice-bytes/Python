import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Nagesh', 'G', 50000)
        self.emp_2 = Employee('Satish', 'Narra', 50000)

    def tearDown(self):
        print('tear down!\n')
        
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Nagesh.G@email.com')
        self.assertEqual(self.emp_2.email, 'Satish.Narra@email.com')

        self.emp_1.first = 'ram'
        self.emp_2.first = 'ramki'
        
        self.assertEqual(self.emp_1.email, 'ram.G@email.com')
        self.assertEqual(self.emp_2.email, 'ramki.Narra@email.com')


if __name__ == '__main__':
    unittest.main()
