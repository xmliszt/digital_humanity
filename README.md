# digital_humanity
Projects in digital humanity


# How to use
1. Open "Terminal" or "Command Prompt" in MacOS or Windows
2. Follow the instructions below to use different analysis tools

# Sentiment Analysis using Textblob
```bash
git clone https://github.com/xmliszt/digital_humanity
cd digital_humanity
pip install virtualenv
virtualenv venv
venv\Scripts\activate (WIN)  OR source bin/activate (MAC)
python sentiment_analysis_textblob.py {directory containing all your text files} {name of output file} {bulk size}
```

* bulk size: The number of sentences analysed in one bulk.

# Sentiment Analysis using VaderSentiment (Bulk mode)
```bash
git clone https://github.com/xmliszt/digital_humanity
cd digital_humanity
pip install virtualenv
virtualenv venv
venv\Scripts\activate (WIN)  OR source bin/activate (MAC)
python sentiment_analysis_vader_bulk.py {directory containing all your text files} {bulk size}
```

# Sentiment Analysis using VaderSentiment (Single mode)
```bash
git clone https://github.com/xmliszt/digital_humanity
cd digital_humanity
pip install virtualenv
virtualenv venv
venv\Scripts\activate (WIN)  OR source bin/activate (MAC)
python sentiment_analysis_vader_single.py {directory containing all your text files}
```