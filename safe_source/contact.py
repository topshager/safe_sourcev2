import functools

from flask  import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from safe_source.db  import get_db

bp  = Blueprint('contact',__name__,url_prefix='/contact')


@bp.route('/submit_contact_form',methods=('GET','POST'))
def contact_form():
  if request.method == 'POST':
    name= request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    cell_no = request.form['cell_no']
    subject = request.form['subject']
    message = request.form['message']
    db = get_db()
    error = None

    if not name or not email or not message:
       error = "Name,Email and message are required"

    if error is None:
        try:
            db.execute(
            'INSERT INTO contact_info ( Name,surname, Email,cell_no,subject,message) VALUES(?,?,?,?,?,?)',
            (name,surname,email,cell_no,subject, message )
            )
            db.commit()
            
            flash("Your messsage was sent successfully!")
            return render_template(url_for('contact.contact_form'))
        except db.IntegrityError:
           error = f"{email} has already been used."
    flash(error, 'danger')
    return render_template('contact.html',
                               name=name, surname=surname, email=email,
                               cell_no=cell_no, subject=subject, message=message)
  return render_template('contact.html')
