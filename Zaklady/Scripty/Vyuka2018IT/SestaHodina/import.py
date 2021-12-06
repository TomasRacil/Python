from urllib.request import Request, urlopen

req = Request('https://adventofcode.com/2021/day/1/input')
req.add_header('Cookie', '_ga=GA1.2.443214356.1637780633; session=53616c7465645f5fb910de0005fe30e374969c1ca27153fa190127918a881901ac6f993835c77eb63ea94b3064f9d7ba; _gid=GA1.2.1380312066.1638268502')
url=urlopen(req)


coordinates=[int(line.strip()) for line in url]

print(coordinates)


