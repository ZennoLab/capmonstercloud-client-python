import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import CastleCustomTaskRequest


class CastleCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://www.example.com"
    websiteKeyExample = "pk_1Tk5Yzr1WFzxrJCh7WzMZzY1rHpaOtdK"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    wUrlExample = "https://s.rsg.sc/auth/js/20251234bgef/build/cw.js"
    swUrlExample = "https://s.rsg.sc/auth/js/20251234bgef/build/csw.js"

    def test_castle_request_required_fields(self):
        required_fields = ["type", "class", "websiteURL", "websiteKey", "metadata"]
        metadata_required_fields = ["wUrl", "swUrl"]
        metadata_example = {
            "wUrl": self.wUrlExample,
            "swUrl": self.swUrlExample,
        }
        request = CastleCustomTaskRequest(
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
        self.assertEqual(task_dictionary["class"], "Castle")
        self.assertEqual(task_dictionary["type"], "CustomTask")

    def test_castle_metadata_validation(self):
        base_kwargs = {
            "websiteUrl": self.websiteUrlExample,
            "websiteKey": self.websiteKeyExample,
            "metadata": {}
        }
        self.assertRaises(TypeError, CastleCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["wUrl"] = self.wUrlExample
        self.assertRaises(TypeError, CastleCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["swUrl"] = self.swUrlExample
        CastleCustomTaskRequest(**base_kwargs)

    def test_castle_metadata_with_count(self):
        metadata_example = {
            "wUrl": self.wUrlExample,
            "swUrl": self.swUrlExample,
            "count": 5,
        }
        request = CastleCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=metadata_example,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["metadata"]["count"], 5)

    def test_castle_missing_fields(self):
        base_kwargs = {}
        self.assertRaises(ValidationError, CastleCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, CastleCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteKey": self.websiteKeyExample})
        self.assertRaises(ValidationError, CastleCustomTaskRequest, **base_kwargs)
        metadata_example = {
            "wUrl": self.wUrlExample,
            "swUrl": self.swUrlExample,
        }
        base_kwargs.update({"metadata": metadata_example})
        CastleCustomTaskRequest(**base_kwargs)

    def test_castle_optional_fields(self):
        metadata_example = {
            "wUrl": self.wUrlExample,
            "swUrl": self.swUrlExample,
        }
        request = CastleCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=metadata_example,
            userAgent=self.userAgentExample,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["userAgent"], self.userAgentExample)


if __name__ == "__main__":
    unittest.main()
