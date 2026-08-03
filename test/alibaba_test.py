import unittest

from pydantic import ValidationError
from capmonstercloudclient.requests import AlibabaCustomTaskRequest, ProxyInfo


class AlibabaCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    sceneIdExample = "1ww7426c"
    prefixExample = "dlw3kug"

    def setUp(self):
        self.proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere"
        )

    def test_alibaba_request_required_fields(self):
        required_fields = ["type", "class", "websiteURL", "metadata"]
        metadata_required_fields = ["sceneId", "prefix"]
        metadata_example = {
            "sceneId": self.sceneIdExample,
            "prefix": self.prefixExample,
        }
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
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
        self.assertEqual(task_dictionary["class"], "alibaba")
        self.assertEqual(task_dictionary["type"], "CustomTask")

    def test_alibaba_metadata_validation(self):
        base_kwargs = {
            "websiteUrl": self.websiteUrlExample,
            "metadata": {},
        }
        self.assertRaises(TypeError, AlibabaCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["sceneId"] = self.sceneIdExample
        self.assertRaises(TypeError, AlibabaCustomTaskRequest, **base_kwargs)
        base_kwargs["metadata"]["prefix"] = self.prefixExample
        AlibabaCustomTaskRequest(**base_kwargs)

    def test_alibaba_metadata_invalid_key(self):
        base_kwargs = {
            "websiteUrl": self.websiteUrlExample,
            "metadata": {
                "sceneId": self.sceneIdExample,
                "prefix": self.prefixExample,
                "unknownField": "value",
            },
        }
        self.assertRaises(TypeError, AlibabaCustomTaskRequest, **base_kwargs)

    def test_alibaba_metadata_extended_fields(self):
        metadata_example = {
            "sceneId": self.sceneIdExample,
            "prefix": self.prefixExample,
            "userId": "HpadJlQnz2zSKcSmjXBaqQvjYUvP4jMJIk/ZwGNDNiM=",
            "userUserId": "/uSXKkVFuuwxXA21/MpXGxpLStWBEup1B3jjlMUWwNE=",
            "verifyType": "1.0",
            "region": "sgp",
            "UserCertifyId": "0a03e59417757735511105780e2a5e",
            "apiGetLib": "https://o.example.com/captcha-frontend/aliyunCaptcha/AliyunCaptcha.js?t=2041",
            "cookieRequired": True,
        }
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["metadata"], metadata_example)

    def test_alibaba_missing_fields(self):
        metadata_example = {
            "sceneId": self.sceneIdExample,
            "prefix": self.prefixExample,
        }
        base_kwargs = {}
        self.assertRaises(ValidationError, AlibabaCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, AlibabaCustomTaskRequest, **base_kwargs)
        base_kwargs.update({"metadata": metadata_example})
        AlibabaCustomTaskRequest(**base_kwargs)

    def test_alibaba_optional_proxy_and_useragent(self):
        metadata_example = {
            "sceneId": self.sceneIdExample,
            "prefix": self.prefixExample,
        }
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
            proxy=self.proxy,
            userAgent=self.userAgentExample,
        )
        task_dictionary = request.getTaskDict()
        self.assertEqual(task_dictionary["proxyType"], self.proxy.proxyType)
        self.assertEqual(task_dictionary["userAgent"], self.userAgentExample)

    def test_alibaba_proxy_not_required(self):
        metadata_example = {
            "sceneId": self.sceneIdExample,
            "prefix": self.prefixExample,
        }
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=metadata_example,
        )
        task_dictionary = request.getTaskDict()
        self.assertNotIn("proxyType", task_dictionary)


if __name__ == "__main__":
    unittest.main()
