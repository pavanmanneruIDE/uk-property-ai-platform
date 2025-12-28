from pydantic import BaseModel
from datetime import date

class PropertyTransaction(BaseModel):
    price: int
    date_of_transfer: date
    postcode: str
    property_type: str
    town_city: str
    district: str
    county: str
