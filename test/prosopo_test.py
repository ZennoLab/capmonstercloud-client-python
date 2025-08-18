import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import ProsopoTaskRequest


class ProsopoTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "prosopo-public-key-123"

    def test_prosopo_request_required_fields(self):
        required_fields = ["type", "websiteURL", "websiteKey"]
        request = ProsopoTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample
        )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(
                f in list(task_dictionary.keys()),
                msg=f'Required captcha input key "{f}" does not include to request.',
            )
        self.assertEqual(task_dictionary["type"], "ProsopoTask")

    def test_prosopo_missing_fields(self):
        base_kwargs = {}
        self.assertRaises(ValidationError, ProsopoTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, ProsopoTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteKey": self.websiteKeyExample})
        ProsopoTaskRequest(**base_kwargs)


if __name__ == "__main__":
    unittest.main()
