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
```
## Prerequisites
•	Python >=3.9
•	openpyxl
•	Linux operating system

## Usage
Importing the Module
After installation, you can import the module as follows:
```python
from deepan_regression_tool import *
```
## Running Regression
To run the regression, use the run_regression function provided by the module.

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Managed Regression",
        epilog=HELP_MESSAGE,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('--no_of_cores', '-no_of_cores', type=int, required=True, help="Number of cores to use for the regression.")
    parser.add_argument('--pathsel_widths', '-pathsel_widths', type=int, nargs='+', required=True, help="Widths for path selection.")
    parser.add_argument('--delaysel_widths', '-delaysel_widths', type=int, nargs='+', required=True, help="Widths for delay selection.")
    parser.add_argument('--json', '-json', type=str, required=True, help="Path to the JSON configuration file.")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        #print(HELP_MESSAGE)
        sys.exit(1)

    args = parser.parse_args()

    no_of_cores = args.no_of_cores
    pathsel_widths = args.pathsel_widths
    delaysel_widths = args.delaysel_widths
    json_file_name = args.json
    random_sel_values = [0,1]
    funclk_freq = [1.0,2.0,3.0]

    # Ensure the json argument is provided
    if not args.json:
        print("Error: --json argument is required")
        print(HELP_MESSAGE)
        sys.exit(1)

    file = open("test.txt",'w')
    file.close()
    file = open("compile.txt",'w')
    file.close()
    file = open("log.txt",'w')
    file.close()
    xl_file_name,regression_dir_name = gen_xl(json_file_name,no_of_cores,pathsel_widths,delaysel_widths,funclk_freq,random_sel_values)
    run_regression(no_of_cores,xl_file_name,regression_dir_name,timeout)
    regression_analyze(no_of_cores,xl_file_name)

```

## Fair Use
This tool is provided as-is under the GNU General Public License v3.0. You are free to use, modify, and distribute this tool, provided that you adhere to the terms of the license. For more details, visit: GNU GPL v3.0.

## Contact
For questions or suggestions, please open an issue on the GitHub repository.
