# generete daily raports base on input csv data
# csv dat need to be in format:
# [index, date, hours, planned_output, real_output]
# ex.
# ['0', '2022-02-21', '0600-0700', '40', '36']

from enum import Enum


class DailyReport:
    def __init__(self, dataset):
        self.__dataset = dataset

    # Calcule raport for one whole day. Return rapot table
    def calculate_raport_for_this_day(self, day):
        raport = []
        daily_output_real = 0
        daily_planned_output = 0
        for element in self.__dataset:
            if element[1]== day:
                daily_planned_output = daily_planned_output + int(element[3])
                daily_output_real = daily_output_real + int(element[4])
        oee = self.calculate_oee(daily_planned_output, daily_output_real)
        raport = [day, daily_planned_output, daily_output_real, oee]
        return raport
    
    # Calculate oee for given data. Return value raunded to two digits
    def calculate_oee(self, planned_output, real_output):
        percentage_result = round(real_output*100/planned_output,2)
        return percentage_result
        
    # Extract dates from given raport. Return list of dates
    def extract_all_dates_from_raport(self):
        dates_list = []
        for element in self.__dataset:
            if element[1] not in dates_list:
                dates_list.append(element[1])
        dates_list.remove('Date')
        return dates_list

    # Calculate raports for given list of dates. Return list of daily raports
    def calculate_raport_for_given_days(self, dates_list):
        daily_raports = []
        for element in dates_list:
            daily_raport = self.calculate_raport_for_this_day(element)
            daily_raports.append(daily_raport)
        return daily_raports

