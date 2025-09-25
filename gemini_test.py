#!/usr/bin/env python3
"""
Simple Gemini AI API Test Application

This is a basic application to test the Google Gemini API.
It demonstrates how to:
1. Connect to the Gemini API
2. Send a prompt
3. Receive and display the response
"""

import os
from google import genai


def main():
    """Main function to test Gemini API"""
    
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not found!")
        print("Please set your Gemini API key:")
        print("export GEMINI_API_KEY='your_api_key_here'")
        return
    
    try:
        # Initialize the Gemini client
        print("🚀 Initializing Gemini AI client...")
        client = genai.Client(api_key=api_key)
        
        # Test prompt
        prompt = "Explain artificial intelligence in simple terms, in exactly 3 sentences."
        
        print(f"💭 Sending prompt: '{prompt}'")
        print("⏳ Waiting for response...")
        
        # Generate content using Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
        )
        
        # Display the response
        print("\n" + "="*50)
        print("🤖 Gemini AI Response:")
        print("="*50)
        print(response.text)
        print("="*50)
        
        # Test a second prompt to verify API is working
        print("\n🔄 Testing with a second prompt...")
        
        second_prompt = "What are the main benefits of renewable energy? List 3 key points."
        response2 = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=second_prompt,
        )
        
        print(f"💭 Second prompt: '{second_prompt}'")
        print("\n" + "="*50)
        print("🤖 Second Response:")
        print("="*50)
        print(response2.text)
        print("="*50)
        
        print("\n✅ Gemini API test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Common issues:")
        print("- Check if your API key is valid")
        print("- Ensure you have internet connection")
        print("- Verify the google-genai package is installed")


if __name__ == "__main__":
    main()