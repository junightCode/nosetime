# -*- coding: utf-8 -*-
from .base_exception import Error as BaseError
from .base_exception import Code


class ThirdPartyError(BaseError):
    TP_PROXY_ERROR = Code(10000, 'ip代理错误', 403)

    def __init__(self, code_or_exception, extra=None, **kwargs):
        super().__init__(code_or_exception, extra, **kwargs)

