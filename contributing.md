# Contributing to Text2page

Thank you for your interest in contributing to Text2page. We welcome contributions from the community to help improve our project. Please take a moment to read through this document to understand how you can contribute effectively.

## Table of Contents
- [Setting up the Development Environment](#setting-up-the-development-environment)
- [How to Contribute](#how-to-contribute)
- [Reporting Issues](#reporting-issues)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Improving Documentation](#improving-documentation)
- [Providing Feedback](#providing-feedback)
- [Code of Conduct](#code-of-conduct)
- [Testing](#testing)

## Setting up the Development Environment

To get started with development on Text2page, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Vishnudas2003/Text2Page.git

2. Create a folder named textFiles in the project directory and place your .txt files inside it. This is where your input files will be located.

## How to Contribute

Contributions to Text2page can take several forms, including but not limited to:

### Reporting Issues

If you encounter any bugs or other problems with Text2page, please [open an issue](https://github.com/Vishnudas2003/Text2Page/issues)
We welcome contributions from the community to help improve Text2page. If you are interested in contributing to Text2page, please follow these steps:

### Submitting Pull Requests

If you'd like to contribute code to the project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the master branch.
3. Make your changes.
4. Commit your changes and push your branch to GitHub.
5. Open a pull request from your branch to the master branch of the Text2page repository.

### Adding Code Formatting (Black) and Static Analysis (Flake)

We've recently introduced two essential tools to enhance the code quality and maintain consistency within the Text2page project.

**Black**: We have integrated Black, a powerful code formatter for Python, to ensure that our codebase is consistently well-formatted. Black helps maintain code readability and adherence to Python style guidelines. Setting up Black is straightforward. Ensure you have it installed:
   
   ```bash
   pip install black
   ```
Before submitting any code changes, it's important to run Black on your Python files. You can do this by executing the following command in your project directory:

   ```bash
   black .
   ```
This will automatically format your code according to Black's style guidelines.

**Flake8**: For static code analysis and style checking, we've incorporated Flake8. Flake8 is a helpful tool that identifies potential issues in your code, including style violations and common programming mistakes. It enforces adherence to PEP 8 guidelines and can significantly improve code quality. To set up Flake8, install it using:

   ```bash
   pip install flake8
   ```
Before submitting your code changes, it's essential to run Flake8 to identify and address any style or quality issues in your Python code. You can run Flake8 with the following command:

   ```bash
   flake8 .
   ```
Address any issues reported by Flake8 to maintain high code quality standards.

By integrating Black for code formatting and Flake8 for static analysis, we aim to ensure that Text2page's codebase remains clean, consistent, and easy to maintain. These tools not only enhance the project's quality but also make it easier for contributors to collaborate effectively.

## Testing

Text2page relies on automated tests to ensure code quality and functionality. Before contributing, please take note of the following testing information:

### Existing Testing Files

We have two main testing files in the project:

1. **`test_create_html.py`**: This file contains tests for the `create_html_from_file` function. It covers various scenarios, including different file types, empty input, missing files, and malformed input.

2. **`test_core_functionality.py`**: This file tests the core functionality of the Text2page tool, including processing both individual files and entire directories. It ensures that the tool behaves as expected in different situations.

### Running Tests

Before submitting your pull request, make sure to run the existing tests:

```bash
python -m unittest

### Improving Documentation

We appreciate contributions to our documentation. If you find areas that need improvement, please submit a pull request with your proposed changes.
```
### Providing Feedback

If you have suggestions or feedback for the project, please feel free to contact us or discuss it in our community forums.

#### Note: This CONTRIBUTING.md file is a work in progress, and we will be adding more details in future updates.

```
You can save this content in a file named `CONTRIBUTING.md` in the root of your project, as instructed. This file provides clear instructions for potential contributors on how to set up the development environment, report issues, submit pull requests, improve documentation, and follow the project's code of conduct. It's important to keep this document up to date as your project evolves.
```