import asyncio
from datetime import datetime

async def backend_request(data):
    reader, writer = await asyncio.open_connection(
        'web', 80)
    writer.write(data)
    data = await reader.read(100)
    writer.close()
    return data

def print_event(event_type, payload):
    timestamp = datetime.now()
    print(f"timestamp:{timestamp},event_type:{event_type},{payload}")

async def handle_request(reader, writer):
    data = await reader.read(100)
    try:
        src_addr, src_port = writer.get_extra_info('peername')
    except:
        src_addr, src_port = 'unknown', 'unknown'
    event_type = 'new_connection'
    payload = f'src_addr:{src_addr!r},src_port:{src_port},payload:{data!r}'
    print_event(event_type, payload)
    response = await backend_request(data)
    writer.write(response)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_request, '0.0.0.0', 80)

    addr = server.sockets[0].getsockname()
    event_type = 'start_client'
    payload = ''
    print_event(event_type, payload)
    async with server:
        await server.serve_forever()

asyncio.run(main())


