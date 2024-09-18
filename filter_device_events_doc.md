# `event_timestamp_diffs.py` Documentation
## Timestamp Difference Calculator

## Table of Contents

* Overview
* Features
* Requirements
* Installation
* Usage
* Input Format
* Output Format
* Example
* Error Handling
* Additional Features
* Extensibility
* Testing
* Conclusion

## Overview

The Timestamp Difference Calculator is a Python script designed to process a JSON file containing an array of events, each with a timestamp. The script performs the following operations:

Reads the input JSON file containing timestamped events.
Filters events based on an optional start timestamp, ignoring events that occur before this timestamp.
Sorts the remaining events in chronological order.
Calculates the number of minutes between each consecutive event.
Generates an output JSON file containing:
A summary of the first and last timestamps.
A differences array detailing the minutes between events along with the corresponding ending timestamps.
This tool is particularly useful for analyzing event sequences, monitoring systems, or any application where understanding the intervals between events is essential.

## Features

Flexible Input Filtering: Optionally specify a start timestamp to process events from a particular point in time.
Automatic Sorting: Ensures events are processed in chronological order, even if the input is unsorted.
Detailed Output: Provides a clear summary and detailed differences between events.
Customizable Timestamp Keys: Accommodates JSON files with different keys for timestamps.
Comprehensive Error Handling: Handles various error scenarios gracefully, providing informative messages.

## Requirements

Python Version: Python 3.7 or higher.
Standard Libraries Used:
json
argparse
datetime
typing
Note: No external libraries are required.

## Installation

### Clone the Repository (if applicable):
```
TODO Update for github upload
git clone https://github.com/yourusername/timestamp-difference-calculator.git
cd timestamp-difference-calculator
```
### Download the Script:
* Save the calculate_minute_diffs.py script to your desired directory.

Verify Python Installation:\
Ensure you have Python 3.7 or higher installed:

```
python --version
```
If you don't have Python installed, download it from Python's official website.

## Usage

The script is executed via the command line and accepts several arguments to customize its behavior.

### Basic Command Structure

```
python calculate_minute_diffs.py <input_file> <output_file> [options]
```

### Positional Arguments
**input_file:**\
Description: Path to the input JSON file containing the array of timestamped events.\
Example: input.json

**output_file:**\
Description: Desired path for the output JSON file that will contain the summary and differences.\
Example: output.json

**Optional Arguments**

**--timestamp_key:**\
Description: Specifies the key used for timestamps in the JSON objects.\
Default: 'timestamp'\
Example: If your JSON objects use "time" instead of "timestamp", specify it as:
```
--timestamp_key time
```

**--start_timestamp:**\
Description: Specifies the ISO 8601 formatted timestamp to start processing from. Events occurring before this timestamp will be skipped.\
Default: None (processes all events)\
Usage:
Example: Only process events from August 1, 2023, 08:00:00 UTC onwards.\
```--start_timestamp "2023-01-01T08:00:00Z"```

### Full Command Example
```
python calculate_minute_diffs.py input.json output.json --timestamp_key time --start_timestamp "2023-01-01T08:00:00Z"
```
## Input Format

The input JSON file should be an array of objects, each containing at least a timestamp field. The key for the timestamp can be customized using the --timestamp_key argument.

Default Timestamp Key: timestamp\
Example (input.json):
```
[
    {"timestamp": "2023-01-01T07:30:00Z", "event": "Pre-Start"},
    {"timestamp": "2023-01-01T08:00:00Z", "event": "Start"},
    {"timestamp": "2023-01-01T09:30:00Z", "event": "Middle"},
    {"timestamp": "2023-01-01T11:00:00Z", "event": "End"}
]
```
Custom Timestamp Key: time\
Example (input.json):

```
[
    {"time": "2023-01-01T07:30:00Z", "event": "Pre-Start"},
    {"time": "2023-01-01T08:00:00Z", "event": "Start"},
    {"time": "2023-01-01T09:30:00Z", "event": "Middle"},
    {"time": "2023-01-01T11:00:00Z", "event": "End"}
]
```
Ensure all timestamp values are in ISO 8601 format.

## Output Format

The output is a JSON object containing two main components:

**summary:**\
Description: Contains the first and last timestamps from the processed events.

Fields:\
first_timestamp: The earliest timestamp after filtering.\
last_timestamp: The latest timestamp after filtering.

