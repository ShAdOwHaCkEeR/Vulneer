
import argparse
from datetime import datetime
from CVE_CHECK import check
now = datetime.now()

def Parsed_Args():

    DEFAULT = now.strftime("PARSED~%m-%d-%Y~%H:%M:%S")
    parser = argparse.ArgumentParser(description=" [*] CVE Parser [*] ")
    parser.add_argument("-f", "--file", type=str, required=True, help="\t| file to read from (data to parse) \nEX:\t [---.py -f/--file my_results.py].")
    parser.add_argument("-s", "--save", type=str, required=False, default=DEFAULT, help="\t| choose file to save data in.")

    args = parser.parse_args()

    return args

def selector(file_name, save_file):
    CVELST = []

    with open(file_name, "r") as CVEf:
        lines = CVEf.readlines()
        for line in lines:
            line = line.rstrip('\n')
            if "CVE" in line:
                index = line.find("CVE")
                end = index + 13
                item = line[index:end]
                if item in CVELST:
                    pass
                else:
                    CVELST.append(item)
            else:
                pass

    # CHECK
    for i in CVELST:
        response = check(i)
        if response == True:
            pass
        if response == False:
            CVELST.remove(i)

    with open(save_file, "w") as SVF:
        for i in CVELST:
            SVF.write(i+"\n")

    return True


if __name__ == '__main__':
    args = Parsed_Args()
    ffile = args.file
    sfile = args.save
    selector(ffile, sfile)