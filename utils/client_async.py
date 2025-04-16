import asyncio
import httpx, time

start = time.time()
async def req(client):
    res = await client.get("http://127.0.0.1:8000/polls/async/test/")
    # res = await client.get("http://127.0.0.1:8000/polls/async/new_question/")
    print('res = ', res)

async def gather_tasks():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
                    req(client),
                    req(client),
                    req(client),
                    req(client),
                    req(client),
                )

asyncio.run(gather_tasks())
print(f'time = {time.time() - start}')




