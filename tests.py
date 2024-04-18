import unittest
from verify_policy_json import verify_policy_json

class TestVerifyPolicyJson(unittest.TestCase):

    def test_with_asterisk(self):
        result = verify_policy_json("test_data/with_asterisk.json")
        self.assertFalse(result)

    def test_with_asterisk_and_other(self):
        result = verify_policy_json("test_data/with_asterisk_and_other.json")
        self.assertTrue(result)

    def test_without_asterisk(self):
        result = verify_policy_json("test_data/without_asterisk.json")
        self.assertTrue(result)

    def test_without_asterisk_2(self):
        result = verify_policy_json("test_data/without_asterisk_2.json")
        self.assertTrue(result)

    def test_no_resource_field(self):
        with self.assertRaises(ValueError) as context:
            verify_policy_json("test_data/no_resource_field.json")
        self.assertIn('Missing \'Resource\'', str(context.exception))

    def test_invalid_json(self):
        with self.assertRaises(ValueError) as context:
            verify_policy_json("test_data/invalid_json.json")
        self.assertIn('Invalid JSON', str(context.exception))

    def test_statement_not_list(self):
        with self.assertRaises(ValueError) as context:
            verify_policy_json("test_data/statement_not_list.json")
        self.assertIn('\'Statement\' should be a list', str(context.exception))

    def test_missing_statement(self):
        with self.assertRaises(ValueError) as context:
            verify_policy_json("test_data/no_statement_field.json")
        self.assertIn('Missing \'Statement\'', str(context.exception))

    def test_no_policy(self):
        with self.assertRaises(ValueError) as context:
            verify_policy_json("test_data/no_policy.json")
        self.assertIn('Missing \'PolicyDocument\'', str(context.exception))

if __name__ == "__main__":
    unittest.main()
