# generete daily raports base on input csv data
# input csv data need to be in format:
# [index, date, hours_timeframe, planned_output, real_output]
# ex.
# ['0', '2022-02-21', '0600-0700', '40', '36']
# output data:
#[date, planned_output, real_output, oee]
# example: 
# ['2023-05-09', 750, 677, 90.27]

import csv

class DailyReport:
    def __init__(self, dataset):
        self.__dataset = dataset
        self.__daily_reports = []
        self.__dates_list = []

    # GET daily raports list
    def get_daily_raports(self):
        return self.__daily_reports

    def transform_dataset_to_daily_reports_list(self):
        self.extract_all_dates_from_raport()
        self.calculate_raport_for_given_days(self.__dates_list)
        # ToDo: save raport to file 
    
    def print_daily_raports(self):
        for element in self.__daily_reports:
            print(element)

    # SAVE daily raports to csv file
    def save_daily_reports_to_file(self, file, path, dataset):
        dataset.to_csv(path + file)


    # Calcule report for one whole day. Return report table
    def calculate_raport_for_this_day(self, day):
        raport = []
        daily_output_real = 0
        daily_planned_output = 0
        for element in self.__dataset:
            if element[1]== day:
                daily_planned_output = daily_planned_output + int(element[3])
                daily_output_real = daily_output_real + int(element[4])
        oee = self.__calculate_oee(daily_planned_output, daily_output_real)
        day_report = [day, daily_planned_output, daily_output_real, oee]
        return day_report
    
    # Calculate oee for given data. Return value raunded to two digits
    def __calculate_oee(self, planned_output, real_output):
        percentage_result = round(real_output*100/planned_output,2)
        return percentage_result
        
    # Extract dates from given raport. Return list of dates
    def extract_all_dates_from_raport(self):
        for element in self.__dataset:
            if element[1] not in self.__dates_list:
                self.__dates_list.append(element[1])
        self.__dates_list.remove('Date')

    def get_dates_list(self):
        return self.__dates_list

    # Calculate raports for given list of dates. Return list of daily raports
    def calculate_raport_for_given_days(self, dates_list):
        for element in dates_list:
            daily_raport = self.calculate_raport_for_this_day(element)
            self.__daily_reports.append(daily_raport)