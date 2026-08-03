from pydantic import BaseModel, Field, field_validator
from .enums import ProxyTypes
from typing import Optional

class ProxyInfo(BaseModel):
    """
    Represents the proxy connection details used to route a captcha-solving request.

    Attributes:
        proxyType: The protocol of the proxy server: "http", "https", "socks4", or "socks5".
        proxyAddress: The IPv4/IPv6 address or hostname of the proxy server.
        proxyPort: The port number on which the proxy server accepts connections.
        proxyLogin: The username used to authenticate with the proxy server.
        proxyPassword: The password used to authenticate with the proxy server.
    """
    proxyType: str = Field(..., description='The protocol of the proxy server: "http", "https", "socks4", or "socks5".')
    proxyAddress: str = Field(..., description='The IPv4/IPv6 address or hostname of the proxy server.')
    proxyPort: int = Field(..., description='The port number on which the proxy server accepts connections.')
    proxyLogin: str = Field(..., description='The username used to authenticate with the proxy server.')
    proxyPassword: str = Field(..., description='The password used to authenticate with the proxy server.')

    @field_validator('proxyType')
    @classmethod
    def validate_proxy_type(cls, value):
        if value not in ProxyTypes.list_values():
            raise ValueError(f'proxyType must be one of {ProxyTypes.list_values()}, got "{value}".')
        return value

    @field_validator('proxyPort')
    @classmethod
    def validate_port(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'proxyPort must be <int> type, got {type(value)}.')
        return value

class ClientProxyInfo(BaseModel):
    """
    Represents the proxy connection details supplied by the client, with optional
    authentication credentials.

    Attributes:
        proxyType: The protocol of the proxy server: "http", "https", "socks4", or "socks5".
        proxyAddress: The IPv4/IPv6 address or hostname of the proxy server.
        proxyPort: The port number on which the proxy server accepts connections.
        proxyLogin: The username used to authenticate with the proxy server,
            if authentication is required.
        proxyPassword: The password used to authenticate with the proxy server,
            if authentication is required.
    """
    proxyType: str = Field(..., description='The protocol of the proxy server: "http", "https", "socks4", or "socks5".')
    proxyAddress: str = Field(..., description='The IPv4/IPv6 address or hostname of the proxy server.')
    proxyPort: int = Field(..., description='The port number on which the proxy server accepts connections.')
    proxyLogin: Optional[str] = Field(default=None, description='The username used to authenticate with the proxy server, if authentication is required.')
    proxyPassword: Optional[str] = Field(default=None, description='The password used to authenticate with the proxy server, if authentication is required.')

    @field_validator('proxyType')
    @classmethod
    def validate_proxy_type(cls, value):
        if value not in ProxyTypes.list_values():
            raise ValueError(f'proxyType must be one of {ProxyTypes.list_values()}, got "{value}".')
        return value

    @field_validator('proxyPort')
    @classmethod
    def validate_port(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'proxyPort must be <int> type, got {type(value)}.')
        return value