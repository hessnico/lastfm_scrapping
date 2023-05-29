import utils as u
import config as cf 
import modules as md
import datetime

user = u.get_username()

u.write_log()

last_page = u.create_nec_files(user)

start = datetime.datetime.now()
print(f"\nExtraction started at {start}")

print(f"Import config from config.py")
cf.import_cookies_headers()

last_index_searched = 0
try:
        for idx in range(last_page, 0, -1):
                print(f"Scrapping page {idx}...")
                now = datetime.datetime.now()
                print(f"    Started at {now}")

                md.write_csv(md.get_soup(idx, user))

                later = datetime.datetime.now()
                print(f"    Finished at {later} \n      Time: {later-now}")
                last_index_searched = idx

                end = datetime.datetime.now()
                print(f"Extraction ended at {end}")
                print(f"    Time for extraction: {end - start}")
        print(f"    Stopped at: {last_index_searched}")

except KeyboardInterrupt:
        print(f"    Stopped at: {last_index_searched}")

except UnboundLocalError:
        print(f"    Stopped at: {last_index_searched}")

except Exception as e:
      print(print(str(e)))
