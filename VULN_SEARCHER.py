

import argparse
import vulners
import json
from API import API_key
from datetime import datetime
now = datetime.now()

KEY = API_key()


def Parsed_ARGS():

    DEFAULT = now.strftime("_[%Y-%m-%d]_CVE_%H-%M-%S_.txt")

    parser = argparse.ArgumentParser(description=" [*] Vuln Searcher [*] ")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--cve", type=str, help="\t| choose CVE to search for (data) \nEX:\t [---.py -c/--cve CVE-****-*****].", required=False)
    group.add_argument("-f", "--from-file", type=str, help="\t| choose CVE's from file \nEX:\t [---.py -f/--from-file CVE_lst.txt].", required=False)
    parser.add_argument("-s", "--save-to", type=str, default=DEFAULT, help="\t| choose file to save data in.", required=False)

    args = parser.parse_args()
    return args

def vuln_eer(cve):

    VSAPI = vulners.Vulners(api_key=KEY)
    CVE = VSAPI.document(cve)

    VALID = json.dumps(CVE)
    CVE_DATA = json.loads(VALID)
    CVED = dict()
    CVED["ID"] = CVE_DATA["id"]
    CVED["BIF"] = CVE_DATA["bulletinFamily"]
    CVED["TITLE"] = CVE_DATA["title"]
    CVED["DESC"] = CVE_DATA["description"]
    CVED["DESC"] = str(CVED["DESC"]).replace(".", "\n\t")
    CVED["PDATE"] = CVE_DATA["published"]
    CVED["MDATE"] = CVE_DATA["modified"]
    CVED["SCORE"] = CVE_DATA["cvss"]["score"]
    CVED["VECTOR"] = CVE_DATA["cvss"]["vector"]

    return CVED


def get_cvelst(cvelst_file):

    cvelst = []
    with open(cvelst_file, "r") as clf:
        lines = clf.readlines()
        for line in lines:
            line = line.rstrip('\n')
            cvelst.append(line)

    return cvelst

def save_er(cvelst, datalst, sv_file):

    with open(sv_file, "w") as SVF:
        for i, z in zip(cvelst, datalst):
            SVF.write("\n"+i+"\n"+str(z))

if __name__ == '__main__':

    args = Parsed_ARGS()
    CVE = args.cve
    fromff = args.from_file
    saveff = args.save_to

    if fromff != None:
        save_data = []
        cve_lst = get_cvelst(fromff)
        for i in cve_lst:
            data = vuln_eer(i)
            save_data.append(data)
        save_er(cve_lst, save_data, saveff)
    if CVE != None:
        data = vuln_eer(CVE)
        with open(saveff, "w") as SAVE:
            SAVE.write(CVE+"\n"+data)
    if CVE and fromff == None:
        print("[cve/cve_filelst]: required !!!")
        exit()
       








