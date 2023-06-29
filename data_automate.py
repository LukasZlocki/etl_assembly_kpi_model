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
    # Extract hourly output for each shift base on given day & save raport to csv file
    # ********************************************************************************
    csv_hourly_report = report.Report()
    hourly_dataset = csv_hourly_report.get_hourly_dataset_from_csv_file()
    shift_raport = daily_shift_report.ShiftReport(hourly_dataset)
    shift_1_rep =  shift_raport.calculate_shifts_raport_for_given_day_and_shift('2022-02-21', 1)
    shift_2_rep =  shift_raport.calculate_shifts_raport_for_given_day_and_shift('2022-02-21', 2)
    shift_3_rep =  shift_raport.calculate_shifts_raport_for_given_day_and_shift('2022-02-21', 3)

    print(shift_1_rep )
    print(shift_2_rep )
    print(shift_3_rep )
    # ToDo: Save shift raport to new csv file

    # ********************************************************************************
    # Extract hourly output for each shift ( I, II, III) for given list of dates
    # Store raport in new csv file: db_shifts_raport.csv
    # ********************************************************************************
    csv_dataset = report.Report()
    dataset = csv_dataset.get_hourly_dataset_from_csv_file()
    # extracting dates only from raport
    dates = csv_dataset.get_all_dates_from_report(dataset) 
    # extract shift raports base only on extracted dates & put all extracted raports to one list
    dataset_for_shift_reports = daily_shift_report.ShiftReport(dataset)
    full_shift_report = []
    for date in dates:
        shift_1_rep =  dataset_for_shift_reports.calculate_shifts_raport_for_given_day_and_shift(date, 1)
        shift_2_rep =  dataset_for_shift_reports.calculate_shifts_raport_for_given_day_and_shift(date, 2)
        shift_3_rep =  dataset_for_shift_reports.calculate_shifts_raport_for_given_day_and_shift(date, 3)
        # add only if raport exist and exclude empty reports
        if shift_1_rep:
            full_shift_report.append(shift_1_rep)
        if shift_2_rep:
            full_shift_report.append(shift_2_rep)
        if shift_3_rep:
            full_shift_report.append(shift_3_rep)
    # print extracted shits raports for each shift and each date
    for element in full_shift_report:
        print(element)
    # ToDo: save the raport list to file 




    # report_shift = daily_shift_report.ShiftReport(data) 
    # date = '2023-05-25' # dates_list[5]
    # data = report_shift.calculate_shifts_raport_for_given_day(date)
    # print("Print three shifts raport for given date")
    # print(data)

        # ToDo - plan:
        # Extract raport for each shift (I, II, III) from given day
        # EXtract raport for each shifts for given list of dates
        # Store calculated data in csv file
        # Code cleanup (separate code)



if __name__ == '__main__':
    main() 