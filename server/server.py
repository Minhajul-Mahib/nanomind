"""
NanoMind Server v0.1.0
The only local AI that runs on 2GB RAM Android phones.
github.com/Minhajul-Mahib/nanomind | MIT License
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List
import uvicorn, time, json, os, platform

try:
    from llama_cpp import Llama
    LLAMA_OK = True
except ImportError:
    LLAMA_OK = False

try:
    import psutil
    def get_ram():
        m = psutil.virtual_memory()
        return round((m.total-m.available)/1024/1024), round(m.total/1024/1024)
except:
    def get_ram(): return 0, 0

MODEL_PATH = os.environ.get("NANOMIND_MODEL", "./models/model.gguf")
N_CTX      = int(os.environ.get("NANOMIND_CTX",     "1024"))
N_THREADS  = int(os.environ.get("NANOMIND_THREADS", "2"))
PORT       = int(os.environ.get("PORT",             "8080"))

app = FastAPI(title="NanoMind", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
llm = None

def load_model():
    global llm
    if not LLAMA_OK:
        print("Install: pip install llama-cpp-python"); return
    if not os.path.exists(MODEL_PATH):
        print(f"No model at {MODEL_PATH} — run: python scripts/download_model.py"); return
    print(f"Loading {MODEL_PATH}...")
    llm = Llama(model_path=MODEL_PATH, n_ctx=N_CTX,
                n_threads=N_THREADS, n_gpu_layers=0, verbose=False)
    used, total = get_ram()
    print(f"✅ Ready — RAM: {used}MB / {total}MB")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: Optional[str] = "nanomind"
    messages: List[Message]
    max_tokens: Optional[int] = 256
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False

@app.get("/health")
def health():
    used, total = get_ram()
    return {"status": "ok", "model_loaded": llm is not None,
            "ram_used_mb": used, "ram_total_mb": total,
            "platform": platform.system(), "version": "0.1.0"}

@app.get("/v1/models")
def models():
    return {"object": "list", "data": [
        {"id": "nanomind", "object": "model", "created": int(time.time())}
    ]}

@app.post("/v1/chat/completions")
def chat(req: ChatRequest):
    if llm is None:
        raise HTTPException(503, "No model loaded. Run: python scripts/download_model.py")
    prompt = ""
    for m in req.messages:
        if   m.role == "system":    prompt += f"<|system|>\n{m.content}<|end|>\n"
        elif m.role == "user":      prompt += f"<|user|>\n{m.content}<|end|>\n"
        elif m.role == "assistant": prompt += f"<|assistant|>\n{m.content}<|end|>\n"
    prompt += "<|assistant|>\n"
    t0  = time.time()
    out = llm(prompt, max_tokens=req.max_tokens, temperature=req.temperature,
              stop=["<|user|>", "<|end|>"], echo=False)
    t1  = time.time()
    text = out["choices"][0]["text"].strip()
    return {
        "id": f"chatcmpl-{int(time.time())}",
        "object": "chat.completion", "created": int(time.time()),
        "model": "nanomind",
        "choices": [{"index": 0, "finish_reason": "stop",
                     "message": {"role": "assistant", "content": text}}],
        "usage": out["usage"],
        "nanomind": {"inference_seconds": round(t1-t0, 2), "local": True, "cloud": False}
    }

if __name__ == "__main__":
    load_model()
    print(f"🚀 NanoMind → http://0.0.0.0:{PORT}")
    print(f"   Docs     → http://localhost:{PORT}/docs")
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="warning")
