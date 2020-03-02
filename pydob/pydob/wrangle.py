import numpy as np
import pandas as pd
from functools import wraps
from multiprocessing.pool import Pool

from . import meta


def pass_through_func():
    return {}


def get_all_dataset_stuff(dataset_name):
    funcs = meta.get_funcs_for_dataset(dataset_name, globals())

    # we call these now
    read_csv_kwargs = funcs.get("read_csv_kwargs", pass_through_func)()
    conversions = funcs.get("conversions", pass_through_func)()

    # and save these for later
    addtnl_wrangle_func = funcs.get("addtnl_wrangle", pass_through_func)
    addtnl_cols_func = funcs.get("addtnl_cols", pass_through_func)

    return (
            read_csv_kwargs,
            conversions,
            addtnl_wrangle_func,
            addtnl_cols_func
        )


def async_wrangler(func):

    @wraps(func)
    def inner(df, *args):
        print(f"\tRunning {func.__name__} (multi-processed).")

        func_to_run, args_to_run  = func(df, *args)

        with Pool() as p:
            r = p.apply_async([
                        func_to_run(df, a)
                        for a in args_to_run
                    ])

        return df

    return inner


def clean_column_names(table):
    table.columns = table.columns.str.replace(r'[^\w\s]','') 
    table.columns = table.columns.str.strip().str.replace(' ','_').str.lower()
    return table


def to_dt_with_coerce(srs):
    return pd.to_datetime(srs, errors="coerce")


def to_dt_with_coerce_and_format(srs):
    return pd.to_datetime(srs, errors="coerce", format="%Y%m%d")


def to_num_with_coerce(srs):
    return pd.to_numeric(srs, errors="coerce", downcast="unsigned")


def inplace_to_num_with_coerce(df, col):
    df[col] = pd.to_numeric(df[col], errors="coerce", downcast="unsigned")


@async_wrangler
def downcast_all_num_cols(df):
    cols = df.select_dtypes(include=[int, float]).columns
    return inplace_to_num_with_coerce, cols


def inplace_replace_empty_string(df, col):
    df[col] = df[col].str.strip().replace("", np.nan)


@async_wrangler
def replace_all_empty_strings(df):
    cols = df.select_dtypes(include=object).columns
    return inplace_replace_empty_string, cols


def inplace_to_cat(df, col):
    df[col] = pd.Categorical(df[col])


@async_wrangler
def convert_cols_to_categorical(df, cols):
    return inplace_to_cat, cols


def inplace_to_bool(df, args):
    c, true_str_or_func = args

    if isinstance(true_str_or_func, str):
        true_str = true_str_or_func
        df[f"is_{c}"] = df[c].apply(lambda x: True if x == true_str else False)

    else:
        true_func = true_str_or_func
        df[f"is_{c}"] = df[c].apply(true_func)


@async_wrangler
def convert_str_cols_to_bool(df, cols_and_true_strs_or_funcs):
    cols = cols_and_true_strs_or_funcs.items()
    return inplace_to_bool, cols


def get_all_bool_cols(df, cols_and_true_strs_or_funcs):
    df = convert_str_cols_to_bool(df, cols_and_true_strs_or_funcs)
    df = df.drop(cols_and_true_strs_or_funcs.keys(), axis=1)
    return df


def get_get_dt_rollup_srs(srs, time_unit):
    return getattr(srs.dt, time_unit).rename(f"{srs.name}_{time_unit}")


def get_dt_rollup_cols(srs):
    year = get_get_dt_rollup_srs(srs, "year")
    quarter = get_get_dt_rollup_srs(srs, "quarter")
    month = get_get_dt_rollup_srs(srs, "month")

    return pd.concat([year, quarter, month], axis=1)


def make_dt_rollup_cols(df, col):
    return df.join(get_dt_rollup_cols(df[col]))


