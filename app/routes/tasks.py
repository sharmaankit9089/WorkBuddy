from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add', methods=["POST"])
def add_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='Pending', user_id=user_id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')
    
    return redirect(url_for('tasks.view_tasks'))



@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
def toggle_status(task_id):
    user_id = session.get('user_id')
    task = Task.query.get(task_id)
    if task and user_id and task.user_id == user_id:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))



@tasks_bp.route('/delete/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    user_id = session.get('user_id')
    task = Task.query.get(task_id)
    if task and user_id and task.user_id == user_id:
        db.session.delete(task)
        db.session.commit()
        flash('Task cleared!','info')
    return redirect(url_for('tasks.view_tasks'))



@tasks_bp.route('/clear', methods=["POST"])
def clear_tasks():
    user_id = session.get('user_id')
    if user_id:
        Task.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        flash('All your tasks cleared!','info')
    return redirect(url_for('tasks.view_tasks'))
