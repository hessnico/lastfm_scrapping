import sys
import os.path
import modules 

def get_last_line_log_last_page_overwrite():
    last_line = ''
    with open('log.log') as f:
        last_line = f.readlines()[-2][-4:]
    
    last_line = int(last_line)
    print(f"    Last extracted page was {last_line}")
    print(type(last_line))
    print(f"Returning line to be extracted {(last_line - 1)}") 

    return (last_line -1)

def create_nec_files(user):
    lst = ['./log.log', './raw_exported_data/out.csv']
    if os.path.getsize(lst[0]) == 0:
        for val in lst:
            print(f"    Creating {val} file")
            fp = open(val, "w")
            fp.close()
        return modules.get_last_library_page(user)
    else:
        last_l = get_last_line_log_last_page_overwrite()
        print(f"    {lst[0]} already exists in folder.")
        print(f"    {lst[1]} already exists in folder.")
        print("    Since the extraction has already begun, starting at the end point.")
        return last_l

def get_username():
    user = input("Insert lastfm username: ")
    print(f"lastfm username: {user}")

    return user

def write_log():
    log = open(f"log.log", "a")
    sys.stdout = log