import unittest
import importlib
import os


class TestMessages(unittest.TestCase):
    def test_student_messages(self):
        # Path to the 'lide' directory
        lide_dir = os.path.join(os.path.dirname(__file__), 'lide')
        
        # Iterate over all files in the 'lide' directory
        for filename in os.listdir(lide_dir):
            if filename.endswith('.py'):
                module_name = f'lide.{filename[:-3]}'
                module = importlib.import_module(module_name)
                
                # Check if the module has a function named 'muj_pozdrav'
                self.assertTrue(hasattr(module, 'muj_pozdrav'), f"{module_name} does not have a function 'muj_pozdrav'")

if __name__ == '__main__':
    unittest.main()