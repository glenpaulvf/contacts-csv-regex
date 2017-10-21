# Glen Paul Florendo
# COMPTNG16
# October 23, 2017

import csv
import re


def evaluate_phone_number(pn):
    # Checks if phone number has area code
    regex_pn = r"^1?[\-]?\(?(\d{3})\)?[\-\.\s]?(\d{3})[\)\-\.]?(\d{4})"
    return re.search(regex_pn, pn)


def format_name(name):
    # Matches with names formatted as:
    # Lastname, Firstname
    # Lastname, Firstname Middleinitial.
    #
    # Changes name format to:
    # Firstname Lastname
    # Firstname Middleinitial. Lastname
        
    regex_name = r"^([A-Za-z]+),\s([A-Za-z]+)(|\s[A-Za-z]\.)?$"
    name_sub = re.sub(regex_name, r"\2\3 \1", name)
    return name_sub


def format_phone_number(pn):
    # Format phone number to (###) ###-####
    
    regex_pn = r"^1?[\-]?\(?(\d{3})\)?[\-\.\s]?(\d{3})[\)\-\.]?(\d{4})"
    pn_sub = re.sub(regex_pn, r"(\1) \2-\3", pn)
    return pn_sub


# Prompt for csv file
ifile = raw_input("Enter csv filename (example.csv): ");

# Prompt for new csv file name
ofile = raw_input("Enter new csv filename (example2.csv: ");

# Set up writer
ofile = open(ofile, 'w+')
writer = csv.writer(ofile, delimiter=",", quoting=csv.QUOTE_ALL)

# Process file
with open(ifile, 'r') as f:
    reader = csv.reader(f)
    
    # Skip header
    next(reader, None)
    
    # Write new header
    header = ["First", "M.I.", "Last", "Phone"]
    writer.writerow(header)
        
    # Iterate through rows in data
    for row in reader:
        # Filter badly-formatted phone numbers
        if evaluate_phone_number(row[1]) is not None:
            # Format name
            data_name = format_name(row[0])
            
            # Format phone number
            data_phone = format_phone_number(row[1])
            
            # Split name into different fields
            new_row = re.split('\s', data_name)
            
            # Append phone number to end of new row
            new_row.append(data_phone)
            
            # If no middle initial, leave field blank
            if len(new_row) == 3:
                new_row.insert(1, "")
                
            # Write new row to output file
            writer.writerow(new_row)

# Close output file
ofile.close()
        