import unittest
from emp import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # can be used to populate a database to set up testing
        pass

    @classmethod
    def tearDownClass(cls):
        # can be used to clean up the database to start other testing from clean state
        pass

    def setUp(self):
        # run this before every single test
        # can be used to add files to a directory
        self.emp_1 = Employee('Coray', 'Schafer', 50000)
        self.emp_2 = Employee('Abhijit', 'Sinha', 99000)

        pass

    def tearDown(self):
        # run this after every single test
        # can be used to delete files from directory those created during testing
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Coray.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Abhijit.Sinha@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Sinha@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Coray Schafer')
        self.assertEqual(self.emp_2.fullname, 'Abhijit Sinha')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Sinha')

if __name__ == '__main__':
    unittest.main()
