import unittest

from pydantic import ValidationError

from capmonstercloudclient.requests import BinanceTaskRequest


class BinanceRequestTest(unittest.TestCase):
    websiteUrlExample = "https://binance.com/login"
    websiteKeyExample = "login"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    def test_binance(
        self,
    ):
        required_fields = ["type", "websiteURL", "websiteKey", "validateId"]
        request = BinanceTaskRequest(
            websiteKey=self.websiteKeyExample,
            websiteUrl=self.websiteUrlExample,
            validateId="asdgf",
        )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(
                f in list(task_dictionary.keys()),
                msg=f'Required captcha input key "{f}" does not include to request.',
            )

    def test_binance_missing(
        self,
    ):
        required_fields = ["type", "websiteURL", "websiteKey", "validateId"]
        base_kwargs = {}
        self.assertRaises(ValidationError, BinanceTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteUrl": self.websiteUrlExample})
        self.assertRaises(ValidationError, BinanceTaskRequest, **base_kwargs)
        base_kwargs.update({"websiteKey": self.websiteKeyExample})
        self.assertRaises(ValidationError, BinanceTaskRequest, **base_kwargs)
        base_kwargs.update({"validateId": "asdgf"})
        BinanceTaskRequest(**base_kwargs)
        base_kwargs.update({"userAgent": self.userAgentExample})
        BinanceTaskRequest(**base_kwargs)


if __name__ == "__main__":
    unittest.main()
