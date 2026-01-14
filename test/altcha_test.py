import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import AltchaCustomTaskRequest


class AltchaCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "altcha-public-key-123"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    challengeExample = "challenge_string_here"
    iterationsExample = "1000"
    saltExample = "salt_string_here"
    signatureExample = "signature_string_here"

    def test_altcha_request_required_fields(self):
        required_fields = ["type", "class", "websiteURL", "websiteKey", "metadata"]
        metadata_required_fields = ["challenge", "iterations", "salt", "signature"]
        metadata_example = {
            "challenge": self.challengeExample,
            "iterations": self.iterationsExample,
            "salt": self.saltExample,
            "signature": self.signatureExample,
        }
        request = AltchaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=metadata_example,
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
        self.assertEqual(task_dictionary["class"], "altcha")
        self.assertEqual(task_dictionary["type"], "CustomTask")

    def test_altcha_metadata_validation(self):
        base_kwargs = {
            "websiteUrl": self.websiteUrlExample,
            "websiteKey": self.websiteKeyExample,
            "metadata": {}
        }
        self.assertRaises(TypeError, AltchaCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["challenge"] = self.challengeExample
        self.assertRaises(TypeError, AltchaCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["iterations"] = self.iterationsExample
        self.assertRaises(TypeError, AltchaCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["salt"] = self.saltExample
        self.assertRaises(TypeError, AltchaCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["signature"] = self.signatureExample
        AltchaCustomTaskRequest(**base_kwargs)

    def test_altcha_missing_fields(self):
        base_kwargs = {}
        self.assertRaises(ValidationError, AltchaCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, AltchaCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteKey": self.websiteKeyExample})
        self.assertRaises(ValidationError, AltchaCustomTaskRequest, **base_kwargs)
        metadata_example = {
            "challenge": self.challengeExample,
            "iterations": self.iterationsExample,
            "salt": self.saltExample,
            "signature": self.signatureExample,
        }
        base_kwargs.update({"metadata": metadata_example})
        AltchaCustomTaskRequest(**base_kwargs)


if __name__ == "__main__":
    unittest.main()

