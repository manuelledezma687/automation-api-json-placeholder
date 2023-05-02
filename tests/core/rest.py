import json
from logging import Logger
from typing import Dict, Optional

import requests
from requests import Response
import curl
from prettyconf import Configuration
import allure


class Rest:

    __resp: Response

    def __init__(self, log: Logger, props: Configuration):
        self.props = props
        self.log = log

    def __set_default_headers(self, headers: Dict, authorization: Optional[str] = None, basic_authorization: Optional[str] = None):
        if not headers:
            headers = {}
        if "Content-Type" not in headers:
            headers["Content-Type"] = "application/json"
        if "User-Agent" not in headers:
            headers["User-Agent"] = self.props("userAgent")
        if authorization:
            headers["Authorization"] = f"Bearer {authorization}"
        if basic_authorization:
            headers["Authorization"] = f"Basic {basic_authorization}"
        return headers

    def get(self, url: str, headers: Optional[Dict] = None, params: Optional[Dict] = None,
            authorization: Optional[str] = None, basic_authorization: Optional[str] = None, verify=False) -> Response:
        self.__resp = requests.get(url, headers=self.__set_default_headers(headers, authorization, basic_authorization),
                                   params=params,
                                   timeout=30,
                                   verify=verify)
        self.__capture()
        return self.__resp

    def post(self, url: str, headers: Optional[Dict] = None, body: Optional[Dict] = None,
             params: Optional[Dict] = None, authorization: Optional[str] = None, verify=False) -> Response:
        self.__resp = requests.post(url, headers=self.__set_default_headers(headers, authorization),
                                    data=json.dumps(body),
                                    params=params, timeout=30, verify=verify)
        self.__capture()
        return self.__resp

    def put(self, url: str, headers: Optional[Dict] = None, params: Optional[Dict] = None,
            authorization: Optional[str] = None, basic_authorization: Optional[str] = None, verify=False) -> Response:

        self.__resp = requests.put(url, headers=self.__set_default_headers(headers, authorization, basic_authorization),
                                   params=params,timeout=30,
                                   verify=verify)
        self.__capture()
        return self.__resp

    def delete(self, url: str, headers: Optional[Dict] = None, params: Optional[Dict] = None,
            authorization: Optional[str] = None, basic_authorization: Optional[str] = None, verify=False) -> Response:

        self.__resp = requests.delete(url, headers=self.__set_default_headers(headers, authorization, basic_authorization),
                                   params=params, timeout=30,
                                   verify=verify)
        self.__capture()
        return self.__resp

    def __capture(self):
        curl_command = curl.parse(self.__resp, return_it=True, print_it=False)
        allure.attach(curl_command, name="curl")
        allure.attach(self.__resp.content, name="response")
        allure.attach(
            f"{(self.__resp.elapsed.total_seconds() * 1000):.2f}ms", name="response time")
        self.log.info(curl_command)
