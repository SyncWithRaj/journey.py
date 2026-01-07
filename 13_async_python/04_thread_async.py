import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_event_loop()  # get_event_loop ka kaam LLM se puch lena ye basically threads ko async jesa banata hai
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")  #run_in_executor let asyncio run a sync function but in another thread
        print(result)

asyncio.run(main())