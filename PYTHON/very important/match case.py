# match case statement
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))

# match case statement with multiple patterns
def http_error(status):
    match status:
        case 400 | 401 | 403 | 404:
            return "Client error"
        case 500 | 501 | 502 | 503:
            return "Server error"
        case _:
            return "Something's wrong with the internet"
print(http_error(400))
print(http_error(401))
print(http_error(500))
print(http_error(501))