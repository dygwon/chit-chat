import sys
import asyncio
import chit_chat.constants as con


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host=host, port=port)
    
    while True:
        message = input(f'Client: ')
        if message == con.EXIT:
            break
        
        writer.write(message.encode())
    
        data = await reader.read()
        print(f'Server: {data.decode()!r}')
    
    print('Close the connection')
    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':    
    if len(sys.argv) < 3:
        host = con.HOST
        port = con.PORT
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
    
    asyncio.run(tcp_echo_client(host, port))
    