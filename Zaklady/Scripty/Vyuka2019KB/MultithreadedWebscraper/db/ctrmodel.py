import re
from urllib.parse import urlparse
from neomodel import config
from .model import WebPage

# Connect to your Neo4j database
config.DATABASE_URL = "bolt://neo4j:Heslo123@neo4j:7687"

def expand_map(root_url, target_urls):
    parsed_root = urlparse(root_url)
    try:
        root = WebPage.nodes.get_or_none(name=parsed_root.netloc)  # Fetch existing or None
        if not root:
            root = WebPage(
                url=root_url, 
                ssl=parsed_root.scheme == "https", 
                name=parsed_root.netloc
            ).save()  # Create and save

        for url in target_urls:
            parsed_url = urlparse(url)
            to = WebPage.nodes.get_or_none(name=parsed_url.netloc)
            if not to:
                to = WebPage(
                    url=url, 
                    ssl=parsed_url.scheme == "https", 
                    name=parsed_url.netloc
                ).save()
            root.connected_webpages.connect(to)  # Use connect() in neomodel
        root.save()

    except Exception as e:
        print(f"Error expanding map: {e}")

# expandMap("https://www.google.com",["https://www.maps.google.com","https://www.play.google.com"])
