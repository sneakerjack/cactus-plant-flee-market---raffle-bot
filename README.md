# cactus-plant-flee-market---raffle-bot

## Overview
This script, `entry.py`, is designed to automate raffle entries by submitting email addresses with randomly selected sizes using provided proxy servers.

## Prerequisites
Make sure you have the following installed before running the script:
- Python 3.x
- Required dependencies (listed in `requirements.txt` if applicable)

## Installation
1. Clone this repository or download the script.
2. Navigate to the script's directory:
   ```bash
   cd path/to/directory
   ```
3. Install dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using the following command:
```bash
python entry.py
```

## Adding Entries
### Adding Emails
To add emails, edit `emails.txt` and enter one email per line. Example:
```
example1@gmail.com
example2@yahoo.com
example3@outlook.com
```

### Adding Proxies
To use proxies, edit `proxy.txt` and enter one proxy per line in the format `IP:PORT:USERNAME:PASSWORD`. Example:
```
192.168.1.1:8080:user:pass
203.0.113.5:3128:user:pass
```

## How It Works
- The script reads all emails from `emails.txt`.
- It picks a random size from a predefined list.
- A random proxy is selected from `proxy.txt` for each request.
- The script submits the entry using the chosen email, size, and proxy.

## Features
- Automates raffle entries with multiple emails.
- Uses proxies for anonymity.
- Randomly selects sizes for variety.
- Logs successful and failed entries.

## Troubleshooting
If you encounter any issues, check the following:
- Ensure all dependencies are installed.
- Verify Python version compatibility.
- Check if `emails.txt` and `proxy.txt` contain valid entries.

## License
This project is licensed under the MIT License.

## Donations
If you find this project helpful, consider supporting me:

SOL - GsXfuEUCd2qcQZv4YRJP5sq6P2T2MMHPj8MsVdQBDjz4  
ETH - 0x0dD4e1d094C9B64329FF418B6F33ac544e84dEb5  
BTC - bc1qgwh8zlt0w3tez35uxd0frutsathymeytlgs927
