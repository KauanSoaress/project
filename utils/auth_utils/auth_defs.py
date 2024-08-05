from flask import Flask, render_template, request, redirect, url_for

def register():
    username = request.form['username']
    password = request.form['password']

    db = current_app.config['MONGO_DB']
    users_collection = db['users']

    # Check if the username already exists
    if users_collection.find_one({'username': username}):
        flash('Username already exists. Choose a different one.', 'danger')
    else:
        users_collection.insert_one({'username': username, 'password': password})
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

def login():
    return None