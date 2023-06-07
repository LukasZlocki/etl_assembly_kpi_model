# Script to automate data collection for micro stops on production line

# Datas are being store in jedox_new.xlsm
#   * Hourly dargets data
#   * Shift targets data
#   * stops raports basis on operator descriptions

import report

import daily_report
import daily_shift_report

# object for extracting, transfering data from jedox file
report_file_operation = report.Report
source_path = "./src/"
output_path = "./temp/"

jedox_file_name = "jedox_new.xlsm"
hourly_raport_dataset_file = "hourly_raport_dataset.csv"

# Loading data from jedox file
#jedox_path = './src/jedox_new.xlsm'

# Reading hourly target data sheet
#hourly_targets_data_sheet = report_file_operation.read_jedox_hourly_targets_sheet(jedox_path)
#print("Hourly targets loaded from jedox file.")
#print(hourly_targets_data_sheet)

# Removing hours, minutes from dates
# hourly_targets_data_sheet = report_file_operation.remove_hours_minutes_from_date(hourly_targets_data_sheet, "Date")

# Converting to csv and write to file in /temp 
# report_file_operation.convert_read_excel_to_csv_end_save_file(hourly_targets_data_sheet)

# Read csv from file to csv dataset
#csv_hourly_targets_dataset = report_file_operation.read_csv_from_file()
#print("CSV hourly output data loaded from file.")

# *****************************************************
# Extracting data from jedox file and transfering it to csv
# *****************************************************
report_file_operation.extract_hourly_target_raport_from_jedox_file(source_path, jedox_file_name)
report_file_operation.save_raports_to_csv_file(output_path, hourly_raport_dataset_file)

# *****************************************************
# Extract hourly output for specific day from csv file
# *****************************************************
focus_day = "2022-02-21"
file_name_path = "./temp/csv_dataset.csv"
data = report_file_operation.read_csv_dataset_no_pandas(file_name_path)

print("Raporting Test")
raport = daily_report.DailyReport(data) 
daily_report = []
daily_report = raport.calculate_raport_for_this_day(focus_day)
print(daily_report)

# *****************************************************
# Extract hourly output for list of days from csv file
# *****************************************************
# ToDo: Code loading dat from file 
print("Creating list of dates:")
dates_list = raport.extract_all_dates_from_raport()
print(dates_list)

print("Calculating daily raports for all dates sets")
daily_raports_set = raport.calculate_raport_for_given_days(dates_list)
for raport in daily_raports_set:
    print(raport)


# ******************************************************
# Extract hourly output for each shift base on given day
# ******************************************************
report_shift = daily_shift_report.ShiftReport(data) 
date = '2023-05-25' # dates_list[5]
data = report_shift.calculate_shifts_raport_for_given_day(date)
print("Print three shifts raport for given date")
print(data)

    # ToDo - plan:
    # Extract raport for each shift (I, II, III) from given day
    # EXtract raport for each shifts for given list of dates
    # Store calculated data in csv file
    # Code cleanup (separate code)