# Script to automate data collection for micro stops on production line

# Datas are being store in jedox_new.xlsm
#   * Hourly dargets data
#   * Shift targets data
#   * stops raports basis on operator descriptions

import report
import daily_report
import daily_shift_report

def main():

    # ************************************************************************
    # Extracting daily raports datas from jedox file and transfering it to csv
    # ************************************************************************
    report_file_operation = report.Report()
    report_file_operation.extract_hourly_target_raport_from_jedox_file()
    report_file_operation.save_raports_to_csv_file()

    # ****************************************************************
    # transform csv data set to daily raport & save raport to csv file
    # ****************************************************************
    csv_report_file = report.Report()
    dataset = csv_report_file.get_hourly_dataset_from_csv_file()
    daily_reports_list = daily_report.DailyReport(dataset)
    daily_reports_list.transform_dataset_to_daily_reports_list()
    daily_reports_list.print_daily_raports()
    # ToDo: Save daily raports to file
    daily_reports_file = "daily_reports_dataset.csv"
    daily_reports_path = "./temp/"
    daily_reports_list.save_daily_reports_to_file(daily_reports_path, daily_reports_file, daily_reports_list.get_daily_raports())
    
    # ********************************************************************************
    # Extract hourly output for each shift ( I, II, III) for given list of dates
    # Store raport in new csv file: db_shifts_raport.csv
    # ********************************************************************************
    csv_dataset = report.Report()
    dataset = csv_dataset.get_hourly_dataset_from_csv_file()
    # extracting dates only from raport
    dates = csv_dataset.get_all_dates_from_report(dataset) 
    # extract shift raports base only on extracted dates & put all extracted raports to one list
    shift_reports = daily_shift_report.ShiftReport(dataset)
    shift_reports.calculate_shift_raports_for_given_list_of_dates(dates)
    shift_reports_list = shift_reports.get_shift_reports_list()
    # print extracted shits raports for each shift and each date
    for element in shift_reports_list:
        print(element)
    # ToDo: save the raport list to file 


        # ToDo - plan:
        # Store calculated data in csv file
        # Code cleanup (separate code)



if __name__ == '__main__':
    main() 