import os


class Bcolors:
    HEADER = '\033[95m' #if os.name == "posix" else ''
    OKBLUE = '\033[94m' #if os.name == "posix" else ''
    OKCYAN = '\033[96m' #if os.name == "posix" else ''
    OKGREEN = '\033[92m' #if os.name == "posix" else ''
    WARNING = '\033[93m' #if os.name == "posix" else ''
    FAIL = '\033[31m' #if os.name == "posix" else ''
    ENDC = '\033[0m' #if os.name == "posix" else ''
    BOLD = '\033[1m' #if os.name == "posix" else ''
    UNDERLINE = '\033[4m' #if os.name == "posix" else ''