import os
import pandas as pd
import numpy as np
from collections import ChainMap
import matplotlib.pyplot as plt

from . import database, meta
from .settings import DATASET_NAMES, FIGURE_DIR


def convert_year_month_to_labels(table, year_col, month_col):
   table.rename_axis(index = {
                                 year_col: "year",
                                 month_col: "month"
                        }, 
                     inplace = True)

   table = table.reset_index()

   data_labels = table.year.astype(str) + "-" + table.month.astype(str)

   data_labels_cat = pd.Categorical(
                           data_labels,
                           data_labels.sort_index(),
                           ordered=True)

   table["data_labels"] = data_labels_cat
   table.set_index("data_labels",inplace=True)

   return table


def convert_float_indices_to_int(df):
   """
   In the date time converting process, missing values would cause a dt.year() have a float value. 
   This function is  to  solve the grouped dataframe having float index year/month issue.
   """
   index_col_names = df.index.names
   df = df.reset_index()
    
   to_convert = list(
                     set(index_col_names) &
                     set(df.select_dtypes(include=float))
                  )

   df.loc[:, to_convert] = df[to_convert].astype(int)
   df = df.set_index(index_col_names)

   return df


def get_sql(
        year_col,
        *other_cols,
        dataset_name=None,
        filter_year=2000,
        addtnl_clause=None
    ):
    """
    Helper function allowing us to avoid writing repetitive SQL strings.
    Please note that the way in which the SQL is dynamically generated
    below could allow for SQL injection - this methodology works fine in
    this case, but don't use this as an example for how to interact with a
    real database.
    """ 
    if other_cols:
       cols_to_select = ", ".join(other_cols) + ", "
    else:
       cols_to_select = ""

    cols_to_select += year_col

    sql = f"""
       select {cols_to_select}
       from {dataset_name}
       where {year_col} >= {filter_year}
    """

    if addtnl_clause:
        sql += f"\nand {addtnl_clause}"

    return sql


