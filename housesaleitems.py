from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog_database_setup import Category, Base, HouseItem, User

engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user

User1 = User(name="Rafaela Cavalcante", email="rafa.pgcavalcante@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/'
             '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for Kitchen
category1 = Category(user_id=1, name="Kitchen")

session.add(category1)
session.commit()


houseItem1 = HouseItem(user_id=1, name="Freezer",
                       description=" Brastemp Freezer inverted position 2015.",
                       price="$2,500", status="for sale", category=category1)

session.add(houseItem1)
session.commit()

houseItem2 = HouseItem(user_id=1, name="Vacuum Cleaner",
                       description="Britania vacuum cleaner + 20 bags",
                       price="$130.50", status="for sale", category=category1)

session.add(houseItem2)
session.commit()

houseItem3 = HouseItem(user_id=1, name="Over",
                       description=("Brastemp cromed stainless "
                                    "oven with 6 entries"),
                       price="$790", status="sold", category=category1)

session.add(houseItem3)
session.commit()


houseItem4 = HouseItem(user_id=1, name="Le Cuisine set of Pan",
                       description=("La Cuisine 10 In Enameled Cast "
                                    "Iron set of 5 pan with "
                                    "Riveted Stainless Steel "
                                    "Handle, red"),
                       price="$199.99", status="for sale", category=category1)

session.add(houseItem4)
session.commit()

category2 = Category(user_id=1, name="Baby Stuff")

session.add(category2)
session.commit()

houseItem1 = HouseItem(user_id=1, name="Organic Rug",
                       description=("Lorena Canals Soft Machine Washable Kids "
                                    "Rug made with Natural Cotton"
                                    "and Non-Toxic Dyes"),
                       price="$210", status="for sale", category=category2)

session.add(houseItem1)
session.commit()

houseItem2 = HouseItem(user_id=1, name="Montessori Bed",
                       description=("Unique and natural hand made house bed "
                                    "with removable railing and corbels"),
                       price="$560.50", status="sold", category=category2)

session.add(houseItem2)
session.commit()

houseItem3 = HouseItem(user_id=1, name="Chicco Stroller",
                       description=("Chicco Bravo Quick-Folder Stroller "
                                    "with 3-in-1 versatility"),
                       price="$680", status="for sale", category=category2)

session.add(houseItem3)
session.commit()

print "added menu items!"
