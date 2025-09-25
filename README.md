# Simple Gemini AI Test Application

A basic Python application to test the Google Gemini AI API. This app demonstrates how to connect to the Gemini API, send prompts, and receive AI-generated responses.

## Features

- 🤖 Connect to Google Gemini AI API
- 💬 Send text prompts and receive responses
- ✅ Test with multiple prompts to verify API functionality
- 🛡️ Error handling and helpful error messages
- 🔧 Environment variable configuration for API key security

## Prerequisites

- Python 3.7 or higher
- A Google Gemini API key (get one from [Google AI Studio](https://aistudio.google.com/))

## Setup Instructions

### 1. Clone or Download

If you haven't already, make sure you have the application files in your workspace.

### 2. Install Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to the API section
4. Generate your API key

### 4. Set Environment Variable

Set your API key as an environment variable:

```bash
# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"

# Windows Command Prompt
set GEMINI_API_KEY=your_api_key_here

# Windows PowerShell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Alternative**: Create a `.env` file in the project directory:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the application:

```bash
python gemini_test.py
```

### Expected Output

The application will:
1. Initialize the Gemini AI client
2. Send a test prompt about artificial intelligence
3. Display the AI response
4. Send a second prompt about renewable energy
5. Display the second response
6. Confirm successful completion

Example output:
```
🚀 Initializing Gemini AI client...
💭 Sending prompt: 'Explain artificial intelligence in simple terms, in exactly 3 sentences.'
⏳ Waiting for response...

==================================================
🤖 Gemini AI Response:
==================================================
[AI-generated response will appear here]
==================================================

🔄 Testing with a second prompt...
💭 Second prompt: 'What are the main benefits of renewable energy? List 3 key points.'

==================================================
🤖 Second Response:
==================================================
[Second AI-generated response will appear here]
==================================================

✅ Gemini API test completed successfully!
```

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `GEMINI_API_KEY` environment variable is set correctly
2. **Network Issues**: Ensure you have a stable internet connection
3. **Package Installation**: Verify that `google-genai` is installed correctly

### Error Messages

- `GEMINI_API_KEY environment variable not found!`: Set your API key as described above
- Network-related errors: Check your internet connection
- Authentication errors: Verify your API key is valid and active

## Customization

You can modify the prompts in `gemini_test.py` to test different types of AI interactions:

```python
# Change these lines in the main() function
prompt = "Your custom prompt here"
second_prompt = "Another prompt to test"
```

## Files Structure

```
workspace/
├── gemini_test.py      # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## API Usage Notes

- This app uses the `gemini-2.0-flash-exp` model
- Rate limits may apply depending on your API plan
- Check the [Gemini API documentation](https://ai.google.dev/guide) for more advanced features

## License

This is a simple test application provided as-is for educational purposes.