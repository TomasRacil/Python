import asyncio

async def my_coroutine():
  print("Korutina spuštěna")
  await asyncio.sleep(1)  # Simulace I/O operace, pozastaví se na 1 sekundu
  print("Korutina pokračuje")

async def main():
  task = asyncio.create_task(my_coroutine()) #vytvoří task
  await task #zavolá task

asyncio.run(main()) # spustí hlavní async funkci