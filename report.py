# extracting data from database and transforming data to csv formats

import pandas as pd
import csv

class Report:
    def __init__(self):
        self.__hourly_target_raports


    
    # EXTRACT horly target raports list from jedox file
    def extract_hourly_target_raport_from_jedox_file(self, jedox_path, file_name):
        # Reading hourly target data sheet
        hourly_targets_data_sheet = self.__read_jedox_hourly_targets_sheet(jedox_path + file_name)
        # Removing hours, minutes from dates
        hourly_targets_data_sheet = self.__remove_hours_minutes_from_date(hourly_targets_data_sheet, "Date")
        # Storing clear raport list in this class field
        self.__hourly_target_raports = hourly_targets_data_sheet
    
    # GET hourly target raports list
    def get_hourly_target_raports(self):
        return self.__hourly_target_raports

    # SAVE hourly targer raports list to csv file
    def save_raports_to_csv_file(self, path, filename):
        self.__hourly_target_raports_list.to_csv(path+filename)

    # LOAD hourly target raports from csv file and store it in variable
    def load_hourly_targets_raports_from_csv_file(self, path, filename):
        self.__hourly_target_raports = pd.read_csv(path+filename)
        return self.__hourly_target_raports

    # read pure data from jedox file
    def __read_jedox_hourly_targets_sheet(path):
        column_numbers = [3, 1, 4, 5]
        xls = pd.ExcelFile(path)
        data = pd.read_excel(
            xls, 'Sheet3', 
            usecols="A,B,E,F", 
            names=['Date', 'Hours', 'Planned', 'Output'
            ])
        return data

    # removing hours, minutes from given set of dates
    def __remove_hours_minutes_from_date(data_set, column_name):
        data_set[column_name] = data_set[column_name].dt.date
        return data_set

    def read_csv_dataset_no_pandas(path_with_filename):
        with open(path_with_filename, "r") as file:
            reader_csv = csv.reader(file)
            list_of_csv = list(reader_csv)
        return list_of_csv
    
    # Calculate oee for given data. Return value raunded to two digits
    def calculate_oee(self, planned_output, real_output):
        percentage_result = round(real_output*100/planned_output,2)
        return percentage_result