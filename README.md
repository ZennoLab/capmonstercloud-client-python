# Zennolab.CapMonsterCloud.Client

Official Python client library for [capmonster.cloud](https://capmonster.cloud/) — an AI-powered CAPTCHA solving and anti-bot bypass API.

## Installation

```bash
python3 -m pip install capmonstercloudclient
```

## 🚀 Quick Start

1. Get your API key in the [CapMonster Cloud Dashboard](https://dash.capmonster.cloud/).
2. Install the package (see above).
3. Copy a snippet below, replace `YOUR_API_KEY`, and run it.

### Bypass reCAPTCHA v2

```python
import asyncio

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2Request


async def main():
    client_options = ClientOptions(api_key="YOUR_API_KEY")
    cap_monster_client = CapMonsterClient(options=client_options)

    recaptcha2_request = RecaptchaV2Request(
        websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
        websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd",
    )

    solution = await cap_monster_client.solve_captcha(recaptcha2_request)
    print(solution)  # {'gRecaptchaResponse': '...'}


asyncio.run(main())
```

### Bypass Cloudflare Turnstile

```python
import asyncio

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import TurnstileRequest


async def main():
    client_options = ClientOptions(api_key="YOUR_API_KEY")
    cap_monster_client = CapMonsterClient(options=client_options)

    turnstile_request = TurnstileRequest(
        websiteURL="https://tsinvisble.zlsupport.com",
        websiteKey="0x4AAAAAAABUY0VLtOUMAHxE",
    )

    solution = await cap_monster_client.solve_captcha(turnstile_request)
    print(solution)  # {'token': '...'}


asyncio.run(main())
```

More end-to-end examples (proxies, image-based captchas, custom anti-bot tasks) are available in the [`examples/`](examples/) directory.

## ⚡ Supported CAPTCHA Recognition Requests

### Classic captcha tasks

- [ImageToTextRequest](https://docs.capmonster.cloud/docs/captchas/image-to-text)
- [RecaptchaV2Request](https://docs.capmonster.cloud/docs/captchas/no-captcha-task)
- [RecaptchaV2EnterpriseRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v2-enterprise-task)
- [RecaptchaV3ProxylessRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-task)
- [FuncaptchaRequest](https://docs.capmonster.cloud/docs/captchas/funcaptcha-task)
- [GeetestRequest](https://docs.capmonster.cloud/docs/captchas/geetest-task)
- [TurnstileRequest — Cloudflare Turnstile](https://docs.capmonster.cloud/docs/captchas/turnstile-task)
- [TurnstileRequest — Cloudflare Challenge](https://docs.capmonster.cloud/docs/captchas/turnstile-challenge-task)
- [TurnstileRequest — Cloudflare Waiting Room](https://docs.capmonster.cloud/docs/captchas/turnstile-waitroom-task)
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task)
- [BinanceTaskRequest](https://docs.capmonster.cloud/docs/captchas/binance)
- [MTCaptchaRequest](https://docs.capmonster.cloud/docs/captchas/mtcaptcha-task)
- [ProsopoTaskRequest](https://docs.capmonster.cloud/docs/captchas/prosopo-task)
- [YidunRequest](https://docs.capmonster.cloud/docs/captchas/yidun-task)

### Custom tasks (anti-bot / WAF / custom challenge systems)

- [AlibabaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/alibaba-task)
- [AltchaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/altcha-task)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome)
- [FriendlyCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/friendly-task)
- [HuntCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/hunt-task)
- [ImpervaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/incapsula)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi)
- [TspdCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tspd-task)

### Complex image tasks (grid / dynamic image selection tasks)

- [RecaptchaComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-click)
- [RecognitionComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/compleximage/rotation/baidu)

---
**[Official Documentation](https://docs.capmonster.cloud/docs/getting-start/)** | **[Register Account](https://dash.capmonster.cloud/)**
