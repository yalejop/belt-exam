from flask import render_template, redirect, session, request, flash

from flask_app import app

from flask_app.models.users import User
from flask_app.models.appointments import Appointment

@app.route('/appointments/add')
def new_appointment():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario)
    
    return render_template('new_appointment.html', user=user)

@app.route('/create/appointment', methods=['POST'])
def create_appointment():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Appointment.validate_appointment(request.form): 
        return redirect('/appointments/add')

    Appointment.save(request.form)
    return redirect('/appointments')

@app.route('/appointments/<int:id>') 
def edit_recipe(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_appointment = { "id": id }
    
    appointment = Appointment.get_by_id(formulario_appointment)

    return render_template('edit_appointment.html', user=user, appointment=appointment)

@app.route('/update/appointments', methods=['POST'])
def update_appointment():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Appointment.validate_appointment(request.form):
        return redirect('/appointments/'+ request.form['id']) 

    Appointment.update(request.form)

    return redirect('/appointments')

@app.route('/delete/appointments/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Appointment.delete(formulario)

    return redirect('/appointments')

