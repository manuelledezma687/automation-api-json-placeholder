from logging import Logger
from typing import Dict, Optional

from requests import Response
from prettyconf import Configuration
import allure

from tests.core.rest import Rest


class ServiceBase:

    def __init__(self, log: Logger, rest: Rest, props: Configuration):
        self.__log = log
        self.__rest = rest
        self.__props = props
        self.__url = f"{self.__props('baseUrl')}"

    @allure.step("Get Posts")
    def get_posts(self, headers:  Optional[Dict] = None, params: Optional[Dict] = None, authorization: Optional[str] = None, path=Optional[str]) -> Response:
        url = f"{self.__url}/{path}"
        return self.__rest.get(url, headers=headers, params=params, authorization=authorization)

    @allure.step("Create a Post")
    def post_resource(self, headers:  Optional[Dict] = None, params: Optional[Dict] = None, authorization: Optional[str] = None, path=Optional[str], body=Optional[Dict]) -> Response:
        url = f"{self.__url}/{path}"
        return self.__rest.post(url, headers=headers, params=params, body=body, authorization=authorization)

    @allure.step("Update Post")
    def update_post(self, headers:  Optional[Dict] = None, params: Optional[Dict] = None, authorization: Optional[str] = None, path=Optional[str], body=Optional[Dict]) -> Response:
        url = f"{self.__url}/{path}"
        return self.__rest.put(url, headers=headers, params=params, authorization=authorization)

    @allure.step("Delete Post")
    def delete_post(self, headers:  Optional[Dict] = None, params: Optional[Dict] = None, authorization: Optional[str] = None, path=Optional[str]) -> Response:
        url = f"{self.__url}/{path}"
        return self.__rest.delete(url, headers=headers, params=params, authorization=authorization)
