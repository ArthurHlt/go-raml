# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

import json
import aiohttp


class HTTPClient:
    def __init__(self, loop, base_uri="<no value>"):
        self.base_url = base_uri
        self.session = aiohttp.ClientSession(loop=loop)
        self.headers = {"Content-Type": "application/json"}

    def set_auth_header(self, val):
        """ set authorization header value """
        self.headers["Authorization"] = val

    def set_header(self, header, val):
        """ set header """
        self.headers[header] = val

    def close(self):
        self.session.close()

    def build_header(self, headers):
        hdrs = self.headers
        if headers is None:
            return hdrs

        for key in headers:
            hdrs[key] = headers[key]
        return hdrs

    async def do_request(self, uri, data, headers, params, content_type, method):
        hdrs = self.build_header(headers)
        if not isinstance(data, str):
            data = json.dumps(data)

        if content_type == "multipart/form-data":
            # when content type is multipart/formdata remove the content-type header
            # as requests will set this itself with correct boundary
            headers.pop('Content-Type')
            res = await method(uri, files=data, headers=headers, params=params)
        else:
            res = await method(uri, data=data, headers=hdrs, params=params)

        res.raise_for_status()
        return res

    async def get(self, uri, data, headers, params, content_type):
        return await self.do_request(uri, data, headers, params, content_type, self.session.get)

    async def delete(self, uri, data, headers, params, content_type):
        return await self.do_request(uri, data, headers, params, content_type, self.session.delete)

    async def post(self, uri, data, headers, params, content_type):
        return await self.do_request(uri, data, headers, params, content_type, self.session.post)

    async def put(self, uri, data, headers, params, content_type):
        return await self.do_request(uri, data, headers, params, content_type, self.session.put)

    async def patch(self, uri, data, headers, params, content_type):
        return await self.do_request(uri, data, headers, params, content_type, self.session.patch)
