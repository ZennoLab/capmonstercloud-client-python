import unittest

from pydantic.error_wrappers import ValidationError

from capmonstercloudclient.requests import BasiliskCustomTaskRequest


class BasiliskCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "189123456"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    def testCaptchaInputTypes(self):
        with self.assertRaises(ValidationError):
            request = BasiliskCustomTaskRequest(
                websiteUrl=BasiliskCustomTaskRequestTest.websiteUrlExample
            )

        with self.assertRaises(ValidationError):
            request = BasiliskCustomTaskRequest(
                websiteKey=BasiliskCustomTaskRequestTest.websiteKeyExample,
            )

        request = BasiliskCustomTaskRequest(
            websiteUrl=BasiliskCustomTaskRequestTest.websiteUrlExample,
            websiteKey=BasiliskCustomTaskRequestTest.websiteKeyExample,
            userAgent=BasiliskCustomTaskRequestTest.userAgentExample,
        )

    def testAllRequiredFieldsFilling(self):
        required_fields = ["class", "type", "websiteURL", "websiteKey"]
        request = BasiliskCustomTaskRequest(
            websiteUrl=BasiliskCustomTaskRequestTest.websiteUrlExample,
            websiteKey=BasiliskCustomTaskRequestTest.websiteKeyExample,
        )
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()),
                msg=f"Required field {i} not in {request_dict}",
            )

        self.assertEqual(request_dict["class"], "Basilisk")
        self.assertEqual(request_dict["type"], "CustomTask")


if __name__ == "__main__":
    unittest.main()
