import os
import unittest
import shutil
from text2page import process_input

class TestOutputDirectoryCreation(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or common resources 
        self.output_dir = os.path.join(os.path.dirname(__file__), "test_output")

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_output_directory_creation(self):
        # Test creating the output directory when it doesn't exist
        input_file = os.path.join(os.path.dirname(__file__), "test_files", "sample_text.txt")
        output_dir = self.output_dir
        stylesheet_url = None  # Replace with an actual URL if needed

        # Your test logic for process_input with a file
        process_input(input_file, output_dir, stylesheet_url)

        # Verify that the output directory is created
        self.assertTrue(os.path.exists(output_dir), "Output directory does not exist")

if __name__ == "__main__":
    unittest.main()
