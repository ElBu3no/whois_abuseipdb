# IP Info Consultation Tool

This Python script provides functionalities to gather information about IP addresses using various APIs, including geolocation, WHOIS lookup, and abuse checking.

## Features

- **Geolocation Consultation**: Retrieve geolocation information for a given IP address.
- **AbuseIPDB Consultation**: Check if an IP address has been listed as abusive on AbuseIPDB.
- **WHOIS Consultation**: Obtain WHOIS information for an IP address.
- **IPinfo Consultation**: Gather general information about an IP address using the IPinfo API.

## Requirements

- Python 3
- Necessary Python libraries: `requests`, `whois`

## Usage

1. Ensure you have Python 3 installed on your system.
2. Install the required Python libraries using pip: `pip install requests whois`
4. Obtain API keys for the AbuseIPDB API and IPinfo API.
5. Create a file named `ips.txt` containing the list of IP addresses you want to analyze, with each IP address on a new line.
6. Replace the placeholder API keys (`XXXXX`) with your actual API keys in the script.
7. Run the script using the following command: python whois_abuseipdb.py
9. View the results printed in the console.

## Notes

- Make sure to handle API rate limits and usage restrictions according to the terms of service of each API provider.
- For more information about each API and its usage, refer to the respective documentation:
- [AbuseIPDB API Documentation](https://docs.abuseipdb.com/)
- [IPinfo API Documentation](https://ipinfo.io/developers)
