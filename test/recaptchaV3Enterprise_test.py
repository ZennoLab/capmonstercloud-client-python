import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import RecaptchaV3EnterpriseRequest


class RecaptchaV3EnterpriseRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d8juDob"
    minScoreExample = 0.9
    pageActionExample = "submit"

    def test_captcha_input_types(self):
        with self.assertRaises(ValidationError):
            request = RecaptchaV3EnterpriseRequest(
                websiteUrl=RecaptchaV3EnterpriseRequestTest.websiteUrlExample
            )

        with self.assertRaises(ValidationError):
            request = RecaptchaV3EnterpriseRequest(
                websiteKey=RecaptchaV3EnterpriseRequestTest.websiteKeyExample,
            )

        request = RecaptchaV3EnterpriseRequest(
            websiteUrl=RecaptchaV3EnterpriseRequestTest.websiteUrlExample,
            websiteKey=RecaptchaV3EnterpriseRequestTest.websiteKeyExample,
            minScore=RecaptchaV3EnterpriseRequestTest.minScoreExample,
            pageAction=RecaptchaV3EnterpriseRequestTest.pageActionExample,
        )

    def test_all_required_fields_filling(self):
        required_fields = ["type", "websiteURL", "websiteKey"]
        request = RecaptchaV3EnterpriseRequest(
            websiteUrl=RecaptchaV3EnterpriseRequestTest.websiteUrlExample,
            websiteKey=RecaptchaV3EnterpriseRequestTest.websiteKeyExample,
            minScore=RecaptchaV3EnterpriseRequestTest.minScoreExample,
            pageAction=RecaptchaV3EnterpriseRequestTest.pageActionExample,
        )
        request_dict = request.getTaskDict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()),
                msg=f"Required field {i} not in {request_dict}",
            )

        self.assertEqual(request_dict["type"], "RecaptchaV3EnterpriseTask")
        self.assertEqual(request_dict["minScore"], self.minScoreExample)
        self.assertEqual(request_dict["pageAction"], self.pageActionExample)

    def test_optional_fields(self):
        request = RecaptchaV3EnterpriseRequest(
            websiteUrl=RecaptchaV3EnterpriseRequestTest.websiteUrlExample,
            websiteKey=RecaptchaV3EnterpriseRequestTest.websiteKeyExample,
        )
        request_dict = request.getTaskDict()
        self.assertNotIn("minScore", request_dict)
        self.assertNotIn("pageAction", request_dict)


if __name__ == "__main__":
    unittest.main()

