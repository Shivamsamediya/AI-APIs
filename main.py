from fastapi import FastAPI, HTTPException
from schemas import ChatRequest, ChatResponse
from ai_service import get_gemini_response

# FastAPI app ka instance banate hain, yeh hamari main application hai
app = FastAPI(
    title="Gemini AI Chat API",
    description="Yeh ek beginner-friendly FastAPI backend hai jo Gemini AI se connected hai.",
    version="1.0.0"
)

# Yeh ek simple root endpoint hai check karne ke liye ki server chal raha hai ya nahi
# Jab aap browser mein http://localhost:8000/ kholenge toh yeh function chalega
@app.get("/")
def read_root():
    # Response ek dictionary format mein jaata hai jo browser mein JSON banke dikhta hai
    return {"message": "Welcome to Gemini AI API backend! Server mast chal raha hai."}

# POST method ka use hota hai jab user se data lena hota hai
# Yeh hamara main chat endpoint hai: POST http://localhost:8000/api/chat
@app.post("/api/chat", response_model=ChatResponse)
def chat_with_ai(request: ChatRequest):
    """
    Yeh endpoint user ka message receive karta hai aur AI ka reply wapas deta hai.
    """
    # Check karte hain ki user ne khali message toh nahi bheja
    if not request.message.strip():
        # Agar message khali hai toh hum HTTP 400 (Bad Request) error throw karte hain
        raise HTTPException(status_code=400, detail="Message empty (khali) nahi ho sakta!")
    
    # AI service wale function ko call karte hain aur user ka message usme bhejte hain
    ai_reply = get_gemini_response(request.message)
    
    # Agar ai_service se error message aata hai, toh usko error response banakar bhejenge
    if ai_reply.startswith("Error aaya:"):
        # HTTP 500 ka matlab internal server error hota hai
        raise HTTPException(status_code=500, detail=ai_reply)
        
    # Sab sahi hone par hum Pydantic model (ChatResponse) mein reply wapas bhejte hain
    return ChatResponse(reply=ai_reply)
