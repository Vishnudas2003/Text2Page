# Text2page

**Text2page** is a Python command-line tool that simplifies the process of converting plain text files (.txt) into well-structured HTML documents. It intelligently parses your text, identifies paragraphs, and generates valid HTML5 files, making it easy to turn your text-based content into web-ready pages.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Contributing](#contributing)

## Installation

Before using **Text2page**, make sure you have Python 3 installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## Prerequisites

Before using **Text2page**, make sure you have Python 3 installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Vishnudas2003/Text2Page.git

   ```

2. **Navigate to the project directory**

   ```bash
   cd text2page

   ```

3. Create a folder named **textFiles** in the project directory and place your .txt files inside it. This is where your input files will be located.

## Usage
### Basic Usage

**To convert a single .txt file to HTML, use the following command:**

```bash
python text2page.py /path/to/your/file.txt
```
 Replace /path/to/your/file.txt with the actual path to your .txt file.
 To convert all .txt files within a directory, use:

 ```bash
python text2page.py /path/to/your/directory
```
This command will process all .txt files within the specified directory.

## Markdown Feature
Text2page includes support for Markdown. It can convert Markdown (.md) files to HTML. Simply provide a Markdown file as input, and Text2page will generate an HTML file with the same content.

```bash
python text2page.py /path/to/your/file.md
```
Replace /path/to/your/file.md with the actual path to your .md file.

### Specifyig Output Directory
By default, Text2page will create an output directory named til in the project directory. You can specify a different output directory using the --output or -o flag. For example:

```bash
python text2page.py /path/to/your/directory -o /path/to/output
```
This command will store the generated HTML files in the /path/to/output directory.

### Version Information
To check the version of Text2page, use the --version or -v flag:

```bash
python text2page.py --version
```

## Features
### Horizontal Rules

Text2page now supports horizontal rules in Markdown. To create a horizontal rule, use three or more hyphens, asterisks, or underscores, separated by spaces (e.g., ---, ***, or ___) in your Markdown content. When Text2page encounters a horizontal rule in the Markdown content, it will replace it with an HTML <hr> tag.

#### Example
Input Markdown:

This is some text above the horizontal rule.

---

And this is some text below the horizontal rule.

### Inline Code Blocks
Text2page now supports inline <code> blocks in Markdown. You can enclose text in single backticks (`) to render it as <code>...text...</code> in the HTML output. For example, `code` will become <code>code</code> in the generated HTML.

```bash
Here is an example of inline code: `code`.
```

To convert a .md file with inline code to HTML, use the following command:

code: `hello world`

```bash
python text2page.py /path/to/your/file.md
```

### Help and Usage Information
To view the help and usage information, use the --help or -h flag:

```bash
python text2page.py --help
```

## Credits

- **Inspiration**: This tool was inspired by the need to convert text documents to web-friendly HTML.
- **Python Community**: Thanks to the Python community for creating argparse and other helpful libraries.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions to Text2page are welcome! If you'd like to contribute, please fork the repository and create a pull request.
