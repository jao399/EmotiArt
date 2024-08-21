import logging
import os
from flask import Blueprint, render_template, redirect, request, url_for, session, flash, jsonify, current_app as app
from werkzeug.utils import secure_filename
from passlib.hash import sha256_crypt
from app import db
from app.models import User, Artwork, Comment
from app.forms import RegistrationForm, LoginForm, CommentForm, ArtworkForm
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/show_artwork/<int:artwork_id>', methods=['GET', 'POST'])
def show_artwork(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    form = CommentForm()
    if form.validate_on_submit() and 'logged_in' in session:
        user = User.query.filter_by(username=session['username']).first()
        new_comment = Comment(
            content=form.content.data,
            artwork_id=artwork_id,
            user_id=user.id
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.show_artwork', artwork_id=artwork_id))
    comments = Comment.query.filter_by(artwork_id=artwork_id).all()
    return render_template('show_artwork.html', artwork=artwork, comments=comments, form=form)


@main.route('/add_comment/<int:artwork_id>', methods=['POST'])
def add_comment(artwork_id):
    form = CommentForm()
    if form.validate_on_submit() and 'logged_in' in session:
        new_comment = Comment(
            content=form.content.data,
            artwork_id=artwork_id,
            user_id=User.query.filter_by(
                username=session['username']).first().id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash('Your comment has been posted.', 'success')
        return redirect(url_for('main.show_artwork', artwork_id=artwork_id))
    flash('Failed to post comment. Please check your input.', 'error')
    return redirect(url_for('main.show_artwork', artwork_id=artwork_id))


@main.route('/edit_artwork/<int:artwork_id>', methods=['GET', 'POST'])
def edit_artwork(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    form = ArtworkForm(obj=artwork)
    if form.validate_on_submit():
        artwork.title = form.title.data
        artwork.description = form.description.data
        if form.file.data:
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
            artwork.filename = filename
        db.session.commit()
        flash('Artwork updated successfully!', 'success')
        return redirect(url_for('main.show_artwork', artwork_id=artwork_id))
    return render_template('edit_artwork.html', form=form, artwork=artwork)


@main.route('/delete_artwork/<int:artwork_id>', methods=['POST'])
def delete_artwork(artwork_id):
    if 'logged_in' not in session:
        return redirect(url_for('main.login'))
    artwork = Artwork.query.filter_by(id=artwork_id).first_or_404()
    if artwork.creator.username != session['username']:
        return "Unauthorized access.", 403
    db.session.delete(artwork)
    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], artwork.filename))
    except Exception as e:
        print(f"Error deleting file: {e}")
    db.session.commit()
    return redirect(url_for('main.profile'))


@main.route('/profile')
def profile():
    if 'logged_in' not in session:
        return redirect(url_for('main.login'))
    username = session['username']
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('User not found.', 'error')
        return redirect(url_for('main.login'))
    artworks = Artwork.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', user=user, artworks=artworks)


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'logged_in' not in session:
        return redirect(url_for('main.login'))
    form = ArtworkForm()
    error_message = None
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        logging.debug(f"Attempting to save file at path: {file_path}")
        try:
            file.save(file_path)
            logging.info("File saved successfully.")
        except Exception as e:
            logging.error(f"Error saving file: {e}")
            error_message = "Could not save the file due to an error."
        if not error_message:
            new_artwork = Artwork(
                title=form.title.data,
                description=form.description.data,
                filename=filename,
                user_id=User.query.filter_by(
                    username=session['username']).first().id
            )
            db.session.add(new_artwork)
            db.session.commit()
            return redirect(url_for('main.profile'))
    return render_template('upload.html', form=form, error=error_message)


@main.route('/gallery')
def gallery():
    all_artworks = Artwork.query.all()
    return render_template('gallery.html', artworks=all_artworks)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    error_message = None
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)).first()
        if existing_user:
            error_message = "Username or Email already exists. Please choose another."
        else:
            hashed_password = sha256_crypt.hash(form.password.data)
            new_user = User(username=username, email=email,
                            hashed_password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.login'))
    return render_template('register.html', form=form, error=error_message)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error_message = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and sha256_crypt.verify(password, user.hashed_password):
            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user.id
            return redirect(url_for('main.profile'))
        else:
            error_message = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error_message)


@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    return render_template('index.html')
