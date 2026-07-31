from typing import List
from enum import Enum, unique


class BaseEnum(Enum):
    """
    Base enum class providing convenience helpers shared by the
    module-specific enumerations defined below.
    """

    @classmethod
    def list_values(cls) -> List[str]:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_names(cls) -> List[str]:
        return list(map(lambda c: c.name, cls))

@unique
class TextModules(BaseEnum):
    """
    Enumerates the recognizable text-captcha module identifiers accepted
    by CapMonster Cloud's ImageToTextTask, used to select service-specific
    recognition logic for known text captcha providers.
    """
    amazon_captcha = 'amazon'
    botdetect_captcha = 'botdetect'
    facebook_captcha = 'facebook'
    gmx_captcha = 'gmx'
    google_captcha = 'google'
    hotmail_captcha = 'hotmail'
    mailru_captcha = 'mailru'
    ok_captcha = 'ok'
    oknew_captcha = 'oknew'
    ramblerrus_captcha = 'ramblerrus'
    solvemedia_captcha = 'solvemedia'
    steam_captcha = 'steam'
    vk_captcha = 'vk'
    yandex_captcha = 'yandex'
    yandexnew_captcha = 'yandexnew'
    yandexwave_captcha = 'yandexwave'
    universal_captcha = 'universal'

@unique
class ProxyTypes(BaseEnum):
    """
    Enumerates the proxy protocols supported when routing a captcha-solving
    request through a proxy server.
    """
    http_proxy = 'http'
    https_proxy = 'https'
    socks4_proxy = 'socks4'
    socks5_proxy = 'socks5'