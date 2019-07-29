from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article():

	article_object = Knowledge(
        name=name,
        topic=topic,
        rating=rating)
	session.add(article_object)
	ession.commit()

def query_all_articles():
	Knowledge = session.query(
		Knowledge).all()
    return Knowledge
    print(query_all())

	

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
