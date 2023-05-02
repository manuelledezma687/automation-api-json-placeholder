# READ ME

## for get schemas from models, paste your json body and get schema on this web:

- https://www.liquid-technologies.com/online-json-to-schema-converter

## If you want to make a pre-request o make and encode here is an example.

~~~

import base64
import json
import re
import requests

    def _generate_external_id(self, app, provider):
        data = {
            "app": app,
            "provider": provider
        }
        data_string = json.dumps(data)
        data_bytes = data_string.encode('utf-8')
        base64_string = base64.urlsafe_b64encode(data_bytes).decode('utf-8')
        base64_string = re.sub(r'=+$', '', base64_string)
        base64_string = re.sub(r'\+', '-', base64_string)
        base64_string = re.sub(r'/', '_', base64_string)
        return base64_string

    def _get_bearer_token(self):
        body = {"grant_type": "client_credentials"}
        headers = {
            "Authorization": f"Basic {self.__props('auth')}",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.post(url=self.__props(
            "authUrl"), headers=headers, data=body, verify=False , timeout=30)
        response.raise_for_status()
        return response.json()["id_token"]

    def external_id(self):
        return self._generate_external_id(
            self.__props("app"),
            self.__props("provider")
        )
~~~