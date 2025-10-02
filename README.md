# Flask Error Handling Demo

A comprehensive Flask application demonstrating proper error handling with custom, attractive error pages for common HTTP errors (404 and 500).

## Features

- **Custom 404 Page**: Beautiful "Page Not Found" error page with helpful navigation
- **Custom 500 Page**: Professional "Internal Server Error" page with technical details
- **Error Logging**: Automatic logging of errors to file with rotation
- **Test Routes**: Intentional error triggers for demonstration purposes
- **Responsive Design**: Mobile-friendly error pages with modern styling
- **Professional UI**: Clean, modern interface using Inter font and CSS Grid

## Project Structure

```
flask-error-handling/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # This file
├── templates/
│   ├── base.html                  # Base template with navigation
│   ├── index.html                 # Home page
│   ├── test.html                  # Test page (working example)
│   └── errors/
│       ├── 404.html               # Custom 404 error page
│       └── 500.html               # Custom 500 error page
└── static/
    └── css/
        └── style.css              # CSS styles for all pages
```

## Installation and Setup

1. **Clone or download** this project to your local machine

2. **Create a virtual environment** (recommended):
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```cmd
   python app.py
   ```

5. **Open your browser** and navigate to: `http://localhost:5000`

## Testing Error Pages

### 404 Error (Page Not Found)
- Click "Trigger 404 Error" on the home page
- Or visit any non-existent URL like: `http://localhost:5000/nonexistent-page`

### 500 Error (Internal Server Error)
- Click "Trigger 500 Error" on the home page
- Or visit: `http://localhost:5000/trigger-500`
- This route intentionally performs division by zero to trigger a server error

## Application Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with demo options |
| `/test-page` | Working page example |
| `/trigger-500` | Intentionally triggers 500 error |
| Any invalid route | Triggers 404 error |

## Error Handling Features

### Logging
- Errors are automatically logged to `logs/app.log`
- Log rotation keeps file sizes manageable
- Includes timestamps, error levels, and stack traces

### Error Pages
- **404 Error**: Friendly "page not found" with suggestions and navigation
- **500 Error**: Professional server error page with technical details
- Both pages include multiple navigation options
- Responsive design works on all screen sizes

### Error Handlers
- `@app.errorhandler(404)`: Handles page not found errors
- `@app.errorhandler(500)`: Handles internal server errors  
- `@app.errorhandler(Exception)`: Catches any unhandled exceptions

## Customization

### Styling
The CSS in `static/css/style.css` uses CSS custom properties (variables) for easy theming:
- `--primary-color`: Main brand color
- `--danger-color`: Error/warning color
- `--success-color`: Success message color

### Error Messages
Edit the templates in `templates/errors/` to customize error messages and styling.

### Logging
Modify the logging configuration in `app.py` to change:
- Log file location
- Log levels
- Log rotation settings

## Development

### Adding New Error Handlers
```python
@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403
```

### Testing Error Scenarios
Add more test routes that simulate different error conditions:
```python
@app.route('/trigger-database-error')
def trigger_db_error():
    # Simulate database connection error
    raise Exception("Database connection failed")
```

## Security Considerations

- Error pages don't expose sensitive information
- Stack traces are logged but not shown to users
- Debug mode should be disabled in production
- Error logging helps with monitoring and debugging

## Browser Compatibility

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for mobile devices
- Graceful degradation for older browsers

## License

This is a demonstration project for educational purposes.