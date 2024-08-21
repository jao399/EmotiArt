# EmotiArt Project

## Overview

EmotiArt is a web-based application that allows users to create, share, and interact with digital artworks. The platform provides features like user registration, artwork upload, gallery viewing, and interaction through likes and dislikes. The project is built using Python, Flask, and SQLite, with a modular structure that ensures scalability and maintainability.

## Features

- **User Authentication**: Register, login, and manage profiles.
- **Artwork Upload**: Upload digital artworks and display them in the gallery.
- **Gallery**: View all uploaded artworks in a structured gallery format.
- **Interaction**: Users can like or dislike artworks, with restrictions ensuring each user can only interact once per artwork.
- **Responsive Design**: The application is designed to be accessible on various devices.

## Project Structure

```plaintext
your_project/
├── app/
│   ├── __init__.py           # Initialize the Flask app
│   ├── models.py             # Database models
│   ├── routes.py             # Application routes
│   ├── forms.py              # Web forms for user input
│   ├── templates/            # HTML templates
│   │   ├── base.html         # Base template
│   │   ├── index.html        # Homepage template
│   │   ├── profile.html      # User profile template
│   │   ├── register.html     # Registration page
│   │   ├── login.html        # Login page
│   │   ├── upload.html       # Artwork upload page
│   │   ├── gallery.html      # Artwork gallery page
│   │   ├── show_artwork.html # Individual artwork display page
│   │   └── edit_artwork.html # Artwork editing page
│   └── static/               # Static files (CSS, images, uploads)
│       ├── uploads/          # Uploaded artwork files
│       ├── css/              # Stylesheets
│       └── images/           # Static images
├── config.py                 # Application configuration settings
├── run.py                    # Entry point for the application
├── requirements.txt          # Python dependencies
└── emotiart.db               # SQLite database file
```

## How to Run

clone the repository

```bash
git clone https://github.com/jao399/EmotiArt
```

Navigate to the project directory

```bash
cd EmotiArt
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python run.py
```

Open a web browser and go to `http://

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Bootstrap](https://getbootstrap.com/)
- [Unsplash](https://unsplash.com/)
- [Font Awesome](https://fontawesome.com/)
- [Pexels](https://www.pexels.com/)
- [Pixabay](https://pixabay.com/)
- [Unsplash](https://unsplash.com/)
```
