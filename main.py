from domain_checker3000 import fileReader, domainChecker
from screenshots import Screenshot
import sys
import os

if __name__ == "__main__":
    # Initialize the file reader with the CSV file path and the column name
    if len(sys.argv) != 4:
        print("Usage: python main.py <file_path> <from_row> <to_row>")
        sys.exit(1)
    # Check if screenshots directory exists
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    from_row = int(sys.argv[2])
    to_row = int(sys.argv[3])
    file_path = sys.argv[1]
    column_name = 'Domain'

  
    reader = fileReader(file_path, column_name)

    # Read the domains from the CSV file
    domains = reader.read_csv()
    domains = domains[from_row:to_row]  
    # Initiailize the screenshot taker with the output directory
    screenshot_taker = Screenshot("screenshots")
    

    # Initialize the domain checker with the list of domains
    checker = domainChecker(domains)
   

    # Check which domains are unreachable
    unreachable_domains = checker.check_domains(screenshot_taker)

    # Print the unreachable domains
    print("Row \t\t"+"Unreachable Domains:")
    for domain in unreachable_domains:
        print(domain[1]+from_row, "\t\t", domain[0])
    print ("number of unreachable domains: ", len(unreachable_domains))