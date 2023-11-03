import argparse
import os
import shutil
import sys
import markdown
import re
import tomllib


def generate_html_content(title, content, stylesheet_url=None):
    final_html_content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
</head>
<body>
<h1>{title}</h1>
{content}
</body>
</html>
"""

    return final_html_content


def create_html_from_file(input_file, output_dir, stylesheet_url=None):
    _, extension = os.path.splitext(input_file)
    with open(input_file, "r", encoding="utf-8") as file:
        input_content = file.read()

    if extension.lower() == ".txt":
        parsed_content = input_content
        output_filename = os.path.basename(input_file).replace(".txt", "")
    elif extension.lower() == ".md":
        parsed_content = input_content
        output_filename = os.path.basename(input_file).replace(".md", "")
    else:
        print(f"Unsupported file type: {extension}")
        return

    title = output_filename
    # Convert the Markdown content
    parsed_content = markdown.markdown(
        parsed_content, extensions=["markdown.extensions.fenced_code"]
    )

    final_html_content = generate_html_content(title, parsed_content, stylesheet_url)

    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"{output_filename}.html")

    with open(output_file, "w", encoding="utf-8") as html_file:
        html_file.write(final_html_content)

    print(f"Converted {input_file} to {output_file}")


def process_input(input_path, output_dir, stylesheet_url=None):
    if os.path.isfile(input_path):
        create_html_from_file(input_path, output_dir, stylesheet_url)
    elif os.path.isdir(input_path):
        process_directory(input_path, output_dir, stylesheet_url)
    else:
        print(f"Error: {input_path} is not a valid .txt or .md file or directory.")


def process_directory(input_dir, output_dir, stylesheet_url=None):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".txt"):
                create_html_from_file(
                    os.path.join(root, file), output_dir, stylesheet_url
                )


def main():
    parser = argparse.ArgumentParser(
        description="Process .txt or .md files to .html with Text2page"
    )
    parser.add_argument(
        "path", nargs="?", help="path to the file or folder to be processed"
    )
    parser.add_argument(
        "--version", "-v", action="store_true", help="print the tool's name and version"
    )
    parser.add_argument(
        "--output",
        "-o",
        default="./text2page",
        help="Specify a different output directory (default: ./text2page)",
    )
    parser.add_argument(
        "--stylesheet", "-s", help="URL to a CSS stylesheet for styling the HTML"
    )
    parser.add_argument(
        "--config",
        "-c",
        metavar="<config.toml>",
        help="If you want to use a TOML config file to set the arguments needed for the program",
    )

    args = parser.parse_args()

    if args.version:
        print("Text2page Tool Version 0.02")
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

    if args.config:
        with open(args.config, "rb") as toml_config:
            try:
                toml_dict = tomllib.load(toml_config)
            except tomllib.TOMLDecodeError as err:
                print(f"There was a problem decoding your TOML file: {err}")
                sys.exit(-1)
            try:
                output = toml_dict.get("output", "./text2page")
                stylesheet = toml_dict.get("stylesheet", "./style.css")
            except KeyError as err:
                print(f"Error: {err} was not found in your TOML file")
                sys.exit(-1)
            process_input(args.path, output, stylesheet)
    else:
        process_input(args.path, args.output, args.stylesheet)


if __name__ == "__main__":
    main()
