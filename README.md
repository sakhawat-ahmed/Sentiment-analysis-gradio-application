## Sentiment Analysis Gradio Application

This project is a 3-class sentiment analysis tool built using Hugging Face Transformers and Gradio.
It predicts one of the following:

Positive

Neutral

Negative

The app also displays the model’s confidence percentage for its prediction.

## Features

3-class sentiment detection

Clean Gradio web interface

Confidence score output

Runs on Windows / Ubuntu

Uses a pretrained, high-quality NLP model

## Project Structure
Sentiment-analysis-gradio-application/
│
├── myenv/                # Virtual environment
├── app.py                # Main application file
├── requirements.txt      # Dependencies
└── README.md             # Documentation

## 1. Create Project Folder
mkdir Sentiment-analysis-gradio-application
cd Sentiment-analysis-gradio-application

## 2. Create Virtual Environment

Below are commands for Ubuntu and Windows.

## For Ubuntu
Install venv (if missing)
sudo apt install python3.12-venv -y

Create virtual environment
python3 -m venv myenv

Activate environment
source myenv/bin/activate

## For Windows (CMD or PowerShell)
Create virtual environment
python -m venv myenv

Activate environment (CMD)
myenv\Scripts\activate

Activate environment (PowerShell)
myenv\Scripts\Activate.ps1

## 3. Install Dependencies

Ensure requirements.txt is inside your project folder.

Install all packages (Ubuntu or Windows)
pip install -r requirements.txt

## 4. Application File

Create a file named app.py and put your application's source logic inside it
(code not included here per your request).

## 5. Run the Application
Ubuntu:
source myenv/bin/activate
python app.py

Windows (CMD):
myenv\Scripts\activate
python app.py

Windows (PowerShell):
myenv\Scripts\Activate.ps1
python app.py