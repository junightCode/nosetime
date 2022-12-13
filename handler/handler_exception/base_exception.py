# -*- coding: utf-8 -*-
import enum

class Code(object):
    def __init__(self, code, message_or_format, status_code=None, fmt_values=(), **kwargs):
        self.code = code
        self.message = message_or_format % fmt_values
        self.status_code = status_code


class ErrorCode(enum.Enum):

    AUTHORIZATION_ERROR = Code(461, '权限认证失败', 500)

    PAGE_NOT_FOUND_ERROR = Code(404, '地址不存在', 404)
    UNAUTHORIZED_ERROR = Code(401, '请求未认证', 401)
    FORBIDDEN_ERROR = Code(403, '无权限的请求', 403)
    TP_PROXY_ERROR = Code(10000, 'ip代理错误', 403)
    INTERNAL_ERROR = Code(500, '内部错误', 500)
    ARGUMENT_ERROR = Code(2, '参数错误', 422)
    RETRY_REEOR = Code(1000, '允许重试的异常')
    UNEXCEPTED_ERROR = Code(500, '未知异常')
    SYSTEM_ERROR = Code(1, '系统错误', 500)

class Error(Exception):
    """
    User error
    """
    " 0 ~ 1000 System Error "
    SYSTEM_ERROR = Code(1, '系统错误', 500)
    ARGUMENT_ERROR = Code(2, '参数错误', 422)

    UNAUTHORIZED_ERROR = Code(401, '请求未认证', 401)
    FORBIDDEN_ERROR = Code(403, '无权限的请求', 403)
    UNEXCEPTED_ERROR = Code(500, '未知异常')


    def __init__(self, code_or_exception, extra='', fmt_values=(), **kwargs):
        if isinstance(code_or_exception, Code):
            self.error_code = code_or_exception.code
            self.message = code_or_exception.message
            self.status_code = code_or_exception.status_code or 500

        elif isinstance(code_or_exception, BaseException):
            self.error_code = getattr(code_or_exception, 'error_code') or -1
            self.message = getattr(code_or_exception, 'message') or str(code_or_exception)
            self.status_code = getattr((code_or_exception, 'status_code')) or 500

        elif isinstance(code_or_exception, int):
            # TODO
            pass
        else:
            self.error_code = -1
            self.message = '未知异常'
            self.status_code = -1

        self.extra = (extra % fmt_values) if extra else ''

        super().__init__(self.message)

    def __str__(self):
        return 'status_code: %s, code: %s, %s %s' %(self.status_code, self.error_code, self.message, self.extra)

    def __repr__(self):
        return self.__str__()
