import utils as u
import config as cf 
import modules as md
import datetime

u.write_log()

start = datetime.datetime.now()
print(f"Extraction started at {start}")
u.create_nec_files()
user = u.get_username()

last_page = md.get_last_library_page(user)

cf.import_cookies_headers()

md.get_last_library_page(user = user)

for idx in range(last_page, last_page-100, -1):
    print(f"Scrapping page {idx}...")
    now = datetime.datetime.now()
    print(f"    Started at {now}")

    md.write_csv(md.get_soup(idx, user))

    later = datetime.datetime.now()
    print(f"    Finished at {later} \n      Time: {later-now}")

end = datetime.datetime.now()
print(f"Extraction ended at {end}")
print(f"    Time for extraction: {end - start}")