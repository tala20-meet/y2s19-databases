from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,topic,rating):

	article_object = Knowledge(
        name=name,
        topic=topic,
        rating=rating)
	session.add(article_object)
	session.commit()

# add_article("Databases","CS",0)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
print(query_all_articles())

def query_article_by_topic(inputtopic):
	Knowledge=session.query(Knowledge).filter_by(topic=inputtopic).all()
	return Knowledge
	

def delete_article_by_topic():
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()


def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating():
	pass
