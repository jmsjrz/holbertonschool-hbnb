from app import create_app

def run_app():
    """
    Runs the Flask app.

    This function creates an instance of the Flask app using the create_app() function from the app module.
    It then runs the app on the specified host and port.

    Args:
        None

    Returns:
        None
    """
    app = create_app()

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
