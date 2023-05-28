import sys

def create_nec_files():
    lst = ['log.log', './raw_exported_data/out.csv']
    for val in lst:
        fp = open(val, "w")
        fp.close()

def get_username():
    user = input("Inser lastfm username: ")
    print(f"lastfm username: {user}")

    return user

def write_log():
    log = open(f"log.log", "a")
    sys.stdout = log