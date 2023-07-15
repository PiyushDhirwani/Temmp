from fuzzywuzzy import fuzz

def find_max_fuzz_ratio(line, fund_list):
    max_ratio = -1
    max_fund = None

    for fund in fund_list:
        ratio = fuzz.ratio(line, fund)
        if ratio > max_ratio:
            max_ratio = ratio
            max_fund = fund

    return max_fund

def find_max_fuzz_ratio_in_lines(lines, fund_list):
    max_fund = None
    max_ratio = -1

    for line in lines:
        fund = find_max_fuzz_ratio(line, fund_list)
        ratio = fuzz.ratio(line, fund)

        if ratio > max_ratio:
            max_ratio = ratio
            max_fund = fund

    return max_fund

# Example usage
lines = [
    "This is line 1",
    "This is line 2",
    "This is line 3",
    "This is line 4",
]

fund_list = [
    "Fund A",
    "Fund B",
    "Fund C",
    "Fund D",
]

max_fund = find_max_fuzz_ratio_in_lines(lines, fund_list)
print("Maximum Fuzz Ratio Fund:", max_fund)
