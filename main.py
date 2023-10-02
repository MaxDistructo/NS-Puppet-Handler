from issue import issue_main
from ping import ping_main
import time
import os


while(True):
    ping_main()
    issue_main()
    time.sleep(int(os.environ.get("NS_SLEEP"))*60)