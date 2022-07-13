"""
This is entry module for client to make connection with server and
to use the services provided by the server
"""
import asyncio


async def tcp_echo_client():
    """
    Makes tcp connection with server
    """
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    data = await reader.read(1000000)
    print(data.decode())
    message = ''
    while True:
        message = input('Enter Command here:\n$')
        if message == "":
            continue
        writer.write(message.encode())
        if message == 'exit' or message == 'quit':
            break

        data = await reader.read(100000)
        print(f'Received:\n {data.decode()}')
    print('Close the connection')
    writer.close()


asyncio.run(tcp_echo_client())
