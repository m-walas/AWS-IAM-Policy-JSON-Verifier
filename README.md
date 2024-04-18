# AWS IAM Policy JSON Verifier

## Description
This project contains a Python module designed to verify AWS IAM Role policy JSON files. The verifier checks if the `Resource` field in any policy statement exactly contains a single asterisk (`*`). If it does, the verifier returns `False`; otherwise, it returns `True`. It also handles various error scenarios like missing fields or incorrect JSON formats.

## Requirements
- Python 3.8 or higher

## Installation Instructions
No additional libraries are required to run this module beyond the standard Python installation. Clone this repository to your local machine using:

```bash
git clone https://github.com/m-walas/AWS-IAM-Policy-JSON-Verifier
```

## How to Run the Code
Navigate to the project directory and run the following command to execute the verification:

```bash
python verify_policy_json.py <path-to-json-file>
```

## Testing
This project uses Python’s built-in unittest framework for testing. To run the tests, execute the following command in the project root directory:

```bash
python -m unittest
```
This command will automatically discover and run all tests defined in the test scripts.