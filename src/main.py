import os, json, requests
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Main Function
def generate_email():

# Get API Key
    key = os.getenv("GROQ_API_KEY")
    if not key:
        return print("❌ Set GROQ_API_KEY in .env")

# Get User Input
    p = input("Purpose: ")
    r = input("Recipient: ")
    t = input("Tone (Professional/Formal/Friendly): ")

#Generating Message
    print("\n🤖 Generating...")

    try:
# API Call
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{
                    "role": "user",
                    "content": f"Write a {t} email to {r} about {p}. Do NOT include any closing like 'Best regards' or a name. Return JSON with subject and body."
                }]
            }
        ).json()

# Process Respond
        msg = res["choices"][0]["message"]["content"]
        email = json.loads(msg.replace("```json","").replace("```",""),strict=False)

# Display Output
        print(f"\n📌 {email['subject']}\n\n{email['body']}")
        print("\nBest regards,\nJackton Mboya")

# Error Handling
    except Exception as e:
        print("❌ Error:", e)

# Run Program
if __name__ == "__main__":
    generate_email()