import functools

from flask import(
    Blueprint,flash,g,redirect, render_template
)
from safe_source.db import get_db

bp = Blueprint('auth',__name__,url_prefix='auth')

"""
@bp.route('/register',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error ='Username is required.'
        elif not password:
            error ='Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user(usename,password)" values(?,?)"
                    (username,...)
                )
                db.commit
            except db .IntergrityError:
                error = f"{user} is already reg"
            else:
            ....
        
"""
