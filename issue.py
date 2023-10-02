import sans
import json
import random
import os
import time
import xml.etree.ElementTree as ET


def issue_main():
    # api = nationstates.Nationstates(os.environ.get("NS_ISSUE_UA"), "Puppet Issue Answerer")
    sans.set_agent(os.environ.get("NS_ISSUE_UA", "NS-Puppet-Handler - Issue Handler - User has not claimed this script usage"))
    puppets = ""
    RATELIMIT_NUM = 50
    RATELIMIT_SEC = 30
    ratelimit = 0

    with open("puppets.json") as f:
        puppets = json.loads(f.read())

    # Each val is the key in the dict
    for user in puppets:
        #print(user)
        if (ratelimit + 3) >= RATELIMIT_NUM:
            time.sleep(RATELIMIT_SEC)
            ratelimit = 0
        auth = sans.NSAuth(password=puppets[user])
        # nation = api.nation(user, password=puppets[user])
        ratelimit = ratelimit + 1
        # JSON of all issues
        rawxml = sans.get(sans.Nation(user, "issues"), auth=auth).xml
        print(ET.tostring(rawxml, encoding="unicode"))
        ratelimit = ratelimit + 1
        ids = {}
        for issue in rawxml.iter("ISSUE"):
            option_arr = []
            # print(issue.get("id"))
            for option in issue.findall("OPTION"):
                option_arr.append(option.get("id"))
            ids[issue.get("id")] = option_arr
        print(ids)
        if len(ids) > 0:
            issue_to_answer = list(ids.keys())[random.randint(0, (len(ids.keys()) - 1))]
            print(f"{issue_to_answer}, Answer {random.randint(0, len(ids[issue_to_answer]) - 1)}")
            sans.post(sans.Nation(user, "issue", c='issue', issue=str(issue_to_answer),
                                  option=str(random.randint(0, len(ids[issue_to_answer]) - 1))), auth=auth)
            ratelimit = ratelimit + 1
        else:
            sans.get(sans.Nation(user, "ping"), auth=auth)

            ratelimit = ratelimit + 1


if __name__ == "__main__":
    issue_main()