def get_year_counts(
                  index_col,
                  year_col,
                  dataset_name=None,
                  filter_year=2000
               ):
    sql = get_sql(
               year_col, index_col,
               dataset_name=dataset_name, filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    # Cindy's suggestion, duplicated complaints genterated by database update
    if dataset_name == "complaints":
        df.drop_duplicates(subset =index_col, keep = 'last',inplace= True)

    return df.groupby(year_col).count()


def get_year_month_counts(
                  index_col,
                  year_col,
                  month_col,
                  dataset_name=None,
                  filter_year=2000
               ):
    sql = get_sql(
               year_col, index_col, month_col,
               dataset_name=dataset_name, filter_year=filter_year
            )

    df = database.get_query_as_df(sql)
    # Cindy's suggestion, duplicated complaints genterated by database update
    if dataset_name == "complaints":
        df.drop_duplicates(subset =index_col, keep = 'last',inplace= True)

    df = df.groupby([year_col, month_col]).count()
    df = convert_float_indices_to_int(df)
    df = convert_year_month_to_labels(
                                df, month_col=month_col, year_col=year_col
                            ).drop(
                                columns=["year","month"]
                            )

    return df


def get_issuance_rate(df):
        return df.approved.notnull(
                         ).sum(
                         ) / df.fully_paid.notnull(
                                          ).sum()


def get_issuance_rates_df(filter_year=2000):
    sql = get_sql(
                "pre_filing_date_year", "approved", "fully_paid",
                dataset_name="applications", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby("pre_filing_date_year").apply(get_issuance_rate)


def get_issuance_num_df(filter_year=2000):
    sql = get_sql(
               "pre_filing_date_year", "approved",
               dataset_name="applications", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby("pre_filing_date_year").count()


def get_issuance_rates_type_df(filter_year=2000):    
    sql = get_sql(
               "pre_filing_date_year", "approved", "fully_paid", "job_type",
               dataset_name="applications", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby(["pre_filing_date_year", "job_type"]).apply(get_issuance_rate)


def get_dataset_type_df( 
                        type_col,
                        index_col,
                        year_col,
                        dataset_name=None, 
                        filter_year=2000
                    ):
    sql = get_sql(
               year_col, index_col, type_col,
               dataset_name=dataset_name, filter_year=filter_year
            )

    df = database.get_query_as_df(sql)
    # Cindy's suggestion, duplicated complaints genterated by database update
    if dataset_name == "complaints":
        df.drop_duplicates(subset =index_col, keep = 'last',inplace= True)

    return df.groupby([year_col, type_col]).count()


def get_ecb_penalty_year_month_by_issue_df(
                            agg_method_or_methods=np.mean,
                            filter_year=2000,
                            to_group_by=["issue_date_year", "issue_date_month"]
                        ):
    sql = get_sql(
               "issue_date_year", "issue_date_month", "penality_imposed", "amount_paid",
               dataset_name="violations_ecb", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby(to_group_by).agg(agg_method_or_methods)


def get_ecb_penalty_year_by_issue_df(
                            agg_method_or_methods=np.mean,
                            filter_year=2000,
                            to_group_by=["issue_date_year"]
                        ):
    sql = get_sql(
               "issue_date_year", "penality_imposed", "amount_paid",
               dataset_name="violations_ecb", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby(to_group_by).agg(agg_method_or_methods)


def get_ecb_penalty_year_month_by_hearing_df(
                            agg_method_or_methods=np.mean,
                            filter_year=2000,
                            to_group_by=["hearing_date_year", "hearing_date_month"]
                        ):
    sql = get_sql(
               "hearing_date_year", "hearing_date_month", "penality_imposed", "amount_paid",
               dataset_name="violations_ecb", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby(to_group_by).agg(agg_method_or_methods)


def violations_ecb_penalties_year_agg(
                            agg_method_or_methods=np.mean,
                            filter_year=2000,
                            to_group_by=["hearing_date_year"]
                        ):
    sql = get_sql(
               "hearing_date_year", "penality_imposed", "amount_paid",
               dataset_name="violations_ecb", filter_year=filter_year
            )

    df = database.get_query_as_df(sql)

    return df.groupby(to_group_by).agg(agg_method_or_methods)


def get_ecb_violations_penalty_boro_df(boro_num=1, agg_method_or_methods=np.mean, filter_year=2000):
    sql = get_sql(
               "issue_date_year", "issue_date_month", "penality_imposed",
               dataset_name="violations_ecb", filter_year=filter_year,
               addtnl_clause=f"boro = {boro_num}"
            )

    df = database.get_query_as_df(sql)

    return df.groupby(["issue_date_year", "issue_date_month"]).agg(agg_method_or_methods)


def get_complaints_boro_df(boro_num=1, filter_year=2000):
    sql = get_sql(
               "date_entered_year", "date_entered_month", "complaint_number",
               dataset_name="complaints", filter_year=filter_year,
               addtnl_clause=f"boro = {boro_num}"
            )

    df = database.get_query_as_df(sql)
    df.drop_duplicates(subset ="complaint_number", keep = 'last',inplace= True)

    return df.groupby(["date_entered_year", "date_entered_month",]).count()


def get_ecb_violations_boro_df(boro_num=1, filter_year=2000):
    sql = get_sql(
               "issue_date_year", "issue_date_month", "isn_dob_bis_extract",
               dataset_name="violations_ecb", filter_year=filter_year,
               addtnl_clause=f"boro = {boro_num}"
            )

    df = database.get_query_as_df(sql)

    return df.groupby(["issue_date_year", "issue_date_month",]).count()


def get_permits_boro_df(boro_name="MANHATTAN", filter_year=2000):
    sql = get_sql(
               "issuance_date_year", "issuance_date_month", "permit_si_no",
               dataset_name="permits", filter_year=filter_year,
               addtnl_clause=f"borough = '{boro_name}'"
            )

    df = database.get_query_as_df(sql)

    return df.groupby(["issuance_date_year", "issuance_date_month"]).count()


def get_applications_boro_df(boro_name="MANHATTAN", filter_year=2000):
    sql = get_sql(
               "pre_filing_date_year", "pre_filing_date_month", "job",
               dataset_name="applications", filter_year=filter_year,
               addtnl_clause=f"borough = '{boro_name}'"
            )

    df = database.get_query_as_df(sql)

    return df.groupby(["pre_filing_date_year", "pre_filing_date_month"]).count()


def get_func_for_dataset(dataset_name, func_suffix):
    return meta.get_funcs_for_dataset(
                            dataset_name, globals()
                                    )[func_suffix]


def applications_year(filter_year=2000):
    return get_year_counts(
                        dataset_name="applications",
                        index_col="job",
                        year_col="pre_filing_date_year",
                        filter_year=filter_year
                    )


def permits_year(filter_year=2000):
    return convert_float_indices_to_int(
                get_year_counts(
                        dataset_name="permits",
                        index_col="permit_si_no",
                        year_col="issuance_date_year",
                        filter_year=filter_year
                ))


def permits_now_year(filter_year=2000):
    return convert_float_indices_to_int(
                get_year_counts(
                        dataset_name="permits_now",
                        index_col="job_filing_number",
                        year_col="issued_date_year",
                        filter_year=filter_year
                ))


def complaints_year(filter_year=2000):
    return get_year_counts(
                        dataset_name="complaints",
                        index_col="complaint_number",
                        year_col="date_entered_year",
                        filter_year=filter_year
                    )


def violations_ecb_year_counts(filter_year=2000, year_col="issue_date_year"):
    return convert_float_indices_to_int(
            get_year_counts(
                        dataset_name="violations_ecb",
                        index_col="isn_dob_bis_extract",
                        year_col=year_col,
                        filter_year=filter_year
                    ))


def get_year_func_for_dataset(dataset_name):
    return get_func_for_dataset(dataset_name, "year")


def get_year_data_for_dataset(dataset_name, filter_year=2000):
    func = get_year_func_for_dataset(dataset_name)
    return {
                func.__name__: func(filter_year=filter_year)
        }


def get_dob_year_data(filter_year=2000, exclude_violations_dob=True):
    datasets = DATASET_NAMES
    if exclude_violations_dob:
        datasets = filter(lambda x: x != "violations_dob", datasets)

    return dict(
            ChainMap(*
                [
                    get_year_data_for_dataset(
                        dataset_name, filter_year=filter_year
                    ) for dataset_name in datasets
            ]))


def applications_year_month(filter_year=2000):
    return get_year_month_counts(
                        dataset_name="applications",
                        index_col="job",
                        year_col="pre_filing_date_year",
                        month_col="pre_filing_date_month",
                        filter_year=filter_year
                    )


def permits_year_month(filter_year=2000):
    return get_year_month_counts(
                      dataset_name="permits",
                      index_col="permit_si_no",
                      year_col="issuance_date_year",
                      month_col="issuance_date_month",
                      filter_year=filter_year
              )


def permits_now_year_month(filter_year=2000):
    return get_year_month_counts(
                      dataset_name="permits_now",
                      index_col="job_filing_number",
                      year_col="issued_date_year",
                      month_col="issued_date_month",
                      filter_year=filter_year
              )

def complaints_year_month(filter_year=2000):
    return get_year_month_counts(
                        dataset_name="complaints",
                        index_col="complaint_number",
                        year_col="date_entered_year",
                        month_col="date_entered_month",
                        filter_year=filter_year
                    )


def violations_ecb_year_month_counts(filter_year=2000, year_col="issue_date_year",
                                     month_col="issue_date_month"):
    return get_year_month_counts(
                      dataset_name="violations_ecb",
                      index_col="isn_dob_bis_extract",
                      year_col=year_col,
                      month_col=month_col,
                      filter_year=filter_year
                  )


def get_year_month_func_for_dataset(dataset_name):
    return get_func_for_dataset(dataset_name, "year_month")


def get_year_month_data_for_dataset(dataset_name, filter_year=2000):
    func = get_year_month_func_for_dataset(dataset_name)
    return {
                func.__name__: func(filter_year=filter_year)
        }


def get_dob_year_month_data(filter_year=2000, exclude_violations_dob=True):
    datasets = DATASET_NAMES
    if exclude_violations_dob:
        datasets = filter(lambda x: x != "violations_dob", datasets)

    return dict(
            ChainMap(*
                [
                    get_year_month_data_for_dataset(
                        dataset_name, 
                        filter_year=filter_year
                ) for dataset_name in datasets
        ]))


def get_streeteasy_sales(end_year=2019):
    df = database.get_streeteasy_sales(area_name="Manhattan")

    df = convert_year_month_to_labels(
                                table=df.loc[:end_year],
                                month_col="month",
                                year_col="year"
                            ).drop(
                                columns=["year","month"]
                            )

    return {"streeteasy_sales": df}


def get_streeteasy_rent(end_year=2019):
    df = database.get_streeteasy_rent(area_name="Manhattan")
    
    df = convert_year_month_to_labels(
                                table=df.loc[:end_year],
                                month_col="month",
                                year_col="year"
                            ).drop(
                                columns=["year","month"]
                            )

    return {"streeteasy_rent": df}


def get_high_level_trends_data(begin_year, end_year):
    return {
                **get_dob_year_data(filter_year=begin_year),
                **get_dob_year_month_data(filter_year=2010),
                **get_streeteasy_sales(end_year=end_year),
                **get_streeteasy_rent(end_year=end_year)
            }


def savefig(fig_name, fig_obj, **adj_kwargs):
    fig_obj.subplots_adjust(**adj_kwargs)
    plt.savefig(os.path.join(FIGURE_DIR, fig_name))