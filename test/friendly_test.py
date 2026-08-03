import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import FriendlyCustomTaskRequest, ProxyInfo


class FriendlyCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "FCMSITEKEY000000000000000000000000000000"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    apiGetLibExample = "https://cdn.jsdelivr.net/npm/friendly-challenge@0.9.18/widget.module.min.js"

    def setUp(self):
        self.proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere"
        )

    def test_friendly_request_required_fields(self):
        required_fields = ["type", "class", "websiteURL", "websiteKey", "metadata"]
        metadata_required_fields = ["apiGetLib"]
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        request = FriendlyCustomTaskRequest(
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
        self.assertEqual(task_dictionary["class"], "friendly")
        self.assertEqual(task_dictionary["type"], "CustomTask")

    def test_friendly_metadata_validation(self):
        base_kwargs = {
            "websiteUrl": self.websiteUrlExample,
            "websiteKey": self.websiteKeyExample,
            "metadata": {},
        }
        self.assertRaises(TypeError, FriendlyCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["apiGetLib"] = self.apiGetLibExample
        FriendlyCustomTaskRequest(**base_kwargs)

    def test_friendly_missing_fields(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        base_kwargs = {}
        self.assertRaises(ValidationError, FriendlyCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, FriendlyCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteKey": self.websiteKeyExample})
        self.assertRaises(ValidationError, FriendlyCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"metadata": metadata_example})
        FriendlyCustomTaskRequest(**base_kwargs)

    def test_friendly_optional_proxy_and_useragent(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        request = FriendlyCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=metadata_example,
            proxy=self.proxy,
            userAgent=self.userAgentExample,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["proxyType"], self.proxy.proxyType)
        self.assertEqual(task_dictionary["userAgent"], self.userAgentExample)

    def test_friendly_proxy_not_required(self):
        metadata_example = {
            "apiGetLib": self.apiGetLibExample,
        }
        request = FriendlyCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=metadata_example,
        )
        task_dictionary = request.getTaskDict()
        self.assertNotIn("proxyType", task_dictionary)


if __name__ == "__main__":
    unittest.main()
