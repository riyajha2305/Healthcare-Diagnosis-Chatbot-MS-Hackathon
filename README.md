# Healthcare Chatbot

![Main Window](images/main_window.png)

## Project Overview

The Healthcare Chatbot is a Python-based desktop application designed to predict potential diseases based on user-entered symptoms. It leverages natural language processing (NLP) techniques and a pretrained Named Entity Recognition (NER) model from Huggingface to extract disease names from user input.

## Project Goals

The primary goal of this project is to provide users with accurate disease predictions based on their symptoms. By utilizing advanced NLP and machine learning models, the chatbot aims to assist users in understanding potential health issues they may be experiencing.

## Technologies Used

- **Python**: Core programming language used for the application.
- **TKinter**: Python's standard GUI (Graphical User Interface) toolkit used for creating the desktop-based application.
- **Spacy**: Open-source library for NLP tasks such as tokenization and lemmatization.
- **Huggingface Transformers**: Utilized for accessing a pretrained model (`raynardj/ner-disease-ncbi-bionlp-bc5cdr-pubmed`) to extract disease names from user input.
- **pip**: Python's package installer used for managing dependencies.

## Installation

To run the Healthcare Chatbot locally, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/riyajha2305/Healthcare-Diagnosis-Chatbot.git
   cd Healthcare-Diagnosis-Chatbot
   ```
2. **Install dependencies**:
  ```
  pip install -r requirements.txt
   ```
3. **Download Spacy**:
   ```
    pip install -U pip setuptools wheel
    pip install -U spacy
    python -m spacy download en_core_web_sm
   ```
4. **Download and save pre-trained model from Huggingface as newsave_model**
   ```
    from transformers import pipeline
    PRETRAINED = "raynardj/ner-disease-ncbi-bionlp-bc5cdr-pubmed"
    ners = pipeline(task="ner",model=PRETRAINED, tokenizer=PRETRAINED)
    
    import pickle as pk
    with open('newsave_model', 'wb') as f:
        pk.dump(ners, f)
   ```
## Usage

1. **Run the Application**
```
python3 ./HealthCare_App.py
```

2. **Enter Symptoms**
Use the GUI interface to enter symptoms. The chatbot will predict potential diseases based on the symptoms provided.
Output Image

3. **View results**
The chatbot will display the predicted diseases or health conditions corresponding to the symptoms entered.

## Application Overview
