logs = []
keyword_match = 0

keyword_error = 0
keyword_fail = 0
keyword_warning = 0
keyword_denied = 0

keywords = ["error", "fail", "denied", "warning"]


num_logs = int(input("How many log entries do you want to enter? "))


if num_logs != 0:
    for i in range(num_logs):
        log = input("Entry " + str(i + 1) + ": ").lower()
        logs.append(log)
else:
    print("No logs. Exiting now")
    exit()

print("\n--- Scan Report ---")
print("\nTotal entries entered: " + str(num_logs))
print("\nEntries with keyword matches:")

matching_entries = 0

for index, log in enumerate(logs):
    entry_had_match = False
    if "error" in log:
        keyword_error += 1
        keyword_match += 1
        entry_had_match = True

    if "fail" in log:
        keyword_fail += 1
        keyword_match += 1
        entry_had_match = True

    if "warning" in log:
        keyword_warning += 1
        keyword_match += 1
        entry_had_match = True

    if "denied" in log:
        keyword_denied += 1
        keyword_match += 1
        entry_had_match = True

    if entry_had_match:
        matching_entries += 1
        print("Entry " + str(index + 1))

print("\nEntries containing keywords: " + str(matching_entries))
print("\nTotal keyword matches found: " + str(keyword_match))

print("\nKeyword breakdown:")
print("error: " + str(keyword_error))
print("fail: " + str(keyword_fail))
print("warning: " + str(keyword_warning))
print("denied: " + str(keyword_denied))