def clean_site_fill_col(df):
    df.site_fill = df.site_fill.replace(
                                    "NONE", np.nan
                              ).replace(
                                    "NOT APPLICABLE", np.nan)

    return df


def applications_read_csv_kwargs():
    return {
        "low_memory": False
    }


def applications_conversions():
    return {
        "pre_filing_date": pd.to_datetime,
        "paid": pd.to_datetime,
        "fully_paid": pd.to_datetime,
        "assigned": pd.to_datetime,
        "approved": to_dt_with_coerce,
        "fully_permitted": to_dt_with_coerce,
        "latest_action_date": to_dt_with_coerce
    }


def applications_addtnl_cols(df):
    return make_dt_rollup_cols(df, "pre_filing_date")


def applications_cols_to_rename():
    return {
        "ownershouse_street_name": "owners_house_street_name",
        "ownersphone": "owners_phone",
        "existingno_of_stories": "existing_no_of_stories",
        "community__board": "community_board",
        "gis_nta_name": "nta_name"
    }


def applications_cols_to_cat():
    return ("borough", "building_class", "applicant_professional_title",
            "applicant_license", "fee_status", "nta_name", "job_status",
            "job_status_descrp", "job_type", "owner_type", "site_fill",
            "special_action_status", "special_district_1", "special_district_2",
            "state", "zoning_dist1", "zoning_dist2", "zoning_dist3")


def applications_cols_to_bool():
    return {
        "adult_estab": "Y",
        "boiler": "X",
        "building_type": "1-2-3 FAMILY",
        "city_owned": "Y",
        "cluster": "Y",
        "curb_cut": "X",
        "efiling_filed": "Y",
        "equipment": "X",
        "fire_alarm": "X",
        "fire_suppression": "X",
        "fuel_burning": "X",
        "fuel_storage": "X",
        "horizontal_enlrgmt": "X",
        "fuel_burning": "X",
        "horizontal_enlrgmt": "Y",
        "landmarked": "Y",
        "little_e": lambda x: x == "Y" or x == "H",
        "loft_board": "Y",
        "mechanical": "Y",
        "nonprofit": "Y",
        "other": "X",
        "pc_filed": "Y",
        "plumbing": "X",
        "professional_cert": "Y",
        "sprinkler": "X",
        "standpipe": "X",
        "vertical_enlrgmt": "Y"
    }


def applications_addtnl_wrangle(df):
    df = df.rename(columns=applications_cols_to_rename())
    df = downcast_all_num_cols(df)
    df = replace_all_empty_strings(df)
    df = clean_site_fill_col(df)
    df = convert_cols_to_categorical(df, applications_cols_to_cat())
    df = get_all_bool_cols(df, applications_cols_to_bool())
    return df


def permits_read_csv_kwargs():
    return {
        "low_memory": False
    }


def permits_conversions():
    return {
        "issuance_date": pd.to_datetime,
        "filing_date": pd.to_datetime,
        "bin": to_num_with_coerce
    }


def permits_addtnl_cols(df):
    return make_dt_rollup_cols(df, "issuance_date")


def permits_cols_to_rename():
    return {
        "superintendent_first__last_name": "superintendent_first_last_name",
    }


def permits_cols_to_cat():
    return (
        "borough", "community_board", "job_type", "nta_name", "oil_gas", 
        "permit_status", "permit_subtype", "permit_type", 
        "permittees_license_type", "site_fill", "special_district_1",
        "special_district_2", "work_type")


def permits_cols_to_bool():
    return {
        "act_as_superintendent": "Y",
        "nonprofit": "Y",
        "residential": "YES",
        "self_cert": "Y"
    }


def permits_addtnl_wrangle(df):
    df = df.rename(columns=permits_cols_to_rename())
    df = downcast_all_num_cols(df)
    df = replace_all_empty_strings(df)
    df = clean_site_fill_col(df)
    df = convert_cols_to_categorical(df, permits_cols_to_cat())
    df = convert_str_cols_to_bool(df, permits_cols_to_bool())
    return df


