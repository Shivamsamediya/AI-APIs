# Beginner-Friendly Gemini AI Chat API 🚀

Welcome! Yeh project aapka pehla AI API backend project hai, jo **Python**, **FastAPI** aur **Gemini AI** se bana hai. Is project ka goal simple aur clean code likhna hai jisse koi bhi beginner asaani se samajh sake.

---

## 📂 Project Structure

```text
AI-APIs/
│
├── main.py              # Application ka starting point (FastAPI server yahan chalta hai)
├── ai_service.py        # Gemini API se baat karne ka logic yahan likha hai
├── schemas.py           # Data ka format define karta hai (Request & Response ka structure)
├── requirements.txt     # Wo saare packages jo is project ko chalne ke liye chahiye
├── .env.example         # Sample environment file, isme hum apn API key ko secure rakhte hain
└── Gemini_API_Postman_Collection.json # Postman me direct import karne ke liye endpoints file
```

---

## 📄 Har File Kya Karti Hai?

1. **`main.py`**: Yeh hamari dukaan (API server) ka front desk hai. Jab bhi koi request aati hai (jaise browser se ya Postman se), yeh usko receive karta hai.
2. **`ai_service.py`**: Yeh piche baitha hua expert (Gemini AI client) hai. `main.py` isko user ka message deta hai, aur yeh Google ke servers (Gemini) se response lakar deta hai.
3. **`schemas.py`**: Yeh ek rule-book hai jo batati hai ki user kis format mein data bhejega (e.g., `{"message": "hi"}`) aur hum kis format mein data wapis bhejenge (e.g., `{"reply": "hello"}`).
4. **`requirements.txt`**: Yeh ek shopping list hai jisme likha hai ki hume kaunse Python tools (libraries) install karne hain (jaise fastapi, google-genai, uvicorn aadi).
5. **`.env` (aap banayenge)**: Yeh ek tijori (safe) hai. Isme aap apna secret password (API Key) chupakar rakhte hain taaki wo code ke sath mix na ho aur secure rahe.

---

## ⚙️ Virtual Environment (venv) Kya Hai Aur Kyu Zaroori Hai?

Jab hum Python projects banate hain, toh hum alag-alag libraries (jaise fastapi, uvicorn) install karte hain. Agar hum sabkuch seedhe apne computer mein globally install kar denge, toh alag-alag projects ke library versions aapas mein takra sakte hain (conflict). 

**Virtual Environment (venv)** ek alag, isolated box banata hai sirf is project ke liye. Is project ki saari libraries is box (venv) ke andar hi rahengi aur aapke computer ki doosri files ya projects ko disturb nahi karengi.

---

## 🚀 Setup Kaise Karein (Step-by-Step)

### Step 1: Virtual Environment (venv) Banayein aur Activate Karein
Terminal/Command Prompt kholein aur project folder ke andar jayein, fir yeh commands chalayein:

**Windows ke liye:**
```bash
# 1. venv banayein ("venv" folder ka naam hai)
python -m venv venv

# 2. venv activate karein
venv\Scripts\activate
```
*(Activation ke baad aapko terminal mein `(venv)` likha hua dikhega. Iska matlab ab aap us box ke andar hain!)*

---

### Step 2: Dependencies Install Karein
Ab humari `requirements.txt` wali shopping list se saare tools us venv box me install karenge:
```bash
pip install -r requirements.txt
```

---

### Step 3: `.env` File Banayein aur API Key Dalein
1. Apne project folder mein ek nayi file banayein jiska naam sirf `.env` ho (naamo ke aage ya piche kuch nahi hona chahiye).
2. Google AI Studio se apni Gemini API key nikal kar `.env` mein aise likhein:
```env
GEMINI_API_KEY=tumhari_api_key_yaha_daalo
```
*(Aap `.env.example` file ko copy karke rename karke bhi usme key daal sakte hain.)*

---

### Step 4: Project (FastAPI Server) Chalayein
Ab hum apna server start karenge uvicorn library use karke:
```bash
uvicorn main:app --reload
```
*`--reload` ka matlab hai ki jaise hi aap code me kuch edit karke save karenge, server apne aap refresh ho jayega.*

---

## 🔁 API Flow: Request FastAPI Se Gemini Tak Kaise Jaati Hai?

1. **User (Postman/Frontend):** Postman se `/api/chat` par ek JSON request (`{"message": "Hello"}`) bhejta hai.
2. **FastAPI (`main.py`):** User ki request aati hai aur hamara `chat_with_ai` endpoint (function) chalta hai. FastAPI automatically check karta hai ki data format `schemas.py` ke hisab se sahi hai ya nahi.
3. **AI Service (`ai_service.py`):** `main.py` us message ko `get_gemini_response` function ko paas karta hai.
4. **Gemini SDK (`google-genai`):** Yeh function Gemini API key use karke Google ke remote servers par wo message bhejta hai.
5. **Google Servers (Gemini AI):** AI model message ko process karta hai aur ek reply (text) generate karta hai.
6. **Return Journey:** Reply wapas `ai_service.py` -> `main.py` mein aata hai aur aakhir me Postman mein JSON format (`{"reply": "Hi there!"}`) banke user ko dikh jata hai.

---

## 🧪 APIs Test Kaise Karein?

Aap API ko test karne ke 2 aasan tareeqe use kar sakte hain:

### Tareeqa 1: Swagger UI (Built-in)
FastAPI ka ek bohot bada fayda ye hai ki wo testing ke liye ek page apne aap banata hai. Server chalu karne ke baad browser me jaiye:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
1. `POST /api/chat` par click karein.
2. **"Try it out"** button dabayein.
3. `"message"` ke aage apna sawaal likhein.
4. **"Execute"** par click karein aur niche server ka response dekhein!

### Tareeqa 2: Postman Collection
Humne pehle se ek **Postman Collection JSON** file (`Gemini_API_Postman_Collection.json`) de di hai jisse aapka kaam asan ho jaye.
1. Postman application kholein.
2. **Import** button par click karein aur is folder se `.json` file ko select karein.
3. "Gemini AI Beginner API" naam ka collection add ho jayega.
4. **"2. Chat with Gemini AI"** request kholiye aur **"Send"** click karein. Aapko AI ka jawab body me dikh jayega!
