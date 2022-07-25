from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)

def queryContact(string):
    # Look the string on database and return all the contacts that match.
    return Contact.query.filter(Contact.terr.like("%" + string + "%") |  Contact.reg.like("%" + string + "%") | Contact.pdvnum.like("%" + string + "%") | Contact.pdvname.like("%" + string + "%") | Contact.manager.like("%" + string + "%") | Contact.leader.like("%" + string + "%")).all()

@contacts.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        data = request.get_json()
        formString = data.get('formid')
        formString = str(formString)
        contacts = queryContact(formString)
        contact_list = []
        for contact in contacts:
            contact_list.append(contact.terr)
            contact_list.append(contact.reg)
            contact_list.append(contact.pdvnum)
            contact_list.append(contact.pdvname)
            contact_list.append(contact.manager)
            contact_list.append(contact.managerPhone)
            contact_list.append(contact.leader)
            contact_list.append(contact.leaderPhone)

        db.session.commit()

        if contacts:
            # Transform array into a string.
            contact_list = str(contact_list)
            return contact_list
        else:
            return "404NOTFOUND"

@contacts.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@contacts.route('/1049490Redunica1234')
def admin():
    contacts = Contact.query.all()
    return render_template('admin.html', contacts=contacts)

@contacts.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # Receive data from form
        terr = request.form['terr']
        reg = request.form['reg']
        pdvnum = request.form['pdvnum']
        pdvname = request.form['pdvname']
        manager = request.form['manager']
        managerPhone = request.form['managerPhone']
        leader = request.form['leader']
        leaderPhone = request.form['leaderPhone']

        # Create a new contact object

        new_contact = Contact(terr, reg, pdvnum, pdvname, manager, managerPhone, leader, leaderPhone)

        # Save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))

@contacts.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    # get contact by id
    print(id)
    contact = Contact.query.get(id)

    if request.method == 'POST':
        contact.terr = request.form['terr']
        contact.reg = request.form['reg']
        contact.pdvnum = request.form['pdvnum']
        contact.pdvname = request.form['pdvname']
        contact.manager = request.form['manager']
        contact.managerPhone = request.form['managerPhone']
        contact.leader = request.form['leader']
        contact.leaderPhone = request.form['leaderPhone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)

@contacts.route('/delete/<id>', methods=['GET'])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))