#!/usr/bin/env python3
"""
Business Email Writer - Using Groq API with R-T-C-C-O Framework
We Can Academy AI Course - Group Project
"""

import os
import json
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def generate_email():
    """R-T-C-C-O version with JSON output"""
    
    # Check API key exists
    if not API_KEY or API_KEY == "your_actual_api_key_here":
        print("❌ ERROR: Please add your GROQ_API_KEY to the .env file!")
        print("Get free key from: https://console.groq.com")
        return
    
    # Get user input
    print("=" * 50)
    print("BUSINESS EMAIL WRITER")
    print("=" * 50)
    
    purpose = input("\nWhat is this email about? > ")
    recipient = input("Who is it for? > ")
    tone = input("Tone (formal/professional/friendly)? > ")
    
    # R-T-C-C-O Prompt Design
    prompt = f"""Role: You are an expert business communication specialist with 15 years of experience writing professional emails for corporate executives in Kenya and East Africa.

Task: Write a complete, polished professional email that achieves the stated purpose effectively.

Context:
        - Sender Name: Jackton Miruka Mboya
        - Email Purpose: {purpose}
        - Recipient: {recipient}
        - Tone: {tone}
        - Region: Kenyan business context (professional, culturally appropriate)

Constraints:
- Keep the email concise (150-250 words)
- Use professional business English
- Include appropriate greeting and closing
- Avoid jargon unless necessary
- Ensure culturally appropriate tone for East African business environment
- Structure: Subject line, greeting, 2-3 paragraph body, professional closing

Output: Return ONLY a JSON object with this exact structure (no markdown, no explanation):
{{"subject": "Compelling subject line", "greeting": "Professional greeting", "body": "Main email content with proper paragraphs", "closing": "Professional sign-off", "signature": "[Your Name]"}}"""
    
    print("\n🤖 Generating email...")
    
    # Groq API
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 800,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        # Parse API response
        result = response.json()
        ai_response = result["choices"][0]["message"]["content"]
        
        # Clean up and parse JSON from AI response
        cleaned = ai_response.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
        
        email_data = json.loads(cleaned)
        
        # Display formatted email
        print("\n" + "=" * 60)
        print("✉️  GENERATED PROFESSIONAL EMAIL")
        print("=" * 60)
        print(f"\n📌 SUBJECT: {email_data['subject']}")
        print(f"\n{email_data['greeting']}")
        print(f"\n{email_data['body']}")
        print(f"\n{email_data['closing']}")
        print(f"{email_data['signature']}")
        print("=" * 60)
        
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    generate_email()