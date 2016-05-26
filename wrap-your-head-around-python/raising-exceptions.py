try:
    raise Exception('testing exception')
except Exception as e:
    print(type(e))
    print(e)
    print('exception raised')

try:
    raise SystemError('testing system error')
except SystemError as e:
    print('system error raised')
except Exception as e:
    print('general exception raised')

class MyException(RuntimeError):
    def __init__(self, arg):
        self.args = arg,

try:
    raise MyException('custom exception')
except NameError as e:
    print('name exception raised')
except MyException as e:
    print(e.args)
except Exception as e:
    print('general exception raised')