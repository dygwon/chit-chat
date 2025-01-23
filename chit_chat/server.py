import sys
import random
import asyncio
import chit_chat.constants as con


async def handle_echo(reader, writer):
    
    
    while True:
        data = await reader.read(100)
        message = data.decode()
        if message == con.EXIT:
            break
        
        addr = writer.get_extra_info('peername')
        print(f'Received {message!r} from {addr!r}')
        
        response = random.choice([
            "Thanks for the response!",
            "Got it!",
            "What else can I help you with?",
            "Howdy, partner."])
        print(f'Send: {response!r}')
        writer.write(response)
        await writer.drain()
    
    print('Closing the connection.')
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
        host = sys.argv[1]
        port = int(sys.argv[2])
        
    asyncio.run(main(host, port))
