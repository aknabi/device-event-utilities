# `filter_device_events_doc.py` Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
    - [Basic Syntax](#basic-syntax)
    - [Command-Line Arguments](#command-line-arguments)
6. [Examples](#examples)
    - [1. Filtering by Default Type (`"HEARTBEAT"`)](#1-filtering-by-default-type-heartbeat)
    - [2. Filtering by Multiple Types (`"ALERT"` and `"INFO"`)](#2-filtering-by-multiple-types-alert-and-info)
    - [3. Case-Insensitive Filtering](#3-case-insensitive-filtering)
    - [4. Filtering by a Different Field (`"id"`)](#4-filtering-by-a-different-field-id)
    - [5. Writing Output to a File](#5-writing-output-to-a-file)
    - [6. Reading JSON from Standard Input](#6-reading-json-from-standard-input)
7. [Detailed Explanation](#detailed-explanation)
    - [Script Structure](#script-structure)
    - [Filtering Function](#filtering-function)
    - [Error Handling](#error-handling)
    - [Resource Management](#resource-management)
8. [Optional Enhancements](#optional-enhancements)
    - [1. Handling Non-String Fields](#1-handling-non-string-fields)
    - [2. Output Formatting Options](#2-output-formatting-options)
    - [3. Support for Nested Fields](#3-support-for-nested-fields)
    - [4. Logging and Verbose Output](#4-logging-and-verbose-output)
9. [Performance Considerations](#performance-considerations)
10. [Conclusion](#conclusion)

---

## Introduction

`filter_device_events.py` is a versatile Python script designed to filter elements within a JSON array based on specified criteria. It allows users to:

- **Filter by multiple values** within a specified field.
- **Choose the field** to filter on, not limited to the default `"type"` field.
- **Perform case-insensitive** filtering to accommodate varying data formats.
- **Handle large JSON files** efficiently through standard input/output streams.

This script is ideal for data processing tasks where JSON data needs to be filtered based on dynamic and multiple criteria.

---

## Features

- **Flexible Field Filtering:** Specify any field within the JSON objects to filter by.
- **Multiple Value Filtering:** Filter elements matching one or more specified values.
- **Case-Insensitive Matching:** Optionally ignore case when matching filter values.
- **Standard I/O Support:** Read from standard input and write to standard output, enabling seamless integration with other command-line tools.
- **Error Handling:** Gracefully handles malformed JSON and incorrect data structures.
- **Output Customization:** Option to write the filtered output to a file or display it in the console.

---

## Prerequisites

- **Python Version:** The script requires Python **3.x**.
- **Standard Libraries Used:**
  - `json`: For parsing and generating JSON data.
  - `argparse`: For handling command-line arguments.
  - `sys`: For accessing system-specific parameters and functions.

No external Python packages are required, making the script easy to deploy and use in various environments.

---

## Installation

1. **Download the Script:**

   Save the `filter_device_events.py` script to your desired directory. You can create a new file using your preferred text editor or download it directly if it's hosted online.

2. **Set Execute Permissions (Optional):**

   If you're on a Unix-like system and want to execute the script directly:

   ```bash
   chmod +x filter_device_events.py
   ```

3. **Ensure Python 3 is Installed:**

   Verify that Python 3.x is installed on your system:

   ```bash
   python3 --version
   ```

   If not installed, download and install Python from the [official website](https://www.python.org/downloads/).

---

## Usage

### Basic Syntax

```bash
python filter_device_events.py [input_file] [options]
```

- **`input_file`**: (Optional) Path to the input JSON file. If not provided, the script reads from standard input.

### Command-Line Arguments

| Argument             | Short Flag | Description                                                                 | Type        | Default       |
|----------------------|------------|-----------------------------------------------------------------------------|-------------|---------------|
| `input_file`         | N/A        | Path to the input JSON file. Reads from standard input if not provided.    | Positional  | `stdin`       |
| `-o`, `--output`     | `-o`       | Path to the output JSON file. Writes to standard output if not provided.    | Optional    | `stdout`      |
| `-f`, `--field`      | `-f`       | The field name to filter by.                                                | Optional    | `"type"`      |
| `-t`, `--types`      | `-t`       | One or more type values to filter by.                                      | Optional    | `["HEARTBEAT"]`|
| `-i`, `--ignore-case`| `-i`       | Perform case-insensitive matching for type values.                         | Optional    | `False`       |
| `-h`, `--help`       | `-h`       | Show help message and exit.                                                 | Optional    | N/A           |

#### Description of Arguments

1. **`input_file`**:
   - **Purpose:** Specifies the JSON file to be filtered.
   - **Usage:** Provide the path directly after the script name.
   - **Example:** `data.json`

2. **`-o`, `--output`**:
   - **Purpose:** Defines where to write the filtered JSON output.
   - **Usage:** Use `-o` followed by the desired output file path.
   - **Example:** `-o filtered_data.json`

3. **`-f`, `--field`**:
   - **Purpose:** Sets the field within JSON objects to apply the filter on.
   - **Usage:** Use `-f` followed by the field name.
   - **Example:** `-f id`

4. **`-t`, `--types`**:
   - **Purpose:** Specifies one or more values to filter by within the chosen field.
   - **Usage:** Use `-t` followed by one or more values.
   - **Example:** `-t ALERT INFO`

5. **`-i`, `--ignore-case`**:
   - **Purpose:** Enables case-insensitive matching for the specified type values.
   - **Usage:** Simply include `-i` or `--ignore-case` in the command.
   - **Example:** `-i`

6. **`-h`, `--help`**:
   - **Purpose:** Displays help information about the script's usage and arguments.
   - **Usage:** Use `-h` or `--help`.
   - **Example:** `-h`

---

## Examples

### 1. Filtering by Default Type (`"HEARTBEAT"`)

**Command:**

```bash
python filter_device_events.py data.json
```

**Explanation:**

- Filters JSON objects where the `"type"` field is `"HEARTBEAT"`.
- Reads from `data.json`.
- Outputs the filtered JSON to the console.

**Sample `data.json`:**

```json
[
    {"id": 1, "type": "HEARTBEAT", "timestamp": "2024-04-01T12:00:00Z"},
    {"id": 2, "type": "ALERT", "timestamp": "2024-04-01T12:05:00Z"},
    {"id": 3, "type": "HEARTBEAT", "timestamp": "2024-04-01T12:10:00Z"},
    {"id": 4, "type": "INFO", "timestamp": "2024-04-01T12:15:00Z"}
]
```

**Output:**

```json
[
    {
        "id": 1,
        "type": "HEARTBEAT",
        "timestamp": "2024-04-01T12:00:00Z"
    },
    {
        "id": 3,
        "type": "HEARTBEAT",
        "timestamp": "2024-04-01T12:10:00Z"
    }
]
```

---

### 2. Filtering by Multiple Types (`"ALERT"` and `"INFO"`)

**Command:**

```bash
python filter_device_events.py data.json --types ALERT INFO
```

**Explanation:**

- Filters JSON objects where the `"type"` field is either `"ALERT"` or `"INFO"`.
- Reads from `data.json`.
- Outputs the filtered JSON to the console.

**Output:**

```json
[
    {
        "id": 2,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:05:00Z"
    },
    {
        "id": 4,
        "type": "INFO",
        "timestamp": "2024-04-01T12:15:00Z"
    }
]
```

---

### 3. Case-Insensitive Filtering

**Command:**

```bash
python filter_device_events.py data.json --types heartbeat alert --ignore-case
```

**Explanation:**

- Filters JSON objects where the `"type"` field is `"heartbeat"` or `"alert"`, ignoring case differences.
- Reads from `data.json`.
- Outputs the filtered JSON to the console.

**Sample `data.json`:**

```json
[
    {"id": 1, "type": "HEARTBEAT", "timestamp": "2024-04-01T12:00:00Z"},
    {"id": 2, "type": "ALERT", "timestamp": "2024-04-01T12:05:00Z"},
    {"id": 3, "type": "heartbeat", "timestamp": "2024-04-01T12:10:00Z"},
    {"id": 4, "type": "Info", "timestamp": "2024-04-01T12:15:00Z"},
    {"id": 5, "type": "ALERT", "timestamp": "2024-04-01T12:20:00Z"}
]
```

**Output:**

```json
[
    {
        "id": 1,
        "type": "HEARTBEAT",
        "timestamp": "2024-04-01T12:00:00Z"
    },
    {
        "id": 2,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:05:00Z"
    },
    {
        "id": 3,
        "type": "heartbeat",
        "timestamp": "2024-04-01T12:10:00Z"
    },
    {
        "id": 5,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:20:00Z"
    }
]
```

*Note:* The `"Info"` type is excluded since it wasn't specified in the filter criteria.

---

### 4. Filtering by a Different Field (`"id"`)

**Command:**

```bash
python filter_device_events.py data.json --field id --types 1 3
```

**Explanation:**

- Filters JSON objects where the `"id"` field is either `1` or `3`.
- Reads from `data.json`.
- Outputs the filtered JSON to the console.

**Sample `data.json`:**

```json
[
    {"id": 1, "type": "HEARTBEAT", "timestamp": "2024-04-01T12:00:00Z"},
    {"id": 2, "type": "ALERT", "timestamp": "2024-04-01T12:05:00Z"},
    {"id": 3, "type": "heartbeat", "timestamp": "2024-04-01T12:10:00Z"},
    {"id": 4, "type": "Info", "timestamp": "2024-04-01T12:15:00Z"},
    {"id": 5, "type": "ALERT", "timestamp": "2024-04-01T12:20:00Z"}
]
```

**Output:**

```json
[
    {
        "id": 1,
        "type": "HEARTBEAT",
        "timestamp": "2024-04-01T12:00:00Z"
    },
    {
        "id": 3,
        "type": "heartbeat",
        "timestamp": "2024-04-01T12:10:00Z"
    }
]
```

*Important Note:* Since the `"id"` field in the JSON data is numeric, but command-line arguments are parsed as strings, the script performs string comparisons. To accurately filter numeric fields, you may need to modify the script to handle different data types.

---

### 5. Writing Output to a File

**Command:**

```bash
python filter_device_events.py data.json --types ALERT INFO --output filtered_data.json
```

**Explanation:**

- Filters JSON objects where the `"type"` field is either `"ALERT"` or `"INFO"`.
- Reads from `data.json`.
- Writes the filtered JSON to `filtered_data.json`.

**Result (`filtered_data.json`):**

```json
[
    {
        "id": 2,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:05:00Z"
    },
    {
        "id": 4,
        "type": "Info",
        "timestamp": "2024-04-01T12:15:00Z"
    },
    {
        "id": 5,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:20:00Z"
    }
]
```

---

### 6. Reading JSON from Standard Input

**Command:**

```bash
cat data.json | python filter_device_events.py --types HEARTBEAT ALERT --ignore-case
```

**Explanation:**

- Pipes the content of `data.json` directly into the script.
- Filters JSON objects where the `"type"` field is either `"HEARTBEAT"` or `"ALERT"`, ignoring case differences.
- Outputs the filtered JSON to the console.

**Output:**

```json
[
    {
        "id": 1,
        "type": "HEARTBEAT",
        "timestamp": "2024-04-01T12:00:00Z"
    },
    {
        "id": 2,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:05:00Z"
    },
    {
        "id": 3,
        "type": "heartbeat",
        "timestamp": "2024-04-01T12:10:00Z"
    },
    {
        "id": 5,
        "type": "ALERT",
        "timestamp": "2024-04-01T12:20:00Z"
    }
]
```

*Note:* The `"Info"` type is excluded as it wasn't specified in the filter criteria.

---

## Detailed Explanation

### Script Structure

The `filter_device_events.py` script is organized into several key components:

1. **Imports:** Utilizes standard Python libraries for JSON handling, argument parsing, and system operations.
2. **Filtering Function:** Contains the logic to filter JSON objects based on specified criteria.
3. **Main Function:** Handles argument parsing, file I/O, error handling, and orchestrates the filtering process.
4. **Execution Guard:** Ensures that the `main` function runs when the script is executed directly.

### Filtering Function

```python
def filter_elements_by_field(json_array, field, values, case_insensitive=False):
    """
    Filters elements in a JSON array where the specified field matches any of the provided values.

    Parameters:
        json_array (list): The input JSON array.
        field (str): The field name to filter by.
        values (list of str): The list of values to filter by.
        case_insensitive (bool): Whether the filtering should be case-insensitive.

    Returns:
        list: The filtered JSON array.
    """
    if case_insensitive:
        # Convert all filter values to lowercase for case-insensitive comparison
        values_lower = [v.lower() for v in values]
        filtered = [
            element for element in json_array
            if field in element and isinstance(element[field], str) and element[field].lower() in values_lower
        ]
    else:
        filtered = [
            element for element in json_array
            if element.get(field) in values
        ]
    return filtered
```

**Functionality:**

- **Parameters:**
  - `json_array`: The list of JSON objects to filter.
  - `field`: The key within each JSON object to apply the filter on.
  - `values`: A list of values to filter by.
  - `case_insensitive`: A boolean flag to enable case-insensitive matching.

- **Logic:**
  - **Case-Insensitive Filtering:**
    - Converts both the filter values and the JSON field values to lowercase.
    - Ensures that only string-type fields are compared to prevent type errors.
  - **Case-Sensitive Filtering:**
    - Directly compares the field's value with the filter values.

- **Returns:**
  - A list of JSON objects that match the filtering criteria.

### Main Function

```python
def main():
    parser = argparse.ArgumentParser(description='Filter JSON array elements by specified field and value(s).')
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='Path to the input JSON file. Reads from stdin if not provided.')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout,
                        help='Path to the output JSON file. Writes to stdout if not provided.')
    parser.add_argument('-f', '--field', type=str, default='type',
                        help='The field name to filter by. Defaults to "type".')
    parser.add_argument('-t', '--types', type=str, nargs='+', default=['HEARTBEAT'],
                        help='One or more type values to filter by. Defaults to "HEARTBEAT".')
    parser.add_argument('-i', '--ignore-case', action='store_true',
                        help='Perform case-insensitive matching for type values.')

    args = parser.parse_args()

    try:
        # Load JSON data
        data = json.load(args.input_file)

        if not isinstance(data, list):
            print("Error: The input JSON must be an array.", file=sys.stderr)
            sys.exit(1)

        # Filter the array based on the specified field and types
        filtered_data = filter_elements_by_field(
            data,
            field=args.field,
            values=args.types,
            case_insensitive=args.ignore_case
        )

        # Output the filtered array
        json.dump(filtered_data, args.output, indent=4)
        args.output.write('\n')  # Ensure newline at the end

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if args.input_file is not sys.stdin:
            args.input_file.close()
        if args.output is not sys.stdout:
            args.output.close()
```

**Functionality:**

1. **Argument Parsing:**
   - Utilizes `argparse` to define and parse command-line arguments.
   - Supports optional and positional arguments with default values.

2. **JSON Loading:**
   - Attempts to load the JSON data from the specified input file or standard input.
   - Validates that the input JSON is an array; exits with an error message if not.

3. **Filtering Process:**
   - Calls the `filter_elements_by_field` function with the parsed arguments to obtain the filtered data.

4. **Output Handling:**
   - Dumps the filtered JSON array to the specified output file or standard output.
   - Ensures the output is properly formatted with indentation for readability.

5. **Error Handling:**
   - Catches and reports JSON decoding errors.
   - Handles unexpected exceptions gracefully, providing informative error messages.

6. **Resource Management:**
   - Ensures that opened files are properly closed after processing, except when using standard input/output.

### Execution Guard

```python
if __name__ == '__main__':
    main()
```

- **Purpose:** Ensures that the `main` function is executed only when the script is run directly, not when imported as a module.

---

## Optional Enhancements

While `filter_device_events.py` is robust and versatile out-of-the-box, the following enhancements can further extend its functionality based on specific requirements:

### 1. Handling Non-String Fields

**Issue:** The current script performs case-insensitive matching only on string-type fields. Filtering numeric or other data types isn't handled appropriately.

**Solution:**

Modify the `filter_elements_by_field` function to handle different data types based on the field's data type.

**Example Modification:**

```python
def filter_elements_by_field(json_array, field, values, case_insensitive=False):
    if case_insensitive:
        # Convert all filter values to lowercase for case-insensitive comparison
        values_lower = [v.lower() for v in values if isinstance(v, str)]
        filtered = [
            element for element in json_array
            if field in element and isinstance(element[field], str) and element[field].lower() in values_lower
        ]
    else:
        filtered = [
            element for element in json_array
            if element.get(field) in values
        ]
    return filtered
```

**Usage Consideration:**

Ensure that the values provided via command-line match the data types of the JSON fields. For example, when filtering numeric fields like `"id"`, provide integer values or modify the script to convert string inputs to the appropriate type.

### 2. Output Formatting Options

**Feature:** Allow users to choose between pretty-printed JSON (with indentation) and compact JSON (without indentation).

**Implementation:**

- **Add an Argument:**

  ```python
  parser.add_argument('-c', '--compact', action='store_true',
                      help='Output compact JSON without indentation.')
  ```

- **Modify JSON Dump:**

  ```python
  if args.compact:
      json.dump(filtered_data, args.output)
  else:
      json.dump(filtered_data, args.output, indent=4)
  args.output.write('\n')
  ```

**Usage Example:**

```bash
python filter_device_events.py data.json --types ALERT --compact
```

**Result:**

Outputs the filtered JSON without indentation, making it more compact.

### 3. Support for Nested Fields

**Feature:** Allow filtering based on nested fields within JSON objects using dot notation (e.g., `"metadata.type"`).

**Implementation:**

- **Define a Function to Access Nested Fields:**

  ```python
  def get_nested_field(element, field_path):
      keys = field_path.split('.')
      for key in keys:
          if isinstance(element, dict) and key in element:
              element = element[key]
          else:
              return None
      return element
  ```

- **Modify the Filtering Function:**

  ```python
  def filter_elements_by_field(json_array, field, values, case_insensitive=False):
      if case_insensitive:
          values_lower = [v.lower() for v in values if isinstance(v, str)]
          filtered = [
              element for element in json_array
              if get_nested_field(element, field) and isinstance(get_nested_field(element, field), str) and get_nested_field(element, field).lower() in values_lower
          ]
      else:
          filtered = [
              element for element in json_array
              if get_nested_field(element, field) in values
          ]
      return filtered
  ```

**Usage Example:**

```bash
python filter_device_events.py data.json --field metadata.type --types ALERT
```

**Explanation:**

- Filters JSON objects where the nested field `"metadata.type"` is `"ALERT"`.

**Note:** Ensure that the nested field paths provided via the `--field` argument exist within the JSON objects to avoid unintended exclusions.

### 4. Logging and Verbose Output

**Feature:** Implement logging to provide insights during the script's execution, especially useful for debugging.

**Implementation:**

- **Import the `logging` Module:**

  ```python
  import logging
  ```

- **Add a Verbose Argument:**

  ```python
  parser.add_argument('-v', '--verbose', action='store_true',
                      help='Enable verbose output.')
  ```

- **Configure Logging:**

  ```python
  if args.verbose:
      logging.basicConfig(level=logging.DEBUG)
  else:
      logging.basicConfig(level=logging.WARNING)
  ```

- **Add Logging Statements:**

  ```python
  logging.debug(f"Filtering field: {args.field}")
  logging.debug(f"Filter values: {args.types}")
  logging.debug(f"Case-insensitive: {args.ignore_case}")
  logging.debug(f"Number of elements before filtering: {len(data)}")
  logging.debug(f"Number of elements after filtering: {len(filtered_data)}")
  ```

**Usage Example:**

```bash
python filter_device_events.py data.json --types ALERT --verbose
```

**Explanation:**

- Enables verbose logging, displaying debug information about the filtering process.

---

## Performance Considerations

### Handling Large JSON Files

**Issue:** Loading very large JSON arrays into memory can be resource-intensive and may lead to performance bottlenecks or memory errors.

**Solution:**

- **Use Streaming JSON Parsers:**

  Utilize libraries like [`ijson`](https://pypi.org/project/ijson/) to parse and process JSON data incrementally without loading the entire file into memory.

- **Implement Chunk-Based Processing:**

  Modify the script to read and process the JSON data in chunks, filtering and writing out results incrementally.

**Example Modification Using `ijson`:**

```python
import ijson

def filter_elements_by_field_streaming(input_stream, field, values, case_insensitive=False, output_stream=None):
    if case_insensitive:
        values_lower = [v.lower() for v in values]
        filtered = (
            item for item in ijson.items(input_stream, 'item')
            if field in item and isinstance(item[field], str) and item[field].lower() in values_lower
        )
    else:
        filtered = (
            item for item in ijson.items(input_stream, 'item')
            if item.get(field) in values
        )
    
    # Write filtered items to output_stream as a JSON array
    output_stream.write('[')
    first = True
    for item in filtered:
        if not first:
            output_stream.write(',\n')
        else:
            first = False
        json.dump(item, output_stream)
    output_stream.write(']\n')
```

*Note:* Incorporating `ijson` requires installing the package via `pip`:

```bash
pip install ijson
```

---

## Conclusion

`filter_device_events.py` is a powerful and flexible tool for filtering JSON arrays based on dynamic criteria. Its ability to handle multiple filter values, specify different fields, and perform case-insensitive matching makes it suitable for a wide range of data processing tasks. Additionally, with optional enhancements like nested field support and logging, the script can be tailored to meet complex requirements.

By following the documentation provided above, you can effectively integrate `filter_device_events.py` into your workflows, ensuring efficient and accurate JSON data filtering.

---

## Complete `filter_device_events.py` Script

For your convenience, here's the complete `filter_device_events.py` script incorporating all the discussed features:

```python
import json
import argparse
import sys

def filter_elements_by_field(json_array, field, values, case_insensitive=False):
    """
    Filters elements in a JSON array where the specified field matches any of the provided values.

    Parameters:
        json_array (list): The input JSON array.
        field (str): The field name to filter by.
        values (list of str): The list of values to filter by.
        case_insensitive (bool): Whether the filtering should be case-insensitive.

    Returns:
        list: The filtered JSON array.
    """
    if case_insensitive:
        # Convert all filter values to lowercase for case-insensitive comparison
        values_lower = [v.lower() for v in values]
        filtered = [
            element for element in json_array
            if field in element and isinstance(element[field], str) and element[field].lower() in values_lower
        ]
    else:
        filtered = [
            element for element in json_array
            if element.get(field) in values
        ]
    return filtered

def main():
    parser = argparse.ArgumentParser(description='Filter JSON array elements by specified field and value(s).')
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='Path to the input JSON file. Reads from stdin if not provided.')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout,
                        help='Path to the output JSON file. Writes to stdout if not provided.')
    parser.add_argument('-f', '--field', type=str, default='type',
                        help='The field name to filter by. Defaults to "type".')
    parser.add_argument('-t', '--types', type=str, nargs='+', default=['HEARTBEAT'],
                        help='One or more type values to filter by. Defaults to "HEARTBEAT".')
    parser.add_argument('-i', '--ignore-case', action='store_true',
                        help='Perform case-insensitive matching for type values.')

    args = parser.parse_args()

    try:
        # Load JSON data
        data = json.load(args.input_file)

        if not isinstance(data, list):
            print("Error: The input JSON must be an array.", file=sys.stderr)
            sys.exit(1)

        # Filter the array based on the specified field and types
        filtered_data = filter_elements_by_field(
            data,
            field=args.field,
            values=args.types,
            case_insensitive=args.ignore_case
        )

        # Output the filtered array
        json.dump(filtered_data, args.output, indent=4)
        args.output.write('\n')  # Ensure newline at the end

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if args.input_file is not sys.stdin:
            args.input_file.close()
        if args.output is not sys.stdout:
            args.output.close()

if __name__ == '__main__':
    main()
```
---
