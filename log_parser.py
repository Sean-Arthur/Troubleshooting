"""

Log Parser
Identifies WARNING and ERROR in device logs.

"""

log_file = "../sample-data/device.log"

errors = []
warnings = []

with open(log_file) as f:
    for line in f:
        if "ERROR" in line:
            errors.append(line.strip())
        elif "WARN" in line:
            warnings.append(line.strip())

print("\n===== Log Summary =====\n")

print(f"Errors found: {len(errors)}")
for e in errors:
    print(" -", e)

print(f"\nWarnings found: {len(warnings)}")
for w in warnings:
    print(" -", w)

print("\n=======================\n")