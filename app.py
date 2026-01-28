from flask import Flask, request, Response
import math

app = Flask(__name__)

@app.route('/app/nasratj355_gmail_com')
def calculate_lcm():
    """
    Calculate LCM of two natural numbers.
    Returns plain text: digits for valid inputs, 'NaN' for invalid.
    """
    try:
        # Get query parameters
        x_str = request.args.get('x', '')
        y_str = request.args.get('y', '')
        
        # Check if parameters exist
        if x_str == '' or y_str == '':
            return Response('NaN', mimetype='text/plain')
        
        # Convert to integers
        x = int(x_str)
        y = int(y_str)
        
        # Check if natural numbers (positive integers)
        if x <= 0 or y <= 0:
            return Response('NaN', mimetype='text/plain')
        
        # Calculate LCM using math.gcd (built-in, efficient)
        lcm = abs(x * y) // math.gcd(x, y)
        
        # Return as plain text string
        return Response(str(lcm), mimetype='text/plain')
        
    except (ValueError, TypeError):
        # Handle non-integer inputs (abc, 5.5, etc.)
        return Response('NaN', mimetype='text/plain')

@app.route('/health')
def health_check():
    """Simple health check endpoint to wake up server"""
    return Response('OK', mimetype='text/plain')

@app.route('/')
def home():
    """Root endpoint - simple message"""
    return '''
    <h1>LCM Calculator (Python)</h1>
    <p>Use: /app/nasratj355_gmail_com?x=number&y=number</p>
    <p>Test:</p>
    <ul>
        <li><a href="/app/nasratj355_gmail_com?x=12&y=18">Valid: 12, 18 → 36</a></li>
        <li><a href="/app/nasratj355_gmail_com?x=-5&y=10">Invalid: -5, 10 → NaN</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
