import asyncio

async def my_coroutine():
  print("Korutina spuštěna")
  await asyncio.sleep(1)
  print("Korutina pokračuje")

async def main():
  # Vytvoření úlohy z korutiny
  task = asyncio.create_task(my_coroutine())

  print("Dělám něco jiného, zatímco úloha běží na pozadí...")

  # Čekání na dokončení úlohy
  await task

  print("Úloha dokončena")

asyncio.run(main())