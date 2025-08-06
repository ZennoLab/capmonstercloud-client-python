import unittest

from capmonstercloudclient.requests import ProxyInfo


FIELDS = ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]


class ProxyFieldsTest(unittest.TestCase):
    proxyPort: int = 8000
    proxyType: str = "https"
    proxyAddress: str = "proxyAddress"
    proxyLogin: str = "proxyLogin"
    proxyPassword: str = "proxyPassword"

    def testFields(self):
        p = ProxyInfo(
            proxyType=ProxyFieldsTest.proxyType,
            proxyAddress=ProxyFieldsTest.proxyAddress,
            proxyPort=ProxyFieldsTest.proxyPort,
            proxyLogin=ProxyFieldsTest.proxyLogin,
            proxyPassword=ProxyFieldsTest.proxyPassword,
        )
        d = p.model_dump()
        for field in FIELDS:
            self.assertTrue(
                field in d, msg=f'Expected that "{field}" will be in {list(d.keys())}'
            )


if __name__ == "__main__":
    unittest.main()
