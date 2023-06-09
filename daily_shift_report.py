# generete daily sift raports base on input csv data
# csv data need to be in format:
# [index, date, hours, planned_output, real_output]
# ex.
# ['0', '2022-02-21', '0600-0700', '40', '36']

class ShiftReport:
    def __init__(self, dataset):
        self.__dataset = dataset
    
        self.__shift_I = ["0600-0700", "0700-0800", "0800-0900", "0900-1000", "1000-1100", "1100-1200", "1200-1300", "1300-1400"]
        self.__shift_II = ["1400-1500", "1500-1600", "1600-1700", "1700-1800", "1800-1900", "1900-2000", "2000-2100", "2100-2200"]
        self.__shift_III = ["2200-2300", "2300-0000", "0000-0100", "0100-0200", "0200-0300", "0300-0400", "0400-0500", "0500-0600"]

    # Extract shifts in date given
    # Format [day, shift, output planned, output real, oee]
    def calculate_shifts_raport_for_given_day(self, day):
        shift_I_hourly_target = []
        shift_II_hourly_target = []
        shift_III_hourly_target = []
        # invoke def to calculate hourly targets for needed shift
        shift_I_hourly_target = self.extract_shift_hourly_targets_based_on_shift_hours_set(day, self.__shift_I,1)
        #shift_II_hourly_targe = self.extract_shift_hourly_targets_based_on_shift_hours_set(self, day, self.__shift_II,2)
        #shift_III_hourly_targe = self.extract_shift_hourly_targets_based_on_shift_hours_set(self, day, self.__shift_III,3)       
        
        hour_target_planed = 0
        hourly_target_real = 0
        for element in shift_I_hourly_target:
            hour_target_planed = hour_target_planed + element[2]
            hourly_target_real = hourly_target_real + element[3] 
        oee = self.calculate_oee(hour_target_planed, hourly_target_real)
        final = [day, 1, hour_target_planed, hourly_target_real, oee] 
        return final

    # Calculate oee for given data. Return value raunded to two digits
    def calculate_oee(self, planned_output, real_output):
        percentage_result = round(real_output*100/planned_output,2)
        return percentage_result

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
                oee = self.calculate_oee(shift_planned_output, shift_output_real)
                shift_raport.append([day, shift_number, shift_planned_output , shift_output_real, oee])
                shift_output_real = 0
                shift_planned_output = 0           
        return shift_raport