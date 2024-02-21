# Zennolab.CapMonsterCloud.Client

Official python client library for [capmonster.cloud](https://capmonster.cloud/) captcha recognition service

## Installation

    python3 -m pip install capmonstercloudclient

## Usage

***
    import asyncio

    from capmonstercloudclient import CapMonsterClient, ClientOptions
    from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

    client_options = ClientOptions(api_key=<YOUR_API_KEY>)
    cap_monster_client = CapMonsterClient(options=client_options)

    async def solve_captcha():
        return await cap_monster_client.solve_captcha(recaptcha2request)

    recaptcha2request = RecaptchaV2ProxylessRequest(websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
                                                    websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd")

    responses = asyncio.run(solve_captcha())
    print(responses)
***

Supported captcha recognition requests:

- [RecaptchaV2Task](https://zenno.link/doc-recaptcha2-en)
- [RecaptchaV3TaskProxyless](https://zenno.link/doc-recaptcha3-en)
- [ReCaptchaV2EnterpriseTask](https://zenno.link/doc-recaptcha2e-en)
- [HCaptchaTask](https://zenno.link/doc-hcaptcha-en)
- [GeeTestTask](https://zenno.link/doc-geetest-en)
- [TurnstileTask](https://zenno.link/doc-turnstile-en)
- [ComplexImageTask Recaptcha](https://zenno.link/doc-complextask-rc-en)
- [ComplexImageTask HCaptcha](https://zenno.link/doc-complextask-hc-en)
- [ImageToTextTask](https://zenno.link/doc-ImageToTextTask-en)