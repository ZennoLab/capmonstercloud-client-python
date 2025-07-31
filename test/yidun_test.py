import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import YidunRequest


class YidunRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "189123456"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    def testCaptchaInputTypes(self):
        with self.assertRaises(ValidationError):
            request = YidunRequest()
        with self.assertRaises(ValidationError):
            request = YidunRequest(websiteUrl=self.websiteUrlExample)
        with self.assertRaises(ValidationError):
            request = YidunRequest(websiteKey=self.websiteKeyExample)

        request = YidunRequest(
            websiteKey=self.websiteKeyExample, websiteUrl=self.websiteUrlExample
        )
        request = YidunRequest(
            websiteKey=self.websiteKeyExample,
            websiteUrl=self.websiteUrlExample,
            userAgent=self.userAgentExample,
        )

    def testAllRequiredFieldsFilling(self):
        required_fields = ["type", "websiteURL", "websiteKey"]
        request = YidunRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        )
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()),
                msg=f"Required field {i} not in {request_dict}",
            )

        self.assertEqual(request_dict["type"], "YidunTask")


if __name__ == "__main__":
    unittest.main()
