#!/usr/bin/env python3 -W ignore
# (Aarav Pal, 2024)

# Import
import sys
import getopt
from tika import parser


def help():
    print(sys.stderr, '''
    This program takes in a jpeg image of medical prescription 
    and it extract the medication names from it.
    
    To execute the code run following 
    python3 extract_medicine_name [-i <input filename>] [-h]
    or 
    ./extract_medicine_name [-i <input filename>] [-h]
    ''')
    sys.exit(0)


def usage():
    print(sys.stderr, '''
    Usage:
    python3 extract_medicine_name [-i <input filename>] [-h]
    or 
    ./extract_medicine_name [-i <input filename>] [-h]
    
    where 
    '-i' option is to get the input filename which needs to be OCR'd 
    and 
    '-h' is for help 
    ''')
    sys.exit(1)


# C style command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:h')
except getopt.GetoptError:
    usage()

optdict = dict(opts)

if '-h' in optdict:
    help()

# Check if input filename is present or not
if '-i' not in optdict:
    usage()
else:
    # Input filename along with its extension
    parsed = parser.from_file(optdict['-i'])

    # Extract content from the document
    parsed_lines = parsed["content"].split('\n')

    # We eyeballed the pdf/jpeg file and realized that medicine names start after "S.No"
    # Created a program which searches for the S.NO
    counter = 0
    print("\n\nNumber of lines in the document ", str(len(parsed_lines)))
    for itr in range(0, len(parsed_lines)):
        counter += 1
        # Split each line into words by using " " as delimiter
        words = parsed_lines[itr].split(' ')
        if words[0] == "S.NO":
            break

    print("Table Header S.No. exist at line ", str(counter-1))

    cnt = 0
    medicine = {}
    while True:
        words = parsed_lines[counter].split(' ')

        # Test first value is numeric
        if parsed_lines[counter] != '':
            medicine[cnt] = words[0] + " " + words[1] + " " + words[2]
            cnt += 1
            counter += 1
        else:
            break

    print("\n\nThere are following medications in the input file \n \n")

    # Write out the name of medications
    cnt = 1
    for key in medicine:
        print(str(cnt) + "\t" + medicine[key])
        cnt += 1

    stop = 0

    # Now take medicine name from dictionary medicine and search web.
