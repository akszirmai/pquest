import os
import sys

print("Executable:", sys.executable)
print("Version:", sys.version)
print("VIRTUAL_ENV:", os.environ.get("VIRTUAL_ENV"))
print("PATH:", os.environ.get("PATH"))