**differences:**\
Description: An array of objects detailing the minutes between consecutive events and the corresponding ending timestamps.

Fields:
minutes: Number of minutes between the current and previous timestamp.\
ending_timestamp: The timestamp corresponding to the end of the interval.\

**Example (output.json):**
```
{
    "summary": {
        "first_timestamp": "2023-01-01T08:00:00+00:00",
        "last_timestamp": "2023-01-01T11:00:00+00:00"
    },
    "differences": [
        {
            "minutes": 90,
            "ending_timestamp": "2023-01-01T09:30:00+00:00"
        },
        {
            "minutes": 90,
            "ending_timestamp": "2023-01-01T11:00:00+00:00"
        }
    ]
}
```
In this example:

The first event is at 08:00:00 UTC, and the last event is at 11:00:00 UTC.

There are two intervals:
- First Interval: 90 minutes between 08:00:00 UTC and 09:30:00 UTC.
- Second Interval: 90 minutes between 09:30:00 UTC and 11:00:00 UTC.

## Example

**Given Input (input.json):**
```
[
    {"timestamp": "2023-01-01T07:30:00Z", "event": "Pre-Start"},
    {"timestamp": "2023-01-01T08:00:00Z", "event": "Start"},
    {"timestamp": "2023-01-01T09:30:00Z", "event": "Middle"},
    {"timestamp": "2023-01-01T11:00:00Z", "event": "End"}
]
```

**Command Without --start_timestamp:**
```
python calculate_minute_diffs.py input.json output.json
```
Console Output:
```
Output successfully written to output.json
```
Generated output.json:
```
{
    "summary": {
        "first_timestamp": "2023-01-01T07:30:00+00:00",
        "last_timestamp": "2023-01-01T11:00:00+00:00"
    },
    "differences": [
        {
            "minutes": 30,
            "ending_timestamp": "2023-01-01T08:00:00+00:00"
        },
        {
            "minutes": 90,
            "ending_timestamp": "2023-01-01T09:30:00+00:00"
        },
        {
            "minutes": 90,
            "ending_timestamp": "2023-01-01T11:00:00+00:00"
        }
    ]
}
```

**Command With --start_timestamp:**\
```
python calculate_minute_diffs.py input.json output.json --start_timestamp "2023-01-01T08:00:00Z"
```
Console Output:
```
Filtered out 1 elements before 2023-01-01T08:00:00+00:00.
Output successfully written to output.json
```
Generated output.json:
```
{
    "summary": {
        "first_timestamp": "2023-01-01T08:00:00+00:00",
        "last_timestamp": "2023-01-01T11:00:00+00:00"
    },
    "differences": [
        {
            "minutes": 90,
            "ending_timestamp": "2023-01-01T09:30:00+00:00"
        },
        {
            "minutes": 90,
            "ending_timestamp": "2023-01-01T11:00:00+00:00"
        }
    ]
}
```
In this example, the event at 07:30:00 UTC is skipped due to the specified --start_timestamp.

## Error Handling

The script includes comprehensive error handling to manage various potential issues. Below are common error scenarios and how the script responds to them.

1. Invalid Input File Path
Scenario: The specified input file does not exist or the path is incorrect.

Error Message:
```
Error reading input file: [Errno 2] No such file or directory: 'nonexistent.json'
```

Solution: Ensure the input file path is correct and the file exists.

2. Invalid JSON Format
Scenario: The input file is not a valid JSON or not an array of objects.

Error Message:
```
Error reading input file: Expecting value: line 1 column 1 (char 0)
```
Solution: Verify that the input file is a properly formatted JSON array.

3. Missing Timestamp Key
Scenario: An event object lacks the specified timestamp key.

Error Message:
```
Error parsing timestamps: 'timestamp' not found in element at index 2
```
Solution: Ensure all event objects contain the specified timestamp key.

4. Invalid Timestamp Format
Scenario: A timestamp value is not in ISO 8601 format or is malformed.

Error Message:
```
Error parsing timestamps: Invalid timestamp format in element at index 1: "2023-01-01 08:00:00"
```
Solution: Ensure all timestamp values are in valid ISO 8601 format (e.g., "2023-01-01T08:00:00Z").

5. All Events Filtered Out
Scenario: The specified --start_timestamp filters out all events.

