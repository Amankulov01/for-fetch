# HTTP Endpoint Health Checker

## Overview
This simple Python script checks the health of specified HTTP endpoints and logs the availability percentages for each domain. It reads endpoint configurations from a YAML file, tests the health every 15 seconds, and displays cumulative availability percentages.

## Usage
1. Ensure you have Python installed.
Install required libraries: requests and pyyaml. Run pip install requests pyyaml in your terminal.
2. Configuration File:
Create a YAML file with your HTTP endpoint details.
Each entry in the YAML list should have a name, URL, and optional fields like method, headers, and body.
3. Run the Script:
Execute the script by running python health_checker.py in your terminal.
When prompted, enter the path to your YAML configuration file.
4. Observing Results:
The script will continuously check the health of endpoints.
After each test cycle, it logs the availability percentage for each domain to the console.
4. User Exit:
To stop the script, press Ctrl+C in the terminal.
## Example Output
```bash
fetch.com has 33% availability percentage
www.fetchrewards.com has 100% availability percentage
fetch.com has 67% availability percentage
www.fetchrewards.com has 50% availability percentage
```
## Notes
- The script rounds availability percentages to the nearest whole number.
- You may customize the YAML file for different endpoints.
## Dependencies
- Python 3
- Required Python libraries: 'requests', 'pyyaml'
