from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

def set_up_logging():
    """Set up logging for the application."""
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # Create a rotating file handler for logging, keeps the 10 most recent logs
    # removing the oldest when the log file exceeds 10KB
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    
    # sets up the log format (how the log messages will appear in the log file)
    file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    
    # Set the logging level to INFO
    file_handler.setLevel(logging.INFO)

    # Add the handler to the app logger
    app.logger.addHandler(file_handler)

    # Set the overall logging level for the app
    app.logger.setLevel(logging.INFO)

    # Log that the app has started
    app.logger.info('Flask Error Handling Demo startup')

# Main routes
@app.route('/')
def index():
    """Home page with links to demonstrate error handling"""
    return render_template('index.html')

@app.route('/trigger-500')
def trigger_500():
    """Route that intentionally triggers a 500 error by dividing by zero"""
    app.logger.warning('Someone accessed the /trigger-500 route')
    # This will cause a ZeroDivisionError and trigger our 500 error handler
    result = 1 / 0
    return f"This should never be reached: {result}"

@app.route('/test-page')
def test_page():
    """A working test page to show normal operation"""
    return render_template('test.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Custom 404 error handler"""
    app.logger.warning(f'404 error: {request.url}')
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error handler"""
    app.logger.error(f'Internal server error: {error}')
    return render_template('errors/500.html'), 500

@app.errorhandler(Exception)
def handle_exception(error):
    """Handle any unhandled exceptions"""
    app.logger.error(f'Unhandled exception: {error}', exc_info=True)
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    set_up_logging()
    app.run(debug=True, host='0.0.0.0', port=5000)