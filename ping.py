import sans
import json
import os
import time

def ping_main():
    sans.set_agent(os.environ.get("NS_CTE_UA", "Unregistered Anti-CTE Script"))
    #api = nationstates.Nationstates(os.environ.get("NS_CTE_UA"), "Anti-CTE")
    puppets = ""
    RATELIMIT_NUM = 50
    RATELIMIT_SEC = 30
    ratelimit = 0

    with open("cte.json") as f:
        puppets = json.loads(f.read())

    #Each val is the key in the dict
    for user in puppets:
        print(user)
        if((ratelimit + 2) >= RATELIMIT_NUM):
            time.sleep(RATELIMIT_SEC)
            ratelimit = 0
        auth = sans.NSAuth(password=puppets[user])
        sans.get(sans.Nation(user, "ping"), auth=auth)
        ratelimit = ratelimit + 2

if __name__ == "__main__":
    ping_main()
