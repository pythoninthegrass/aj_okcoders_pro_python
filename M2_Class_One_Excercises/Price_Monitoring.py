# Build a price-monitoring tool that does the following

# Scrapes product rices from a website
# Compares to prices in the given Excel file
# Updates the Excel file with new prices
# Highlights prices changes
# Sends an alert if there is a big price drop

from price_monitoring_helpers import load_excel_file, load_website

def run_program():
    load_website()
    # load_excel_file()

if __name__ == '__main__':
  run_program()