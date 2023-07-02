# Installation 
    git clone git@github.com:imanimen/free-translate-service.git
    cd translate
    pip install fastapi pydantic deep_translator
    python app.py
# Run
python app.py

# Endpoint
server:port/translate

{
    "text": "your-sample-text",
    "source": "en",
    "target": "fa"
}
# Documenation
server:port/docs