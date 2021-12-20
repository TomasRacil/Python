from neomodel import StructuredNode, StringProperty, RelationshipTo, config


config.DATABASE_URL = 'bolt://neo4j:heslo123@localhost:7687'


class WebPage(StructuredNode):
    url= StringProperty(unique_index=True)
    connected_webpages= RelationshipTo('WebPage','WEBPAGE')

# url="https://www.google.com"
# ur="https://www.maps.google.com"
# try:
#     root=WebPage.nodes.get(url=url)
# except:
#     root=WebPage(url=url).save()
# try:
#     to=WebPage.nodes.get(url=ur)
#     root.connected_webpages.connect(to)
# except:
#     to=WebPage(url=ur).save()
#     root.connected_webpages.connect(to)
# google=WebPage(url="https://www.google.com").save()
# googleMaps=WebPage(url="https://www.maps.google.com").save()
# google.connected_webpages.connect(googleMaps)

# class Book(StructuredNode):
#     title = StringProperty(unique_index=True)
#     author = RelationshipTo('Author', 'AUTHOR')

# class Author(StructuredNode):
#     name = StringProperty(unique_index=True)
#     books = RelationshipFrom('Book', 'AUTHOR')


# harry_potter = Book(title='Harry potter and the..').save()
# rowling =  Author(name='J. K. Rowling').save()
# harry_potter.author.connect(rowling)
#rowling.books.connect(harry_potter)

# all_books = Book.nodes.all()
# all_autors = Author.nodes.all()
# for autor in all_autors:
#     autor.delete()
# for book in all_books:
#     book.delete()