#!/usr/bin/env python3
"""
Simple Gemini AI Question-Answering Web App

A Flask web application that provides a simple interface to ask questions
and get answers from Google's Gemini AI.
"""

import os
from flask import Flask, render_template, request, jsonify, flash
from google import genai

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production

def get_gemini_client():
    """Initialize and return Gemini client"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

@app.route('/')
def index():
    """Main page with question form"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle question submission and return Gemini's answer"""
    try:
        # Get the question from the form
        question = request.json.get('question', '').strip()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Please enter a question'
            })
        
        # Check if API key is available
        client = get_gemini_client()
        if not client:
            return jsonify({
                'success': False,
                'error': 'Gemini API key not configured. Please set GEMINI_API_KEY environment variable.'
            })
        
        # Get response from Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=f"Please answer this question clearly and helpfully: {question}",
        )
        
        return jsonify({
            'success': True,
            'question': question,
            'answer': response.text
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error getting response from Gemini: {str(e)}'
        })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    client = get_gemini_client()
    return jsonify({
        'status': 'healthy',
        'gemini_configured': client is not None
    })

if __name__ == '__main__':
    print("🚀 Starting Gemini AI Question-Answering Web App")
    print("📝 Access the app at: http://localhost:5000")
    
    # Check if API key is configured
    if not os.getenv("GEMINI_API_KEY"):
        print("⚠️  Warning: GEMINI_API_KEY environment variable not set")
        print("   The app will start but won't be able to answer questions")
        print("   Set your API key with: export GEMINI_API_KEY='your_key_here'")
    else:
        print("✅ Gemini API key is configured")
    
    app.run(debug=True, host='0.0.0.0', port=5000)