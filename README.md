# python-utils-91

A collection of Python utility functions designed to simplify and enhance everyday programming tasks. From handling file operations to formatting strings, this library aims to provide lightweight, reusable tools for developers.

## Features

- **File Handling:** Easily read, write, and manipulate files with built-in methods to streamline common file operations.
- **String Formatting:** Simplify string manipulation with versatile functions for trimming, padding, and formatting strings.
- **Data Validation:** Quickly validate input data types, formats, and structures, helping reduce the likelihood of runtime errors.
- **Date and Time Utilities:** Simplify date and time manipulations, including parsing, formatting, and arithmetic operations.

## Installation

To install `python-utils-91`, you can use pip. Open your terminal and run:

```bash
pip install python-utils-91
```

If you prefer to clone the repository directly, you can do so with the following command:

```bash
git clone https://github.com/yourusername/python-utils-91.git
cd python-utils-91
```

Then install the required packages with:

```bash
pip install -r requirements.txt
```

## Basic Usage

Here is a simple example demonstrating how to use some of the utility functions:

```python
from python_utils import FileUtils, StringUtils, DateUtils

# Using FileUtils to read a file
content = FileUtils.read_file('example.txt')
print(content)

# Using StringUtils to format a string
formatted_string = StringUtils.format_string("Hello {name}", name="World")
print(formatted_string)

# Using DateUtils to get today's date in a specific format
today = DateUtils.get_today_formatted("%Y-%m-%d")
print(f"Today's date is: {today}")
```

## License

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.