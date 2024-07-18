import functools

from flask  import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from safe_source.db  import get_db

bp  = Blueprint('contact',__name__,url_prefix='/contact')


@bp.route('/contact',methods=('GET','POST'))
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

    if error is None:
        try:
            db.execute(
            'INSERT INTO contact_info ( Name,surname, Email,cell_no,subject,message) VALUES(?,?,?,?,?,?)',
            (name,surname,email,cell_no,subject, message )
            )
        except db.IntegrityError:
           error = f"{email} has already been used."
    flash(error)
  return render_template('contact.html')
