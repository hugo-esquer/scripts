# copié depuis une ia
import os
import re

LOG_DIR = "/home/hugo/Documents/log"
MAX_LOG = 5

for log in sorted(os.listdir(LOG_DIR)):
    base_name = os.path.join(LOG_DIR, log)
    if log.endswith(".log"):
        os.system(f"mv {base_name} {base_name}.1")

    elif re.match(r"(.+.\d+)", log):
        name = os.path.splitext(log)
        for i in range(MAX_LOG-1, 0, -1):
            old_name = os.path.join(LOG_DIR, f"{name[0]}.{i}")
            new_name = os.path.join(LOG_DIR, f"{name[0]}.{i+1}")
            if os.path.exists(old_name):
                os.system(f"mv {old_name} {new_name}")

#print resutl
print(sorted(os.listdir(LOG_DIR)))


