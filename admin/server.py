"""
This module is the entry point for client to make connection with server
and to get services done by the server
"""
import asyncio
import signal
from user_details import UserDetails
from services.authentication import authenticate_user
from services.commands_management import call_commands
from services.authentication.entry.signout import signout

signal.signal(signal.SIGINT, signal.SIG_DFL)
# dictionary stores all the clients
user = {}


async def handle_echo(reader, writer):
    """
    Allous client to serve their commands
    """
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    # this loop continues until the user logs in.
    try:
        # bool- True: on user enter exit command
        close_connection = False
        if addr[1] not in user.keys():
            # if user is connected first time it will stores the user details in the user dictionary
            user[addr[1]] = UserDetails()
            message = """
            To login enter command: "login <username> <password>"
            To register enter command: "register <username> <password>"
            """
            writer.write(message.encode())
            while True:
                data = await reader.read(100000)
                message = data.decode().strip()
                if message == "exit" or message == "quit":
                    close_connection = True
                    break
                # path for all the data files location
                path = (user[addr[1]].get_root())+"/data"
                # calls the method to authenticate user
                reply = authenticate_user.authenticate(message, path, user[addr[1]].change_username)
                # If we get reply success then we will send this message to the 
                # user and allow the user to enter further commands and it will 
                # break the loop
                if reply["status"] == "Success":
                    reply = reply["message"]+"\n Now you are allowed to enter commands. " \
                                             "Enter <commands> to know what type of commands " \
                                             "are available."
                    writer.write(reply.encode())
                    break
                writer.write(reply["message"].encode())
                await writer.drain()
        if not close_connection:
            while True:
                data = await reader.read(1000000)
                message = data.decode().strip()
                # on command exit it will execute this command to logout of the user from the server
                if message == 'quit' or message == 'exit':
                    reply = signout(user[addr[1]].get_root(), user[addr[1]].get_username())
                    break
                # calls the method to execute the respective services
                reply = call_commands(message, user[addr[1]])
                print(f"Received {message} from {addr}")
                print(f"Send: {reply}")
                writer.write(reply.encode())
                await writer.drain()
            print(f"Closing the connection {addr}")
            writer.close()
        else:
            print(f"Closing the connection {addr}")
            writer.close()
    # on connection problems it will allow us to stop executing and it will logout the user.
    except ConnectionResetError:
        print("(:-Connection error. Signing out the user for security reasons.-:)")
        reply = signout(user[addr[1]].get_root(), user[addr[1]].get_username())


async def main():
    """
    Allows client to connect with the server
    """
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
