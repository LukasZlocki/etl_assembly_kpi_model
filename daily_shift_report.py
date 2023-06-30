# generete daily sift raports base on input csv data
# csv data need to be in format:
# [index, date, hours, planned_output, real_output]
# ex.
# ['0', '2022-02-21', '0600-0700', '40', '36']

class ShiftReport:
    def __init__(self, dataset):
        self.__dataset = dataset
        
        # Shift time frames
        self.__shift_I = ["0600-0700", "0700-0800", "0800-0900", "0900-1000", "1000-1100", "1100-1200", "1200-1300", "1300-1400"]
        self.__shift_II = ["1400-1500", "1500-1600", "1600-1700", "1700-1800", "1800-1900", "1900-2000", "2000-2100", "2100-2200"]
        self.__shift_III = ["2200-2300", "2300-0000", "0000-0100", "0100-0200", "0200-0300", "0300-0400", "0400-0500", "0500-0600"]

        # Shift Report list
        self.__shift_reports_list = []

    # GET shit reports list
    def get_shift_reports_list(self):
        return self.__shift_reports_list

    # Calculate shit raports base on list of dates
    def calculate_shift_raports_for_given_list_of_dates(self, list_of_dates):
        for date in list_of_dates:
            shift_1_rep =  self.calculate_shifts_raport_for_given_day_and_shift(date, 1)
            shift_2_rep =  self.calculate_shifts_raport_for_given_day_and_shift(date, 2)
            shift_3_rep =  self.calculate_shifts_raport_for_given_day_and_shift(date, 3)
            # add only if raport exist and exclude empty reports
            if shift_1_rep:
                self.__shift_reports_list.append(shift_1_rep)
            if shift_2_rep:
                self.__shift_reports_list.append(shift_2_rep)
            if shift_3_rep:
                self.__shift_reports_list.append(shift_3_rep)

    # Extract shifts in date given
    # Format [day, shift_number, output_planned, output real, oee]
    def calculate_shifts_raport_for_given_day_and_shift(self, day, shift_number):
        shift_hourly_target = []
        # invoke def to calculate hourly targets for needed shift
        if shift_number == 1:
            shift_hourly_target = self.extract_shift_hourly_targets_based_on_shift_hours_set(day, self.__shift_I,1)
        if shift_number == 2:
            shift_hourly_target = self.extract_shift_hourly_targets_based_on_shift_hours_set(day, self.__shift_II,2)
        if shift_number == 3:
            shift_hourly_target = self.extract_shift_hourly_targets_based_on_shift_hours_set(day, self.__shift_III,3)
        return shift_hourly_target

    # Calculate oee for given data. Return value raunded to two digits
    def __calculate_oee(self, planned_output, real_output):
        if (planned_output == 0 and real_output == 0):
            percentage_result = 0
        else:
            percentage_result = round(real_output*100/planned_output,2)
        return percentage_result

    # Extract report for given shift and given day
    # Output format [date, shift_number, output_planned, output_real. oee]
    def extract_shift_hourly_targets_based_on_shift_hours_set(self, day, shift_hours_seter, shift_number):
        shift_raport = []
        shift_output_real = 0
        shift_planned_output = 0
        oee = 0
        for element in self.__dataset:
            if element[1]== day:
                for timeframe in shift_hours_seter:
                    if element[2] == timeframe:
                        shift_planned_output = shift_planned_output + int(element[3])
                        shift_output_real = shift_output_real + int(element[4])
        if (shift_planned_output > 0):
            oee = self.__calculate_oee(shift_planned_output, shift_output_real)
            shift_raport.append([day, shift_number, shift_planned_output , shift_output_real, oee])
            shift_output_real = 0
            shift_planned_output = 0           
        return shift_raport