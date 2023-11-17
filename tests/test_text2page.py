import os
import unittest
import shutil
from text2page import process_input

class TestText2Page(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or common resources
        self.output_dir = os.path.join(os.path.dirname(__file__), "test_output")

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_convert_sample_text_to_html(self):
        # Test converting a sample text file to HTML
        input_file = os.path.join(os.path.dirname(__file__), "test_files", "sample_text.txt")
        output_dir = self.output_dir
        stylesheet_url = None  # Replace with an actual URL if needed

        # Your test logic for process_input with a file
        process_input(input_file, output_dir, stylesheet_url)

        # Verify that the output directory is created
        self.assertTrue(os.path.exists(output_dir), "Output directory does not exist")

        # Verify that the output file is created
        expected_output_file = os.path.join(output_dir, "sample_text.html")
        self.assertTrue(os.path.exists(expected_output_file), "Output file does not exist")

        # Read the content of the generated HTML file
        with open(expected_output_file, "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        # Add assertions to check the content of the HTML file in a case-insensitive manner
        expected_header = "<h1>Sample_Text</h1>"
        self.assertIn(expected_header.lower(), html_content.lower(), f"{expected_header.lower()} not found in HTML content")

if __name__ == "__main__":
    unittest.main()
