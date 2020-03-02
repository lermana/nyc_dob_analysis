import os, sys


# first, we look to see if `DOB_DATA_DIR` is in the environment
DATA_DIR = os.environ.get("DOB_DATA_DIR")

# if it's not, go to a different directory
if DATA_DIR is None:

    try:
        # change the below line to affect default behavior
        DATA_DIR = os.path.join(
                        os.path.expanduser('~'),
                        "projects", "nyc_dob_analysis", "data")

    except FileNotFoundError:
        print("`DATA_DIR` variable not set up - check `pydob.settings`. Terminating.")
        sys.exit()

DATASET_NAMES = (
        "applications", "permits", "permits_now", 
        "complaints", "violations_dob", "violations_ecb", "expense_actuals"
    )

# get path for DoB file writing
DOB_DIR = os.path.join(DATA_DIR, "dob")

# get URLs for data downloads
BASE_URL = "https://data.cityofnewyork.us/api/views/{}/rows.csv?accessType=DOWNLOAD"

APPLICATIONS_URL = BASE_URL.format("ic3t-wcy2")
PERMITS_URL = BASE_URL.format("ipu4-2q9a")
PERMITS_NOW_URL = BASE_URL.format("rbx6-tga4")
COMPLAINTS_URL = BASE_URL.format("eabe-havv")
VIOLATIONS_DOB_URL = BASE_URL.format("3h2n-5cm9")
VIOLATIONS_ECB_URL = BASE_URL.format("6bgk-3dad")
EXPENSE_ACTUALS_URL = BASE_URL.format("7yay-m4ae")


# DB connection string, and table names
DATABASE = os.path.join(DATA_DIR, "dob_data.db")

# StreetEasy
# learn more at: https://streeteasy.com/blog/data-dashboard/
STREETEASY_URL = "https://streeteasy-market-data-download.s3.amazonaws.com/"
STREETEASY_DIR = os.path.join(DATA_DIR, "streeteasy")

# plotting
nt_blue = os.environ.get("NEWTRAILS_BLUE", "steelblue")
nt_black = os.environ.get("NEWTRAILS_BLACK", "black")
nt_style = os.environ.get("NEWTRAILS_STYLE", "default")
FIGURE_DIR = os.path.join(DATA_DIR, "figures")