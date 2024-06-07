import requests
import random
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Fetch data from REST Countries API
response = requests.get('https://restcountries.com/v3.1/all')
countries = response.json()

# Select 10 random countries
random_countries = random.sample(countries, 10)

# Extract required attributes
country_data = []
for country in random_countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0]
    flag = country.get('flags', {}).get('png', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 'N/A')
    country_data.append((name, capital, flag, subregion, population))

# Database setup
DATABASE_URL = "sqlite:///countries.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    capital = Column(String, nullable=False)
    flag = Column(String, nullable=False)
    subregion = Column(String, nullable=False)
    population = Column(Integer, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the table
for data in country_data:
    country = Country(name=data[0], capital=data[1], flag=data[2], subregion=data[3], population=data[4])
    session.add(country)

# Commit the transaction
session.commit()
session.close()