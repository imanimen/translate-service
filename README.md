# Installation 
    git clone git@git.dyneemadev.com:micro-services/translate.git
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
server:port/docs# translate-api-free
