# CapMonster Python Captcha Solver & Anti-Bot Bypass API Library

[![PyPI version](https://img.shields.io/pypi/v/capmonstercloudclient.svg?style=flat-square)](https://pypi.org/project/capmonstercloudclient/)
[![PyPI downloads](https://img.shields.io/pypi/dm/capmonstercloudclient.svg?style=flat-square)](https://pypi.org/project/capmonstercloudclient/)
[![Python version](https://img.shields.io/pypi/pyversions/capmonstercloudclient.svg?style=flat-square)](https://pypi.org/project/capmonstercloudclient/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Official Python 3 package for easy integration with the [CapMonster Cloud](https://capmonster.cloud/) API — the fastest and most reliable automated captcha-solving service.

This wrapper allows you to seamlessly integrate high-speed AI captcha recognition into your Python web scraping, data extraction, and testing workflows. It is fully compatible with popular browser automation frameworks like **Selenium, Playwright, Puppeteer, Scrapy, and BeautifulSoup**.

🔥 **[Create a Free Account & Get Your API Key](https://dash.capmonster.cloud/Account/SignUp?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)** to start bypassing bot protections instantly!

## 🛠️ Key Features

- ⚡ **Fast & Fully Automated:** Solve captchas in seconds without human intervention.
- 🤖 **100% AI-Powered:** Machine learning algorithms ensure the highest success rate.
- 🌐 **Browser Automation Ready:** Easily plug into your Selenium or Playwright scripts.
- 🛡️ **Advanced WAF Bypass:** Effortlessly bypass Cloudflare Turnstile, DataDome, Amazon WAF, and Imperva.
- 💰 **Cost-Effective:** One of the most affordable solutions on the market for scale.

## ⚙️ Installation

Install the CapMonster Cloud Python client using pip:

```bash
pip install capmonstercloudclient
```

## 🚀 Quick Start & Usage Example

**Prerequisite:** You need an active CapMonster API key. [Grab it from your dashboard](https://dash.capmonster.cloud/Account/SignUp?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme).

Below is a standard example of solving a reCAPTCHA v2 (Proxyless) using `asyncio`. You can easily pass the resulting token into your Selenium or Playwright browser instances.

```python
import asyncio

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

# Initialize the client with your CapMonster Cloud API key
client_options = ClientOptions(api_key="<YOUR_API_KEY>")
cap_monster_client = CapMonsterClient(options=client_options)

async def solve_captcha():
    # Setup the reCAPTCHA v2 request
    recaptcha2request = RecaptchaV2ProxylessRequest(
        websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
        websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd"
    )
    # Await the solution token
    return await cap_monster_client.solve_captcha(recaptcha2request)

if __name__ == "__main__":
    responses = asyncio.run(solve_captcha())
    print("Captcha Solved! Token:", responses)
```

## 🧩 Supported Captcha Recognition Types

Our Python API wrapper supports almost all modern anti-bot challenges. Click on the links below to view detailed API documentation and payload examples.

### 🔹 Classic Captchas
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task) - Amazon WAF Bypass
- [BinanceTaskRequest](https://docs.capmonster.cloud/docs/captchas/binance) - Binance Captcha Solver
- [BinanceTaskProxylessRequest](https://docs.capmonster.cloud/docs/captchas/binance)
- [GeeTestProxylessRequest](https://zenno.link/doc-geetest-en) - GeeTest Solver
- [GeeTestRequest](https://zenno.link/doc-geetest-proxy-en)
- [ImageToTextRequest](https://zenno.link/doc-ImageToTextTask-en) - Standard OCR (Image-to-Text)
- [RecaptchaV2ProxylessRequest](https://zenno.link/doc-recaptcha2-en) - Google reCAPTCHA v2
- [RecaptchaV2Request](https://zenno.link/doc-recaptcha2-proxy-en)
- [RecaptchaV3ProxylessRequest](https://zenno.link/doc-recaptcha3-en) - Google reCAPTCHA v3
- [RecaptchaV2EnterpriseProxylessRequest](https://zenno.link/doc-recaptcha2e-en)
- [RecaptchaV2EnterpriseRequest](https://zenno.link/doc-recaptcha2e-proxy-en)
- [TurnstileProxylessRequest](https://zenno.link/doc-turnstile-en) - Cloudflare Turnstile Challenge
- [TurnstileRequest](https://zenno.link/doc-turnstile-proxy-en)

### 🔹 Custom Tasks (Anti-Bot & Advanced WAFs)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome) - DataDome Slider & Interstitial bypass
- [ImpervaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/incapsula) - Imperva / Incapsula bypass
- [ImpervaCustomTaskProxylessRequest](https://docs.capmonster.cloud/docs/captchas/incapsula)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi)

### 🔹 Complex Image Tasks
- [RecaptchaComplexImageTaskRequest](https://zenno.link/doc-complextask-rc-en) (Grid / Dynamic Image Selection)

---

### 💡 Ready to supercharge your web automation?
Join thousands of developers effortlessly bypassing captchas.  
👉 **[Sign up for CapMonster Cloud](https://capmonster.cloud/) today and boost your scraper's success rate!**
