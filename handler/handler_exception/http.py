# -*- coding: utf-8 -*-
from .base_exception import Error as BaseError
from .base_exception import Code


class HttpError(BaseError):

    PAGE_NOT_FOUND_ERROR = Code(404, '地址不存在', 404)
    INTERNAL_ERROR = Code(500, '内部错误', 500)
    AUTHORIZATION_ERROR = Code(461, '权限认证失败', 500)
    RETRY_REEOR = Code(1000, '允许重试的异常')

    def __init__(self, code_or_exception, extra='', **kwargs):
        super().__init__(code_or_exception, extra, **kwargs)


