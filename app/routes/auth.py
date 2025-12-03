from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not password or not confirm_password:
            flash('Please fill out all fields', 'warning')
            return redirect(url_for('auth.register'))

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('auth.register'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user'] = username
            session['user_id'] = user.id
            flash('Login Successful', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')



@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('user_id', None)
    flash('Logged out', 'info')
    return redirect(url_for('auth.login'))