import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import TemuCustomTaskRequest


class TemuCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    cookieExample = "sessionid=abc123; path=/; domain=.example.com"

    def test_temu_request_required_fields(self):
        required_fields = ["type", "class", "websiteURL", "metadata"]
        metadata_required_fields = ["cookie"]
        request = TemuCustomTaskRequest(
            websiteUrl=self.websiteUrlExample, metadata={"cookie": self.cookieExample}
        )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(
                f in list(task_dictionary.keys()),
                msg=f'Required captcha input key "{f}" does not include to request.',
            )
        for f in metadata_required_fields:
            self.assertTrue(
                f in list(task_dictionary["metadata"].keys()),
                msg=f'Required captcha input key "{f}" does not include to request.',
            )

    def test_temu_metadata_validation(self):
        base_kwargs = {"websiteUrl": self.websiteUrlExample, "metadata": {}}
        self.assertRaises(TypeError, TemuCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["cookie"] = self.cookieExample
        TemuCustomTaskRequest(**base_kwargs)
        # Unsupported keys should raise error
        base_kwargs["metadata"]["extra"] = "not-allowed"
        self.assertRaises(TypeError, TemuCustomTaskRequest, **base_kwargs)

    def test_temu_missing_fields(self):
        base_kwargs = {}
        self.assertRaises(ValidationError, TemuCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, TemuCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"metadata": {"cookie": self.cookieExample}})
        TemuCustomTaskRequest(**base_kwargs)


if __name__ == "__main__":
    unittest.main()
