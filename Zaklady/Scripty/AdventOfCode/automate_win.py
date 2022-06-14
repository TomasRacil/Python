"""
WIP automatizace aoc
"""

import os
from datetime import datetime

USER = "Racil"

now = datetime.now()
directory = os.path.dirname(__file__) + "\\"
print(directory + str(now.year))
if not os.path.exists(directory + str(now.year)):
    os.mkdir(directory + str(now.year))
if not os.path.exists(directory + str(now.year) + "\\" + USER + "\\" + str(now.day)):
    os.mkdir(directory + str(now.year) + "\\" + USER + "\\" + str(now.day))
else:
    print("all exists")
    # with open(dir+'win_test.txt','a') as f:
    #     f.write("jou jou")
# working_directory = os.getcwd()
