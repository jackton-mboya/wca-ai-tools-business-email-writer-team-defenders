import os
import json
from groq import Groq
from dotenv import load_dotenv

# 1. SETUP: Load API Key safely
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_business_email():
    print("\n--- TEAM DEFENDERS AI EMAIL WRITER ---")
    
    # 2. USER INPUT: Collecting details for personalization
    recipient = input("Who is this email for?: ")
    purpose = input("What is the purpose?: ")
    # SWAP: We now ask for Tone instead of Key Points
    tone = input("What is the desired tone? (e.g., Formal, Friendly, Urgent, Professional): ")

    # 3. R-T-C-C-O PROMPT: Using the required framework [cite: 15]
    prompt = f"""
    ROLE: Expert Business Communication Consultant.
    TASK: Write a professional email for a Kenyan business context.
    CONTEXT: Recipient: {recipient}, Purpose: {purpose}, Tone: {tone}.
    CONSTRAINTS: Keep it under 200 words. Sender is Jackton Mboya.
    OUTPUT: Return ONLY a JSON object with 'subject', 'body', and 'signature'.
    """

    # 4. API CALL: Sending request to Groq Cloud [cite: 15]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    # 5. JSON HANDLING: Parsing the response [cite: 15]
    email_data = json.loads(response.choices[0].message.content)

    print("\n" + "="*40)
    print(f"SUBJECT: {email_data['subject']}")
    print("-" * 40)
    print(email_data['body'])
    print(f"\nBest Regards,\nJackton Mboya") # Professional Signature
    print("="*40 + "\n")

if __name__ == "__main__":
    generate_business_email()