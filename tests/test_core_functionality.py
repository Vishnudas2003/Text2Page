import os
import shutil
import unittest
from text2page import process_input

class TestCoreFunctionality(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or common resources
        self.output_dir = os.path.join(os.path.dirname(__file__), "test_output")

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_process_input_file(self):
        # Test when the input is a file
        input_file = os.path.join(os.path.dirname(__file__), "test_input.txt")
        output_dir = self.output_dir
        stylesheet_url = "your_stylesheet_url"  # Replace with an actual URL if needed

        # Your test logic for process_input with a file
        process_input(input_file, output_dir, stylesheet_url)

        # Add assertions to check the expected output or any side effects
        expected_output_file = os.path.join(output_dir, "test_input.html")
        self.assertTrue(os.path.exists(expected_output_file), "Output file does not exist")
        # You can add more specific assertions based on the expected content or other criteria

    def test_process_input_directory(self):
        # Test when the input is a directory
        input_dir = os.path.join(os.path.dirname(__file__), "test_directory")
        output_dir = self.output_dir
        stylesheet_url = "your_stylesheet_url"  # Replace with an actual URL if needed

        # Your test logic for process_input with a directory
        process_input(input_dir, output_dir, stylesheet_url)

    def test_process_input_invalid_path(self):
        # Test when the input path is invalid
        invalid_path = "invalid_path"
        output_dir = self.output_dir
        stylesheet_url = "your_stylesheet_url"  # Replace with an actual URL if needed

        # Your test logic for process_input with an invalid path
        process_input(invalid_path, output_dir, stylesheet_url)

        # Add assertions to check the expected output or any side effects
        # For example, you can check that an error message is printed or a specific exception is raised

if __name__ == "__main__":
    unittest.main()
