import os
import shutil
import unittest
from text2page import create_html_from_file

class TestText2Page(unittest.TestCase):
    def setUp(self):
        # Set up a common output directory for all tests
        self.output_dir = os.path.join(os.path.dirname(__file__), "test_output")

    def tearDown(self):
        # Clean up the output directory after each test
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_create_html_from_file(self):
        # Create the input file
        input_file = os.path.join(os.path.dirname(__file__), "test_input.txt")
        with open(input_file, "w") as f:
            f.write("This is a test.")

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Create the expected output file
        expected_output_file = os.path.join(self.output_dir, "test_input.html")
        with open(expected_output_file, "w") as f:
            f.write(
                "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\"/>\n</head>\n<body>\n<p>This is a test.</p>\n</body>\n</html>"
            )

        # Run the function
        create_html_from_file(input_file, self.output_dir)

        # Check the output file
        with open(expected_output_file, "r") as f:
            expected_output = f.read()
        with open(expected_output_file, "r") as f:
            actual_output = f.read()

        self.assertEqual(expected_output, actual_output)

    def test_create_html_from_file_empty_input(self):
        # Test when the input file is empty.
        # The output HTML file should also be empty.
        input_file = os.path.join(os.path.dirname(__file__), "test_empty_input.txt")
        expected_output_file = os.path.join(self.output_dir, "test_empty_input.html")
        with open(input_file, "w") as f:
            f.write("")

        create_html_from_file(input_file, self.output_dir)

        with open(expected_output_file, "r") as f:
            expected_output = f.read()
        with open(expected_output_file, "r") as f:
            actual_output = f.read()

        self.assertEqual(expected_output, actual_output)

    def test_create_html_from_file_missing_file(self):
        # Test when the input file does not exist.
        # The function should raise a FileNotFoundError.
        input_file = os.path.join(os.path.dirname(__file__), "non_existent_file.txt")
        with self.assertRaises(FileNotFoundError):
            create_html_from_file(input_file, self.output_dir)

    def test_create_html_from_file_malformed_input(self):
        # Test when the input file contains invalid content.
        # The function should handle malformed input gracefully.
        input_file = os.path.join(os.path.dirname(__file__), "test_malformed_input.txt")
        expected_output_file = os.path.join(self.output_dir, "test_malformed_input.html")
        with open(input_file, "w") as f:
            f.write("This is not valid HTML content.")

        create_html_from_file(input_file, self.output_dir)

        with open(expected_output_file, "r") as f:
            expected_output = f.read()
        with open(expected_output_file, "r") as f:
            actual_output = f.read()

        self.assertEqual(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()
