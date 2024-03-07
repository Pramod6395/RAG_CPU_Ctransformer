# Streaming Project Knowledge Based Using TGI and Streamlit

## Overview

This project is a knowledge-based system using Streamlit and language models for providing information about PDF uploaded data related projects and case studies. The system is designed to answer user queries.


### Installation Process for Stremlite Application with TGI model consumation:

#### 1. Create a virtual environment named 'ron' with Python 3.11.5:

```bash
conda create -n chatbot python=3.11.5 -y
```

#### 2. Activate the virtual environment:
```bash
conda activate chatbot
```

#### 3. Install all necessary dependencies:
```bash
pip install -r requirements.txt
```


#### 4. Run the Streamlit script:
```bash
streamlit run main.py
```

#### 5. Access the UI:

[](http://localhost:8501/)
```bash
Visit http://localhost:8501/ in your web browser to access the user interface.
```


### Using Docker:
```bash
docker run -p 8501:8501 -v /path_to/RAG_TGI:/app/ streamlit
```


