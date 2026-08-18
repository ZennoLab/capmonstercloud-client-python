# CapMonster Cloud Python SDK: AI Captcha Solver & Anti-Bot Bypass

<p align="center">
  <a href="https://capmonster.cloud/en/?utm_source=github&utm_medium=readme&utm_campaign=python_repo">
    <img src="https://img.shields.io/badge/CapMonster%20Cloud-Python%20Captcha%20Solver-00B2FF?style=for-the-badge&logo=python&logoColor=white" alt="CapMonster Cloud Python SDK" height="40">
  </a>
</p>

<p align="center">
  <strong>Fast, AI-driven CAPTCHA solving client for Python. Seamlessly bypass Cloudflare Turnstile, reCAPTCHA v2/v3/Enterprise, DataDome, GeeTest, and Amazon WAF in web scraping and browser automation.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/v/capmonstercloudclient.svg?style=flat-square&color=blue" alt="PyPI version"></a>
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/dm/capmonstercloudclient.svg?style=flat-square&color=green" alt="PyPI downloads"></a>
  <a href="https://pypi.org/project/capmonstercloudclient/"><img src="https://img.shields.io/pypi/pyversions/capmonstercloudclient.svg?style=flat-square" alt="Python Versions"></a>
  <a href="https://github.com/ZennoLab/capmonstercloud-client-python/stargazers"><img src="https://img.shields.io/github/stars/ZennoLab/capmonstercloud-client-python?style=flat-square&color=yellow" alt="GitHub Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square" alt="License: MIT"></a>
</p>

---

Official asynchronous Python SDK for [CapMonster Cloud](https://capmonster.cloud/?utm_source=github&utm_medium=readme&utm_campaign=python_repo). Easily plug ultra-fast AI captcha recognition into **Playwright, Selenium, Puppeteer, Scrapy, BeautifulSoup, and Requests** automation workflows without human-in-the-loop delays.

**[👉 Get your Free API Key & Free Trial Balance on CapMonster Cloud](https://dash.capmonster.cloud/Account/SignUp?utm_source=github&utm_medium=referral&utm_campaign=python_repo_readme)**

---

## ⚡ Highlights & Benchmarks

- ⚡ **Sub-Second Speed:** 100% automated neural networks solve captchas in as fast as 0.3–2.5 seconds.
- 🤖 **Zero Human Workers:** Reliable, consistent uptime without mechanical turk latencies.
- 🌐 **Native Automation Wrappers:** Plug-and-play code snippets for **Playwright & Selenium**.
- 🛡️ **Modern Anti-Bot Bypass:** Full support for Cloudflare Turnstile, DataDome, GeeTest v4, Amazon WAF, and Imperva.
- 💰 **Lowest Cost per 1,000 Solutions:** High accuracy rate with competitive pay-as-you-go pricing.

---

## 📦 Installation

```bash
pip install capmonstercloudclient
```

---

## 🚀 Quick Start Examples

### 1. Simple Async Example (reCAPTCHA v2 Proxyless)

```python
import asyncio
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

# 1. Initialize client with your API key
options = ClientOptions(api_key="YOUR_CAPMONSTER_API_KEY")
client = CapMonsterClient(options=options)

async def main():
    # 2. Build the task payload
    request = RecaptchaV2ProxylessRequest(
        websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
        websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd"
    )
    
    # 3
