import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Load the sentiment model
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Model labels
labels = ["Negative", "Neutral", "Positive"]

def analyze(text):
    # Encode the text
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    
    # Get model outputs
    outputs = model(**inputs)
    
    # Apply softmax to get probabilities
    probs = torch.softmax(outputs.logits, dim=1)[0].detach().numpy()
    
    # Get top sentiment
    idx = int(np.argmax(probs))
    sentiment = labels[idx]
    confidence = probs[idx] * 100
    
    return f" This is a **{sentiment}** sentence.\n📊 Confidence: **{confidence:.2f}%**"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 3-Class Sentiment Analysis (Positive / Neutral / Negative)")
    text_in = gr.Textbox(label="Enter text", placeholder="Write something...")
    text_out = gr.Markdown()
    btn = gr.Button("Analyze")
    
    btn.click(analyze, inputs=text_in, outputs=text_out)

demo.launch()
