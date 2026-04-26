import os, json, requests
from dotenv import load_dotenv

# LOAD ENV VARIABLES
load_dotenv()

# MAIN FUNCTION
def generate_email():

    # GET API KEY
    key = os.getenv("GROQ_API_KEY")
    if not key:
        return print("❌ Set GROQ_API_KEY in .env")

    # GET USER INPUT
    p = input("Purpose: ")
    r = input("Recipient: ")
    t = input("Tone (Professional/Formal/Friendly): ").lower()

    # BASIC SAFETY CHECK
    blocked = ["suicide", "kill myself", "self-harm", "goodbye note"]
    if any(word in p.lower() for word in blocked):
        print("❌ Sorry, this tool cannot generate that type of email.")
        return

    # GENERATING MESSAGE
    print("\n🤖 Generating...")

    try:
        # API CALL
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{
                    "role": "user",
                    "content": (
                        f"Write a {t} professional email to {r} about {p}. "
                        "Do NOT include any harmful or inappropriate content. "
                        "Do NOT include any closing like 'Best regards' or a name. "
                        "Return JSON with subject and body."
                    )
                }]
            }
        ).json()

        # PROCESS RESPONSE
        msg = res["choices"][0]["message"]["content"]
        email = json.loads(msg.replace("```json","").replace("```",""), strict=False)

        #DISPLAY OUTPUT
        print(f"\n📌 {email['subject']}\n\n{email['body']}")
        print("\nBest regards,\nJackton Mboya")

    # ERROR HANDLING
    except Exception as e:
        print("❌ Error:", e)

# RUN PROGRAM
if __name__ == "__main__":
    generate_email()