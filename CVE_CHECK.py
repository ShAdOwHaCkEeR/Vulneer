

import vulners
from API import API_key

KEY = API_key()
VSAPI = vulners.Vulners(api_key=KEY)

def check(cve):

    data = VSAPI.document(cve)
    if len(data) > 5:
        return True
    if len(data) < 5:
        return False