def permits_now_read_csv_kwargs():
    return {
        "low_memory": False
    }


def permits_now_conversions():
    return {
        "expired_date": pd.to_datetime,
        "issued_date": to_dt_with_coerce
    }


def permits_now_addtnl_cols(df):
    return make_dt_rollup_cols(df, "issued_date")


def permits_now_cols_to_cat():
    return (
        "borough", "permittees_license_type", "work_type")


def permits_now_addtnl_wrangle(df):
    df = df.rename(columns=permits_cols_to_rename())
    df = downcast_all_num_cols(df)
    df = replace_all_empty_strings(df)
    df = convert_cols_to_categorical(df, permits_now_cols_to_cat())
    return df

def complaints_read_csv_kwargs():
    return {
        "low_memory": False,
        "dtype": {"complaint_category": str}
    }


def complaints_conversions():
    return {
        "date_entered": to_dt_with_coerce,
        "disposition_date": to_dt_with_coerce_and_format,
        "inspection_date": to_dt_with_coerce_and_format,
        "dobrundate": pd.to_datetime,
        "complaint_number": to_num_with_coerce,
        "zip_code": to_num_with_coerce,
        "bin": to_num_with_coerce,
        "community_board": to_num_with_coerce,
    }


def complaints_addtnl_cols(df):
    return make_dt_rollup_cols(df, "date_entered")


def complaints_cols_to_rename():
    return {
        "dobrundate": "dobrun_date"
    }


def complaints_cols_to_cat():
    return (
        "status", "complaint_category", "unit", "disposition_code",
        "special_district", "boro")


def complaints_addtnl_wrangle(df):
    df.drop_duplicates(subset ="complaint_number", keep="last", inplace=True)
    df["boro"] = df.complaint_number.astype(str).str[0].astype(int)
    df = df.rename(columns=complaints_cols_to_rename())

    df = downcast_all_num_cols(df)
    df = replace_all_empty_strings(df)
    df = convert_cols_to_categorical(df, complaints_cols_to_cat())
    return df


def violations_dob_read_csv_kwargs():
    return {
        "low_memory": False
    }


def violations_dob_conversions():
    return {
        "issue_date": to_dt_with_coerce
    }


def violations_dob_addtnl_cols(df):
    return make_dt_rollup_cols(df, "issue_date")


def violations_dob_addtnl_wrangle(df):
    df = df.dropna(subset=["issue_date"]).copy()

    df = downcast_all_num_cols(df)
    df = replace_all_empty_strings(df)

    return df 


def violations_ecb_read_csv_kwargs():
    return {
        "low_memory": False
    }


def violations_ecb_conversions():
    return {
            "bin": to_num_with_coerce,
            "issue_date": to_dt_with_coerce_and_format,
            "hearing_date": to_dt_with_coerce_and_format,
            "served_date": to_dt_with_coerce_and_format
        }


def violations_ecb_addtnl_cols(df):
    df =  make_dt_rollup_cols(df, "issue_date")
    return make_dt_rollup_cols(df, "hearing_date")


def violations_ecb_cols_to_cat():
    return (
        "aggravated_level", "certification_status", "hearing_status",
        "infraction_code1", "infraction_code2", "infraction_code3",
        "infraction_code4", "infraction_code5", "infraction_code6",
        "infraction_code7", "infraction_code8", "infraction_code9",
        "infraction_code10", "section_law_description1",
        "section_law_description2", "section_law_description3",
        "section_law_description4", "section_law_description5",
        "section_law_description6", "section_law_description7",
        "section_law_description8", "section_law_description9",
        "section_law_description10", "severity", "violation_type")


def violations_ecb_addtnl_wrangle(df):
    df = df.dropna(subset=["issue_date"]).copy()
    df = downcast_all_num_cols(df)
    df = replace_all_empty_strings(df)
    df = convert_cols_to_categorical(df, violations_ecb_cols_to_cat())
    return df