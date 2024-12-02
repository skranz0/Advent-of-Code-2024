def main():
    reports = read_input("input.txt")
    safe_reports = 0
    unsafe_reports = 0
    for report in reports:
        if check_consistency(report) and check_differences(report):
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

def check_consistency(report: str) -> bool:
    report = list(map(int, report.split(' ')))
    return report == sorted(report) or report == sorted(report, reverse=True)

def check_differences(report: str) -> bool:
    report = list(map(int, report.split()))
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i+1])
        if difference < 1 or difference > 3:
            return False
    return True


if __name__ == '__main__':
    main()
