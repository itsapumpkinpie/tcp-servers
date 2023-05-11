import socket

HOST, PORT = '', 8080

# Создаем сокет и настраиваем его для прослушивания подключений
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT}...')

while True:
    # Принимаем входящее соединение
    client_connection, client_address = listen_socket.accept()
    # Получаем данные от клиента
    request = client_connection.recv(1024)
    print(request.decode('utf-8'))

    # Разбираем запрос
    request_lines = request.decode('utf-8').split('\r\n')
    request_method, path, request_version = request_lines[0].split()

    # Отправляем ответ клиенту
    if request_method == 'GET':
        if path == '/':
            http_response = b"""\
HTTP/1.1 200 OK

Hi from main page!
"""
        elif path == '/about':
            http_response = b"""\
HTTP/1.1 200 OK

Hi from about-page :)))
"""
        else:
            http_response = b"""\
HTTP/1.1 404 Not Found

404 Not Found
"""
    else:
        http_response = b"""\
HTTP/1.1 501 Not Implemented

501 Not Implemented
"""

    client_connection.sendall(http_response)
    # Закрываем соединение
    client_connection.close()
