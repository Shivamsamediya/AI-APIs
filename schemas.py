from pydantic import BaseModel

# Yeh class user ki request ka data define karti hai (User kya message bhej raha hai)
class ChatRequest(BaseModel):
    message: str # User ka message yahan aayega, example: "Hi, how are you?"

# Yeh class hamari API ka response format define karti hai (AI kya reply dega)
class ChatResponse(BaseModel):
    reply: str # Gemini AI ka response yahan aayega
