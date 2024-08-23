# Deepan's Regression Tool

## Overview

Deepan's Regression Tool is designed to automate regression testing by running commands specified in an Excel file and logging the results. This tool is especially useful for managing large-scale testing environments where multiple test cases need to be executed and monitored.

## Features

- Executes commands specified in an Excel file.
- Logs the results of each command.
- Handles various error scenarios and retries failed commands.
- Updates the Excel file with the status of each command.

## License

This tool is licensed under the GNU General Public License v3.0. For more details, visit: [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Installation

To use this tool, install it via pip:

```sh
pip3 install deepan_regression_tool
Prerequisites
Python >=3.9
openpyxl
Usage
Importing the Module
After installation, you can import the module as follows:

from deepan_regression_tool import *
Running Regression
To run the regression, use the run_regression function provided by the module.

from deepan_regression_tool import *

# Example usage
deepan_regression_tool.run_regression(4, 'path/to/your/excel_file.xlsx', 'path/to/regression_dir')
Function Descriptions
run_regression(no_of_cores, xl_file_name, regression_dir_name)
no_of_cores: Number of cores to be used for the regression.
xl_file_name: Path to the Excel file containing the commands.
regression_dir_name: Path to the directory where regression results should be stored.
This function reads the commands from the specified Excel file, executes them, and logs the results.

Fair Use
This tool is provided as-is under the GNU General Public License v3.0. You are free to use, modify, and distribute this tool, provided that you adhere to the terms of the license. For more details, visit: GNU GPL v3.0.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

Contact
For questions or suggestions, please open an issue on the GitHub repository.
