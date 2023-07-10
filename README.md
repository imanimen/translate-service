# Installation 
    git clone https://github.com/imanimen/translate-service.git
    cd translate-service
    pip install -r requirements.txt
# Run
    python app.py
# Endpoint
    http://127.0.0.1/translate
# Method 
    POST
# Payload
    {
        "text": "your-sample-text",
        "source": "en",
        "target": "fa"
    }
# Documentation
    http://127.0.0.1/docs

# Notes
    - Install Python 3 or higher
    - Keep in mind that this service need to make requests to google so it needs intenet
    - Feel free to submit merge request 
    - Enjoy