Error Message:
```
Filtered out 4 elements before 2023-01-02T00:00:00+00:00.
No timestamps remain after filtering. Exiting.
```

Solution: Choose a --start_timestamp that includes at least one event.

6. Invalid --start_timestamp Format
Scenario: The provided --start_timestamp is not in ISO 8601 format.

Error Message:
```
Error parsing start_timestamp: Invalid timestamp format: 2023-01-01 08:00:00
```
Solution: Provide the --start_timestamp in valid ISO 8601 format (e.g., "2023-01-01T08:00:00Z").

7. Invalid --timestamp_key
Scenario: The specified --timestamp_key does not exist in any event objects.

Error Message:
```
Error parsing timestamps: 'time' not found in element at index 0
```
Solution: Verify the correct timestamp key is specified using --timestamp_key.

8. Output File Write Errors
Scenario: The script lacks permissions to write to the specified output path or the path is invalid.

Error Message:
```
Error writing output file: [Errno 13] Permission denied: 'output.json'
```
Solution: Ensure you have write permissions to the desired output directory and that the path is correct.

## Additional Features

While the current script fulfills the primary requirements, here are some additional features and enhancements you might consider implementing:

**End Timestamp Filtering:**

Description:\
Add an optional --end_timestamp parameter to define an upper bound for processing. Events occurring after this timestamp will be ignored.

Implementation:\
Add a new argument in the parse_arguments() function.\
Filter timestamps to be less than or equal to end_timestamp.\

**Handling Timezones:**

Description:\
Ensure all timestamps are normalized to a single timezone or handle multiple timezones gracefully.

Implementation:\
Utilize timezone-aware datetime objects.
Convert all timestamps to UTC or the desired timezone before processing.

**Logging:**

Description:\
Integrate Python's logging module for better traceability and log management.

Implementation:\
Replace print statements with appropriate logging levels (e.g., info, warning, error).
Configure log outputs to console and/or log files.

**Performance Optimization:**

Description:\
Enhance performance for processing large datasets.

Implementation:\
Optimize data structures and algorithms.\
Implement streaming processing for very large files.

**Unit Testing:**

Description:\
Develop unit tests to ensure the script functions as expected.

Implementation:\
Use Python's unittest framework or other testing libraries like pytest.

## Extensibility

The script is designed with modular functions, making it easy to extend and customize based on specific needs. Here are some ways you can extend the script:

**Adding Event Metadata:**\
Include additional event details in the output, such as event names or IDs.

**Output Formats:**\
Support other output formats like CSV or XML in addition to JSON.

**Advanced Filtering:**\
Implement filters based on event types, categories, or other criteria besides timestamps.

**Interactive Mode:**\
Develop an interactive command-line interface (CLI) for easier usage without specifying all parameters upfront.

**Integration with Databases:**\
Extend the script to read from and write to databases instead of JSON files.

## Testing

Before deploying the script in a production environment, it's crucial to test it with various input scenarios to ensure reliability and correctness.

#### Test Cases

**Standard Input:**\
Description: Timestamps are in order and correctly formatted.\
Expectation: Correct summary and differences.

**Unsorted Input:**\
Description: Events are not in chronological order.\
Expectation: Script sorts events correctly and calculates differences accurately.

**Missing Timestamp Key:**\
Description: Some event objects lack the timestamp key.\
Expectation: Script raises a KeyError with an informative message.

**Invalid Timestamp Formats:**\
Description: Timestamps are malformed or not in ISO 8601 format.\
Expectation: Script raises a ValueError with details.

**All Events Filtered Out:**\
Description: The specified --start_timestamp filters out all events.\
Expectation: Script notifies the user and exits gracefully.

**Different Timestamp Keys:**\
Description: JSON objects use a different key for timestamps.\
Expectation: Script processes events correctly when --timestamp_key is specified.

**Large Dataset:**\
Description: Input JSON contains a large number of events.\
Expectation: Script processes the data efficiently without performance issues.

#### Testing Steps
**Prepare Test JSON Files:**\
Create multiple JSON files representing different scenarios outlined above.

**Run the Script Against Each Test File:**\
Execute the script using various combinations of arguments.

**Verify Outputs:**\
Ensure the output JSON matches expected results for each test case.

**Check Error Messages:**\
Confirm that error messages are informative and accurate for invalid inputs.

**Automate Testing:**\
Consider writing automated tests using frameworks like unittest or pytest for continuous testing.

