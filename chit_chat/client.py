import sys
import asyncio
import chit_chat.constants as con


async def tcp_echo_client(message, host, port):
    reader, writer = await asyncio.open_connection(host=host, port=port)
    
    print(f'Send: {message!r}')
    writer.write(message.encode())
    
    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')
    
    print('Close the connection')
    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 1:
        print('Please supply a message')
        print('Usage: python client.py MESSAGE HOST PORT')
    message = sys.argv[1]
    
    if num_args < 3:
        host = con.HOST
        port = con.PORT
    else:
        host = sys.argv[2]
        port = sys.argv[3]
    
    asyncio.run(tcp_echo_client(message, host, port))
    