# Installation 
    git clone git@github.com:imanimen/free-translate-service.git
    cd free-translate-service
    pip install fastapi pydantic deep_translator
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
# Documenation
    http://127.0.0.1/docs