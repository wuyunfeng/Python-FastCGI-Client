from FastCGIClient import *
import sys
from urlparse import urlparse as parse_url


def main():
    argvs = sys.argv
    argc = len(argvs)
    if argc < 3:
        print('Usage: python fcgi.py http://127.0.0.1:9000/path/to/some.php?queryString path/to/documentroot postData')
        print('Example: python fcgi.py http://127.0.0.1:9000/echo.php\?name\=john '
              '/Users/baidu/php_workspace name=john&address=beijing')
        return
    argv = argvs[1]
    documentRoot = argvs[2]
    parseResult = parse_url(argv)
    host = parseResult.hostname
    port = parseResult.port
    uri = parseResult.path
    query = parseResult.query
    client = FastCGIClient(host, port, 3000, 0)
    content = ''
    if argc > 3:
        content = argvs[3]
    # content = "name=john&address=beijing"
    params = {'GATEWAY_INTERFACE': 'FastCGI/1.0',
              'REQUEST_METHOD': 'POST',
              'SCRIPT_FILENAME': documentRoot + uri,
              'SCRIPT_NAME': uri,
              'QUERY_STRING': query,
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


if __name__ == '__main__':
    main()
