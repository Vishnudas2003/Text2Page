import argparse
import os
import shutil

# Define the version number
VERSION = "1.0.0"  # Replace with your actual version number

def create_html_from_txt(input_file, output_dir):
    # Read the content of the input .txt file
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        txt_content = txt_file.read()
    paragraphs = txt_content.split('\n\n')
    filename = os.path.basename(input_file).replace('.txt', '')
    html_content = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{filename}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
'''
    for paragraph in paragraphs:
        html_content += f'  <p>{paragraph}</p>\n'
        html_content += '</body>\n</html>\n'
    os.makedirs(output_dir, exist_ok=True)

    # Determine the output HTML file path
    output_file = os.path.join(output_dir, f'{filename}.html')

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f'Converted {input_file} to {output_file}')

def process_input(input_path, output_dir):
    if os.path.isfile(input_path) and input_path.endswith('.txt'):
        create_html_from_txt(input_path, output_dir)
    elif os.path.isdir(input_path):
        process_directory(input_path, output_dir)
    else:
        print(f"Error: {input_path} is not a valid .txt file or directory.")

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.txt'):
                create_html_from_txt(os.path.join(root, file), output_dir)

def main():
    parser = argparse.ArgumentParser(description='Process .txt files to .html with Text2page')
    parser.add_argument('path', nargs='?', help='path to the file or folder to be processed')
    parser.add_argument('--version', '-v', action='store_true', help='print the tool\'s name and version')
    parser.add_argument('--output', '-o', default='./text2page', help='Specify a different output directory (default: ./text2page)')

    args = parser.parse_args()

    if args.version:
        print("Text2page Tool Version", VERSION)
        return

    if not args.path:
        parser.error("the following arguments are required: path")
        return

    if not os.path.exists(args.path):
        print(f"Error: {args.path} does not exist.")
        return

    # Remove the existing 'text2page' folder if it exists
    if os.path.exists(args.output):
        shutil.rmtree(args.output)

    process_input(args.path, args.output)

if __name__ == "__main__":
    main()
