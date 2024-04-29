import sys
from pylint import lint

THRESHOLD = 9  # Define the threshold for linter score

try:
    run = lint.Run(["factorial.py"], exit=False)  # 'exit' should be the correct parameter
except SystemExit:
    pass  # Prevent pylint from exiting the script
try:
    score = run.linter.stats.global_note  # Access the global note directly
except AttributeError:
    print("Error: Could not retrieve the global note from pylint.")
    sys.exit(1)  # If we can't get the score, exit with an error

# Check if the score meets or exceeds the threshold
if score < THRESHOLD:
    print("Linter failed: Score below threshold.")
    sys.exit(1)  # Exit with a failure status

# If the score meets or exceeds the threshold
print("Linter passed with sufficient score.")
sys.exit(0)  # Exit with a success status