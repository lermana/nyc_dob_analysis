import os
import sys
import shutil
import datetime
import pandas as pd

from .settings import *
from . import database, wrangle, streeteasy


def get_data_from_url(url, read_csv_kwargs):
    return pd.read_csv(url, **read_csv_kwargs)


def get_dob_file_path(dataset_name):
    return os.path.join(DOB_DIR, f"{dataset_name}.csv")


def get_dob_urls():
    all_vars = globals()

    relevant_keys = filter(
                lambda x: x.lower().endswith("url"), all_vars
            )

    return {
                "_".join(k.lower().split("_")[:-1]): all_vars[k]
                for k in relevant_keys
        }


def get_dataset_url(dataset_name):
    return get_dob_urls()[dataset_name]


def get_dob_df(
            dataset_name=None,
            use_existing=False,
            write_to_file=True
        ):

    def conversions_func(df):
        for k, v in conversions.items():
            print(f"\tApplying {v.__name__} to {k}")
            df[k] = v(df[k])

        return df

    path = get_dob_file_path(dataset_name)
    url = get_dataset_url(dataset_name)

    (
        read_csv_kwargs,
        conversions,
        addtnl_wrangle_func,
        addtnl_cols_func,
                            ) = wrangle.get_all_dataset_stuff(dataset_name)

    if use_existing and os.path.exists(path):
        print(f"Reading csv from {path},\n\twith kwargs {read_csv_kwargs}.")
        df = pd.read_csv(path, low_memory=False).iloc[:, 1:]

    else:
        print(f"Retrieving data from {url},\n\twith kwargs {read_csv_kwargs}.")
        df = get_data_from_url(url, read_csv_kwargs)

        if write_to_file is True:
            print(f"Writing data to {path}.")
            df.to_csv(path)

    print("Cleaning column names.")
    df = wrangle.clean_column_names(df)

    for func in (conversions_func, addtnl_wrangle_func, addtnl_cols_func):
        if func.__name__ != "pass_through_func":
            print(f"Running {func.__name__}.")
            df = func(df)

    return df


def get_data_and_push_to_db(
                        dataset_name=None,
                        use_existing=False,
                        write_to_file=True,
                        return_df=False
                    ):
    """
    `dataset_name` must be one of:
        - "applications"
        - "permits"
        - "complains"
        - "violations_dob"
        - "violations_ecb"

    These are listed in `settings.DATASET_NAMES`.

    You can set the `read_csv` behavior, as well as whether any additonal
    columns are created, and other functionality, by editing the relevant
    functions in `pydob.wrangle`.
    """
    if dataset_name not in DATASET_NAMES:
        print("Invalid `dataset_name` passed. Check the docstring.")
        return None

    print(f"\nBuilding table for {dataset_name}")

    print("Getting data.")
    df = get_dob_df(
                dataset_name=dataset_name,
                use_existing=use_existing,
                write_to_file=write_to_file
            )

    print(f"Pushing to table {dataset_name}.")
    database.df_to_db(df, dataset_name)

    if return_df:
        return df


def build_all_dob_tables(use_existing=True, write_to_file=True):
    print(f"Building tables for each of {DATASET_NAMES}.")

    for dataset_name in DATASET_NAMES:
        get_data_and_push_to_db(
                        dataset_name,
                        use_existing=use_existing,
                        write_to_file=write_to_file
                    )


def build_street_easy():
    print(f"\nRetrieving streeteasy data.")
    sales, rent = streeteasy.get_all_data()

    print(f"Building table for streeteasy_sales.")
    database.df_to_db(sales, "streeteasy_sales")

    print(f"Building table for streeteasy_rent.")
    database.df_to_db(rent, "streeteasy_rent")


def user_ok(question_or_comment):
    proceed = None

    while proceed not in ("y", "n"):
        proceed = input(f"{question_or_comment} [y, n] ")
    
    if proceed == "n":
        sys.exit()


def dir_prep(use_existing=False):
    if not os.path.exists(DATA_DIR):
        if not os.environ.get("DOB_DATA_DIR"):
            user_ok(f"""You have not yet set `DOB_DATA_DIR`. This directory houses all data
            needed for the project. The program will default to using:

                - {DATA_DIR}

            is that ok? If not, enter 'n' and set this environment variable to your
            liking. The program will make `DOB_DATA_DIR` if it does not already
            exist.""")

        os.makedirs(DATA_DIR)
    
    if os.path.exists(DATABASE):
        user_ok("This will wipe the existing DB, ok?")
        os.remove(DATABASE)

    dir_dict = {"DOB_DIR": DOB_DIR, "STREETEASY_DIR": STREETEASY_DIR, "FIGURE_DIR": FIGURE_DIR}
    for d in sorted(dir_dict.keys()):
        path = dir_dict[d]

        if os.path.exists(path):
            if use_existing or d == "FIGURE_DIR":
                continue
            else:
                shutil.rmtree(path)

        os.makedirs(dir_dict[d])


def build(use_existing=False):
    now = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S %p")
    print(f"\nBuilding all data at {now}.")

    dir_prep(use_existing=use_existing)
    build_all_dob_tables(use_existing=use_existing)
    build_street_easy()

    now = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S %p")
    print(f"\nProgram complete at {now}.\n")