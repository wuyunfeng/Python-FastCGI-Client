from FastCGIClient import *

client = FastCGIClient('127.0.0.1', 9000, 3000, 0)
params = dict()
documentRoot = "/Users/baidu/php_workspace"
uri = "/echo.php"
content = "name=john&address=beijing"
params = {'GATEWAY_INTERFACE': 'FastCGI/1.0',
          'REQUEST_METHOD': 'POST',
          'SCRIPT_FILENAME': documentRoot + uri,
          'SCRIPT_NAME': uri,
          'QUERY_STRING': '',
          'REQUEST_URI': uri,
          'DOCUMENT_ROOT': documentRoot,
          'SERVER_SOFTWARE': 'php/fcgiclient',
          'REMOTE_ADDR': '127.0.0.1',
          'REMOTE_PORT': '9985',
          'SERVER_ADDR': '127.0.0.1',
          'SERVER_PORT': '80',
          'SERVER_NAME': "localhost",
          'SERVER_PROTOCOL': 'HTTP/1.1',
          'CONTENT_TYPE': 'application/x-www-form-urlencoded',
          'CONTENT_LENGTH': len(content)
          }
print(client.request(params, content))
