from app import db
from models import AdoptPet

db.drop_all()
db.create_all()

ap = AdoptPet(name="Blue", species="cat", available=True)
db.session.add(ap)
db.session.commit()
