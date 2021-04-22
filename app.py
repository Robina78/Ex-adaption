from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, AdoptPet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool243243"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()





@app.route('/')
def list_page():
    pets = AdoptPet.query.all()  
  
    return render_template('list_pets.html', pets=pets)



@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        

        pet = AdoptPet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('list_page'))

    else:
        return render_template('add_pet_form.html', form=form)



@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = AdoptPet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():        
        pet.photo_url = form.photo_url.data        
        pet.notes = form.notes.data 
        pet.available = form.available.data       
        db.session.commit()
        flash(f"{pet.name} updated.",'success')
        return redirect(url_for('list_page'))

    else:
        return render_template('edit.html', form=form, pet=pet)

        