## Conclusion

The Timestamp Difference Calculator is a versatile and robust tool for analyzing time intervals between events in JSON-formatted data. Its flexibility in handling different timestamp keys, optional filtering, and comprehensive error handling makes it suitable for a wide range of applications.

By following the documentation above, you can effectively install, configure, and utilize the script to meet your specific data processing needs. Additionally, its modular design allows for easy extension and customization to accommodate future requirements.

### Script Source Code

For your convenience, the complete Python script is provided below.

```
import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculate minute differences between timestamps in a JSON array.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file.')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file.')
    parser.add_argument('--timestamp_key', type=str, default='timestamp', help='The key used for timestamps in the JSON objects.')
    parser.add_argument('--start_timestamp', type=str, default=None, help='ISO 8601 formatted timestamp to start processing from. Elements before this timestamp will be skipped.')
    return parser.parse_args()

def read_json_file(file_path: str) -> List[Dict]:
    with open(file_path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array of objects.")
    return data

def parse_timestamp(ts_str: str) -> datetime:
    try:
        # Replace 'Z' with '+00:00' to handle UTC
        return datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
    except ValueError as ve:
        raise ValueError(f"Invalid timestamp format: {ts_str}") from ve

def parse_timestamps(data: List[Dict], timestamp_key: str) -> List[datetime]:
    timestamps = []
    for idx, item in enumerate(data):
        if timestamp_key not in item:
            raise KeyError(f"Element at index {idx} is missing the '{timestamp_key}' field.")
        try:
            ts = parse_timestamp(item[timestamp_key])
            timestamps.append(ts)
        except ValueError as ve:
            raise ValueError(f"Invalid timestamp format in element at index {idx}: {item[timestamp_key]}") from ve
    return timestamps

def filter_timestamps(timestamps: List[datetime], start_ts: Optional[datetime]) -> List[datetime]:
    if start_ts is None:
        return timestamps
    filtered = [ts for ts in timestamps if ts >= start_ts]
    return filtered

def calculate_minute_differences(timestamps: List[datetime]) -> List[Dict]:
    minute_diffs = []
    for i in range(1, len(timestamps)):
        diff = timestamps[i] - timestamps[i-1]
        minutes = int(diff.total_seconds() / 60)
        diff_info = {
            "minutes": minutes,  # Renamed from "difference_minutes" to "minutes"
            "ending_timestamp": timestamps[i].isoformat()
        }
        minute_diffs.append(diff_info)
    return minute_diffs

def main():
    args = parse_arguments()
    
    # Parse the start_timestamp if provided
    start_ts = None
    if args.start_timestamp:
        try:
            start_ts = parse_timestamp(args.start_timestamp)
        except ValueError as ve:
            print(f"Error parsing start_timestamp: {ve}")
            return
    
    # Read and parse the input JSON file
    try:
        data = read_json_file(args.input_file)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    
    # Extract and parse timestamps
    try:
        timestamps = parse_timestamps(data, args.timestamp_key)
    except Exception as e:
        print(f"Error parsing timestamps: {e}")
        return
    
    if not timestamps:
        print("No timestamps found in the input data.")
        return
    
    # Sort timestamps to ensure chronological order
    timestamps.sort()
    
    # Filter timestamps based on start_timestamp
    if start_ts:
        original_count = len(timestamps)
        timestamps = filter_timestamps(timestamps, start_ts)
        filtered_count = len(timestamps)
        skipped = original_count - filtered_count
        print(f"Filtered out {skipped} elements before {start_ts.isoformat()}.")
    
    if not timestamps:
        print("No timestamps remain after filtering. Exiting.")
        return
    
    # Calculate minute differences
    minute_diffs = calculate_minute_differences(timestamps)
    
    # Prepare the summary with first and last timestamps
    summary = {
        "first_timestamp": timestamps[0].isoformat(),
        "last_timestamp": timestamps[-1].isoformat()
    }
    
    # Prepare the output object with summary and differences
    output = {
        "summary": summary,
        "differences": minute_diffs
    }
    
    # Write the output to the specified JSON file
    try:
        with open(args.output_file, 'w') as f:
            json.dump(output, f, indent=4)
        print(f"Output successfully written to {args.output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    main()
```

### License

Specify the license under which the script is distributed, if applicable.

### Contact

Provide contact information or support channels for users who may have questions or need assistance.

