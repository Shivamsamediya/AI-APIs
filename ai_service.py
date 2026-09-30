import os
from google import genai
from dotenv import load_dotenv

# .env file se environment variables ko load karte hain
# Isse hum secure tareeqe se API key use kar sakte hain bina code mein hardcode kiye
load_dotenv()

# .env file se API key nikal rahe hain
API_KEY = os.getenv("GEMINI_API_KEY")

# Agar API key nahi mili toh hum ek error batayenge taaki user ko pata chal jaye
if not API_KEY:
    raise ValueError("GEMINI_API_KEY .env file mein nahi mili. Kripya .env file banayein aur usme apni API key dalein.")

# Gemini client ko initialize karte hain, yeh hamari API key use karega
# Yeh latest google-genai SDK ka naya syntax hai
client = genai.Client(api_key=API_KEY)

def get_gemini_response(user_message: str) -> str:
    """
    Yeh function user ka message leta hai, Gemini API ko bhejta hai,
    aur phir AI ka response wapis karta hai.
    """
    try:
        # Client ke through model se content generate karwate hain
        # 'gemini-2.5-flash' ek fast aur efficient model hai text generation ke liye
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message
        )
        
        # API ke response se text nikal kar wapis (return) karte hain
        return response.text
    except Exception as e:
        # Agar koi error aata hai (jaise internet issue ya galat key), toh usko properly handle karte hain
        return f"Error aaya: {str(e)}"
