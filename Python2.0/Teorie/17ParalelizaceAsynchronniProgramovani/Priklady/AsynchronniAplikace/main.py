import asyncio
import time

async def fetch_data(url):
  print(f"Začínám stahovat: {url}")
  await asyncio.sleep(2)  # Simulace síťového požadavku
  print(f"Dokončeno stahování: {url}")
  return f"Data z {url}"

async def main():
  start_time = time.time()

  # Vytvoření úloh pro stahování dat
  task1 = asyncio.create_task(fetch_data("url1"))
  task2 = asyncio.create_task(fetch_data("url2"))

  # Čekání na dokončení úloh
  data1 = await task1
  data2 = await task2

  end_time = time.time()
  print(f"Celkový čas: {end_time - start_time:.2f} sekund")
  print(f"Data 1: {data1}")
  print(f"Data 2: {data2}")

asyncio.run(main())