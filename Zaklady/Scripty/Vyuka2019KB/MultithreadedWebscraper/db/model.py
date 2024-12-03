"""Modell for webpages in neo4j"""

from neomodel import StructuredNode, StringProperty, BooleanProperty, RelationshipTo

class WebPage(StructuredNode):
    name = StringProperty(unique_index=True, required=True)  # primary key
    url = StringProperty(required=True)
    ssl = BooleanProperty(default=False) 
    connected_webpages = RelationshipTo('WebPage', 'WEBPAGE')

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