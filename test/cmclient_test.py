import asyncio
import unittest
import os

from capmonstercloudclient.requests import RecaptchaV2Request
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.exceptions import UnknownRequestInstanceError


api_key = os.getenv("API_KEY")


class InstanceRequestTest(unittest.IsolatedAsyncioTestCase):
    def testSuccessResponse(self):
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        request = RecaptchaV2Request(
            websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
            websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd",
        )
        # Success
        response_1 = asyncio.run(client.solve_captcha(request))
        self.assertTrue(isinstance(response_1, dict))

    def testFailedInstanceRequest(self):
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        # Failed
        with self.assertRaises(
            UnknownRequestInstanceError,
            msg="Unknown instance of request must call <UnknownRequestInstanceError>.",
        ):
            asyncio.run(client.solve_captcha("hmmm"))


if __name__ == "__main__":
    unittest.main()
