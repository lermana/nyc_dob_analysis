import os
import io
import zipfile
import requests
import pandas as pd


from .settings import STREETEASY_URL, STREETEASY_DIR


def download_streeteasy_zip(file_path):
    data_url = STREETEASY_URL + file_path

    with requests.get(data_url) as r:

        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            z.extractall(path=STREETEASY_DIR)


def get_raw_streeteasy_data_from_file(file_name):
    return pd.read_csv(
                    os.path.join(STREETEASY_DIR, file_name))


def download_all_recorded_sales():
    download_streeteasy_zip("sales/All/recordedSalesVolume_All.zip")


def get_raw_sales_data_from_file():
    return get_raw_streeteasy_data_from_file("recordedSalesVolume_All.csv")


def get_clean_data(raw_data, data_name):
    date_cols = raw_data.columns[3:]
    label_cols = ["area_name", "borough", "area_type"]
    raw_data.columns = label_cols + date_cols.to_list()

    data_reindexed = raw_data.set_index("area_name")

    label_cols = ["borough", "area_type"]
    label_data = data_reindexed[label_cols]
    data_reindexed.drop(label_cols, axis=1, inplace=True)

    date_cols = data_reindexed.columns
    date_cols_levels = list(zip(*date_cols.str.split("-")))
    date_cols_levels = [list(map(int, vals)) for vals in date_cols_levels]

    date_cols = pd.MultiIndex.from_arrays(
                                date_cols_levels,
                                names=["year", "month"]
                            )

    data_reindexed.columns = date_cols
    data_reindexed = data_reindexed.stack(
                                  ).stack(
                                  ).rename(
                                      data_name
                                  ).to_frame()

    data_reindexed.index = data_reindexed.index.swaplevel(2, 1)
    data_reindexed = data_reindexed.join(label_data)

    return data_reindexed.reset_index(
                        ).set_index(
                                ["area_name", "year", "month"
                       ]).sort_index()


def get_sales_data(raw_data=None):
    if raw_data is None:
        download_all_recorded_sales()
        raw_data = get_raw_sales_data_from_file()

    data = get_clean_data(raw_data, data_name="median_sales_price")
    return data


def download_median_asking_rent():
    download_streeteasy_zip("rentals/All/medianAskingRent_All.zip")


def get_raw_rent_data_from_file():
    return get_raw_streeteasy_data_from_file("medianAskingRent_All.csv")


def get_rent_data(raw_data=None):
    if raw_data is None:
        download_median_asking_rent()
        raw_data = get_raw_rent_data_from_file()

    data = get_clean_data(raw_data, data_name="median_asking_rent")
    
    return data


def get_all_data():
    sales = get_sales_data().reset_index()
    rent = get_rent_data().reset_index()
    return sales, rent