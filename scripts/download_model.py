"""
NanoMind Model Downloader
Auto-detects your RAM and picks the best model.
"""
import os, sys, requests
from pathlib import Path

try:
    import psutil
    RAM_GB = psutil.virtual_memory().available / 1024**3
except:
    RAM_GB = 3.0

MODELS = [
    {
        "id": 1,
        "name": "TinyLlama 1.1B — works on 1GB RAM",
        "file": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "size_gb": 0.6, "min_ram_gb": 1.0
    },
    {
        "id": 2,
        "name": "Gemma 2B — works on 2GB RAM",
        "file": "gemma-2b-it-q4_k_m.gguf",
        "url": "https://huggingface.co/lmstudio-ai/gemma-2b-it-GGUF/resolve/main/gemma-2b-it-q4_k_m.gguf",
        "size_gb": 1.5, "min_ram_gb": 2.0
    },
    {
        "id": 3,
        "name": "Phi-3 Mini — RECOMMENDED (3GB RAM)",
        "file": "Phi-3-mini-4k-instruct-q4.gguf",
        "url": "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf",
        "size_gb": 2.2, "min_ram_gb": 3.0
    },
    {
        "id": 4,
        "name": "Mistral 7B — best quality (6GB RAM)",
        "file": "mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "size_gb": 4.1, "min_ram_gb": 6.0
    },
]

def main():
    print(f"\n🧠 NanoMind Model Downloader")
    print(f"   Available RAM: ~{RAM_GB:.1f}GB\n")

    compatible = [m for m in MODELS if m["min_ram_gb"] <= RAM_GB]
    best = compatible[-1] if compatible else MODELS[0]

    for m in MODELS:
        fits = "✓" if RAM_GB >= m["min_ram_gb"] else "✗"
        star = " ← AUTO-SELECTED" if m == best else ""
        print(f"  [{m['id']}] {fits} {m['name']} ({m['size_gb']}GB){star}")

    print()
    choice = input(f"Enter number [Enter = auto-select]: ").strip()

    if choice == "":
        model = best
    else:
        try:
            model = next(m for m in MODELS if m["id"] == int(choice))
        except:
            print("Invalid."); sys.exit(1)

    Path("./models").mkdir(exist_ok=True)
    dest = Path("./models") / model["file"]

    if dest.exists():
        print(f"\n✅ Already downloaded: {dest}")
    else:
        print(f"\n⬇  Downloading {model['name']} ({model['size_gb']}GB)...")
        r = requests.get(model["url"], stream=True)
        total = int(r.headers.get("content-length", 0))
        done = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1024*1024):
                if chunk:
                    f.write(chunk)
                    done += len(chunk)
                    if total:
                        pct = done/total*100
                        bar = "█"*int(pct/2) + "░"*(50-int(pct/2))
                        print(f"\r  [{bar}] {pct:.1f}%", end="", flush=True)
        print(f"\n✅ Done: {dest}")

    with open(".env", "w") as f:
        f.write(f'NANOMIND_MODEL="{dest}"\n')
        ctx = "1024" if model["min_ram_gb"] <= 2 else "2048"
        f.write(f'NANOMIND_CTX={ctx}\nNANOMIND_THREADS=2\n')

    print(f"\n🚀 Now run: python server/server.py\n")

if __name__ == "__main__":
    main()
