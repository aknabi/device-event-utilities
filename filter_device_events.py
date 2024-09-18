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
