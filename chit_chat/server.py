import sys
import asyncio
import constants as con


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    
    print(f'Received {message!r} from {addr!r}')
    
    print(f'Send: {message!r}')
    writer.write(data)
    await writer.drain()
    
    print('Close the connection')
    writer.close()
    await writer.wait_closed()
    
    
async def main(host: str, port: int):
    server = await asyncio.start_server(handle_echo, host, port)
    
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        host = con.HOST
        port = con.PORT
    else:
        host = sys.argv[2]
        port = int(sys.argv[3])
        
    asyncio.run(main(host, port))
