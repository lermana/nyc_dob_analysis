import sqlite3
import pandas as pd
from functools import wraps

from .settings import DATABASE
from  . import wrangle


def get_conn():
    return sqlite3.connect(DATABASE,
                           detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES
                        )


def df_to_db(df, name, if_exists="replace"):
    with get_conn() as conn:
        df.to_sql(name, conn, index=False, if_exists=if_exists)


def get_query_as_df(query):
    with get_conn() as conn:
        df = pd.read_sql(query, conn)

    return df


def get_table(table_name, cat_cols=None, filter_date_col=None, filter_year=None):
    print(f"Reading {table_name} from database.")
    df = get_query_as_df(f"select * from {table_name}")

    if filter_date_col is not None and filter_year is not None:
        df = df.loc[df[filter_date_col] >= filter_year, :]

    if cat_cols is not None:
        df = wrangle.convert_cols_to_categorical(df, cat_cols)

    return df


def get_applications(filter_year=None):
    return get_table(
                table_name="applications",
                cat_cols=wrangle.applications_cols_to_cat(),
                filter_date_col="pre_filing_date_year",
                filter_year=filter_year)


def get_permits(filter_year=None):
    return get_table(
                table_name="permits",
                cat_cols=wrangle.permits_cols_to_cat(),
                filter_date_col="issuance_date_year",
                filter_year=filter_year
            )


def get_permits_now(filter_year=None):
    return get_table(
                table_name="permits_now",
                cat_cols=wrangle.permits_now_cols_to_cat(),
                filter_date_col="issued_date_year",
                filter_year=filter_year
            )


def get_complaints(filter_year=None):
    return get_table(
                table_name="complaints",
                cat_cols=wrangle.complaints_cols_to_cat(),
                filter_date_col="date_entered_year",
                filter_year=filter_year
            )


def get_violations_dob(filter_year=None):
    return get_table(
                table_name="violations_dob",
                filter_date_col="issue_date_year",
                filter_year=filter_year
            )


def get_violations_ecb(filter_year=None):
    return get_table(
                table_name="violations_ecb",
                cat_cols=wrangle.violations_ecb_cols_to_cat(),
                filter_date_col="issue_date_year",
                filter_year=filter_year
            )


def get_expense_actuals(filter_year=None):
    return get_table(
                table_name="expense_actuals",
                filter_date_col="fisc_yr",
                filter_year=filter_year
            )

def streeteasy_wrapper(func):

    @wraps(func)
    def inner(area_name=None, only_price_col=True):
        dataset_name = func()
        df = get_table(dataset_name)
        df = df.set_index(
                        ["area_name", "year", "month"]
              ).sort_index()

        if area_name:
            df = df.loc[area_name]

        if only_price_col:
            df = df.iloc[:, 0]

        return df

    return inner


@streeteasy_wrapper
def get_streeteasy_sales(area_name=None, only_price_col=True):
    return "streeteasy_sales"


@streeteasy_wrapper
def get_streeteasy_rent(area_name=None, only_price_col=True):
    return "streeteasy_rent"