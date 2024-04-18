import json

def verify_policy_json(file_path):
    """
    Verifies the policy JSON file at the specified path.

    The function checks for the correct structure of the policy document and validates that no statement's
    resource field is exactly '*'. It raises specific errors for missing fields or incorrect structures.

    Args:
    file_path (str): The path to the JSON file to be verified.

    Returns:
    bool: True if all checks pass and no resource field is '*', otherwise False.

    Raises:
    ValueError: If any required field is missing or the JSON structure is incorrect.
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        policy_document = data.get('PolicyDocument')
        if policy_document is None:
            raise ValueError("Missing 'PolicyDocument'")

        statements = policy_document.get('Statement')
        if statements is None:
            raise ValueError("Missing 'Statement'")
        if not isinstance(statements, list):
            raise ValueError("'Statement' should be a list")

        for statement in statements:
            resource = statement.get('Resource')
            if resource == '*':
                return False
            if resource is None:
                raise ValueError("Missing 'Resource' field in a statement")

        return True

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON")
    except FileNotFoundError:
        raise ValueError("File not found")
