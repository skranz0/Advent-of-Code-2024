def main():
    reports = read_input("input.txt")
    safe_reports = 0
    unsafe_reports = 0
    for report in reports:
        report_list = list(map(int, report.split()))
        if check_consistency(report_list) and check_differences(report_list):
            safe_reports += 1
        else:
            dampened_report_list = dampen(report_list)
            if check_consistency(dampened_report_list) and check_differences(dampened_report_list):
                safe_reports += 1
            else:
                unsafe_reports += 1
    print(f"Safe: {safe_reports}")
    print(f"Unsafe: {unsafe_reports}")

def read_input(filepath):
    with open(filepath, mode='r') as file:
        lines = file.readlines()
    print(f"{len(lines)} reports read")
    return lines

def check_consistency(report: list[int]) -> bool:
    return report == sorted(report) or report == sorted(report, reverse=True)

def check_differences(report: list[int]) -> bool:
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i+1])
        if difference < 1 or difference > 3:
            return False
    return True

def dampen(report: list[int]) -> list[int]:
    for level in report:
        dampened_report = report.copy()
        dampened_report.remove(level)
        if check_consistency(dampened_report) and check_differences(dampened_report):
            return dampened_report
    return report




if __name__ == '__main__':
    main()
