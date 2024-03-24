from mitmproxy import http, ctx

class MyUniqueProxyServer:
    def _init_(self):
        self.requests = {}

    def request(self, flow: http.HTTPFlow):
        ctx.log.info(f"Request intercepted: {flow.request.url}")
        self.requests[flow.request.url] = flow.request

    def response(self, flow: http.HTTPFlow):
        ctx.log.info(f"Response intercepted: {flow.request.url}")

addons = [
    MyUniqueProxyServer()
]