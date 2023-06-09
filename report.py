# extracting data from database and transforming data to csv formats

import datetime
import pandas as pd
import csv
from pathlib import Path
import os

class Report:
    def __init__(self):
        self.__hourly_target_raports = []

        self.__source_path = source_path = Path("./src/")
        self.__output_path = output_path = Path("./temp/")

        self.__jedox_file_name = jedox_file_name = "jedox_new"
        self.__jedox_file_extension = "xlsm"
        self.__hourly_raport_dataset_file = hourly_raport_dataset_file = "hourly_raport_dataset"
        self.__hourly_raport_dataset_file_extension = "csv"

    # EXTRACT horly target raports list from jedox file
    def extract_hourly_target_raport_from_jedox_file(self):
        # Reading hourly target data sheet
        hourly_targets_data_sheet = self.__read_jedox_hourly_targets_sheet(
            os.path.join(
                self.__source_path , 
                self.__jedox_file_name 
                + '.' + 
                self.__jedox_file_extension
            )
        )

        # Removing hours, minutes from dates
        hourly_targets_data_sheet = self.__remove_hours_minutes_from_date(hourly_targets_data_sheet, "Date")
        # Storing clear raport list in this class field
        self.__hourly_target_raports = hourly_targets_data_sheet
    
    # GET dates of raports only
    def get_all_dates_from_report(self, dataset):
        dates_list_of_dates = []
        for element in dataset:
            dates_list_of_dates.append(element[1])
        #removing dupilcates
        dates_no_duplicates = self.__remove_duplicates_dates(dates_list_of_dates)
        # sorting dates ascending
        # sorting not needed
        return dates_no_duplicates


    # GET hourly report from csv file
    def get_hourly_dataset_from_csv_file(self):
        path_with_filename = os.path.join(
            self.__output_path,
            self.__hourly_raport_dataset_file
            + '.' +
            self.__hourly_raport_dataset_file_extension
        )
        with open(path_with_filename, "r") as file:
            reader_csv = csv.reader(file)
            list_of_csv = list(reader_csv)
        return list_of_csv

    # GET hourly target raports list
    def get_hourly_target_raports(self):
        return self.__hourly_target_raports

    # SAVE hourly targer raports list to csv file
    def save_raports_to_csv_file(self):
        self.__hourly_target_raports.to_csv(
            os.path.join(
                self.__output_path,
                self.__hourly_raport_dataset_file
                + '.' + 
                self.__hourly_raport_dataset_file_extension
            )
        )

    # LOAD hourly target raports from csv file and store it in variable
    def load_hourly_targets_raports_from_csv_file(self, path, filename):
        self.__hourly_target_raports = pd.read_csv(path+filename)
        return self.__hourly_target_raports

    def __remove_duplicates_dates(self, dates_set):
        dates_no_duplicates_list = []
        for element in dates_set:
            if (element in dates_no_duplicates_list):
                continue
            else:
                dates_no_duplicates_list.append(element)
        return dates_no_duplicates_list

    # READ pure data from jedox file
    def __read_jedox_hourly_targets_sheet(self, path):
        column_numbers = [3, 1, 4, 5]
        xls = pd.ExcelFile(path)
        data = pd.read_excel(
            xls, 'Sheet3', 
            usecols="A,B,E,F", 
            names=['Date', 'Hours', 'Planned', 'Output'
            ])
        return data

    # removing hours, minutes from given set of dates
    def __remove_hours_minutes_from_date(self, data_set, column_name):
        data_set[column_name] = data_set[column_name].dt.date
        return data_set


    
    # Calculate oee for given data. Return value raunded to two digits
    def calculate_oee(self, planned_output, real_output):
        percentage_result = round(real_output*100/planned_output,2)
        return percentage_result