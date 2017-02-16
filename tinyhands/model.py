from uuid import uuid4
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bug(Base):
	'''Represents one OSM bug'''
	__tablename__ = 'bugs'

	id = Column(String, primary_key=True)
	name = Column(String)
	lon = Column(Float)
	lat = Column(Float)
	status = Column(String)
	text = Column(Text)
	osmids = Column(Text)
	tag = Column(String)

	def __init__(self, **kwargs):
		'''Initialize bug with a UUID'''
		self.id = uuid4()

	def __repr__(self):
		return {'id': self.id}