from app import create_app

app = create_app()

if __name__ == '__main__':
    app.config['DEBUG'] = True  # Set DEBUG mode before running the app
    app.run()
