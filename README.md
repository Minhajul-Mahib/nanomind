<div align="center">

# 🧠 NanoMind

### The only open-source AI that runs on a 2GB RAM Android phone.
### Offline. Private. Free. For the other 3 billion.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Minhajul-Mahib/nanomind?style=social)](https://github.com/Minhajul-Mahib/nanomind/stargazers)
[![Min RAM](https://img.shields.io/badge/Min%20RAM-1GB-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.9+-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Raspberry%20Pi-lightgrey)]()

<br>

> **Every other offline AI tool requires 6GB+ RAM — locking out billions of people.**
> **NanoMind runs on 1GB. Built for the other 3 billion.**

**[🌐 nanomind.ink](https://nanomind.ink)** · **[💬 Discord](https://discord.gg/TYt5bnnNun)** · **[📖 Docs](docs/SETUP.md)**

</div>

---

## The Problem Nobody Solved

Every existing local AI app — PocketPal, Google AI Edge, Off Grid — has the same requirement: **6–8GB RAM**.

That locks out:
- ❌ Budget Android phones ($50–80 range)
- ❌ Raspberry Pi with 2GB RAM
- ❌ Old laptops with 4GB RAM
- ❌ Billions of people who can't afford flagship devices

**NanoMind is built specifically for these devices.**

---

## NanoMind vs Everything Else

| | PocketPal | Google AI Edge | Off Grid | **NanoMind** |
|---|---|---|---|---|
| Min RAM | 6GB | 6GB | 6GB | **✅ 1GB** |
| Works on budget phones | ✗ | ✗ | ✗ | **✅ Yes** |
| Works on Raspberry Pi | ✗ | ✗ | ✗ | **✅ Yes** |
| 100% Offline | ✅ | ✅ | ✅ | **✅ Yes** |
| Open Source | ✅ | ✅ | ✅ | **✅ MIT** |
| OpenAI-Compatible API | ✗ | ✗ | ✗ | **✅ Yes** |

---

## Current Status

| Platform | Status |
|---|---|
| 🐧 Linux / Raspberry Pi | ✅ Available now |
| 🍎 macOS | ✅ Available now |
| 🪟 Windows | ✅ Available now |
| 📱 Android APK | 🔨 Coming in v0.2 |
| 🍏 iOS | 📋 Planned |

---

## Quick Start (Linux / Mac / Windows / Raspberry Pi)

**Step 1 — Clone and install**
```bash
git clone https://github.com/Minhajul-Mahib/nanomind
cd nanomind
pip install -r server/requirements.txt
```

**Step 2 — Download a model (auto-picks best for your RAM)**
```bash
python scripts/download_model.py
```

**Step 3 — Start NanoMind**
```bash
python server/server.py
# → Running at http://localhost:8080
# → API docs at http://localhost:8080/docs
```

**Step 4 — Chat with it**
```python
from openai import OpenAI

# Works with ANY app built for OpenAI — just change the base_url
client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")

response = client.chat.completions.create(
    model="nanomind",
    messages=[{"role": "user", "content": "Am I running locally?"}]
)
print(response.choices[0].message.content)
# → "Yes. 100% on your device. Zero data sent anywhere."
```

---

## Supported Models (Auto-Selected Based on Your RAM)

| RAM Available | Model | Size | Quality |
|---|---|---|---|
| 1GB+ | TinyLlama 1.1B | 0.6 GB | Basic |
| 2GB+ | Gemma 2B | 1.5 GB | Good |
| 3GB+ | **Phi-3 Mini** ⭐ | 2.2 GB | Great — recommended |
| 6GB+ | Mistral 7B | 4.1 GB | Excellent |

The installer detects your RAM automatically and picks the right model.
No manual hunting on HuggingFace required.

---

## Architecture

```
Your Device (1GB RAM minimum)
┌─────────────────────────────────────┐
│  NanoMind Server (Python)           │
│  ┌─────────────────────────────┐    │
│  │  FastAPI                    │    │
│  │  OpenAI-compatible API      │    │
│  │  /v1/chat/completions       │    │
│  └──────────────┬──────────────┘    │
│  ┌──────────────┴──────────────┐    │
│  │  llama-cpp-python           │    │
│  │  4-bit quantized inference  │    │
│  │  CPU-only — no GPU needed   │    │
│  └──────────────┬──────────────┘    │
│  ┌──────────────┴──────────────┐    │
│  │  GGUF Model (local file)    │    │
│  │  TinyLlama / Gemma / Phi-3  │    │
│  └─────────────────────────────┘    │
│                                     │
│  ⚠ Zero internet after setup       │
│  ⚠ Zero telemetry ever             │
└─────────────────────────────────────┘
```

---

## Roadmap

- [x] v0.1 — Python API server (OpenAI-compatible)
- [x] v0.1 — Auto model downloader (detects RAM, picks best model)
- [x] v0.1 — Linux / Mac / Windows / Raspberry Pi support
- [ ] v0.2 — Android APK ← **in progress**
- [ ] v0.2 — In-app model browser
- [ ] v0.3 — Voice input/output
- [ ] v0.3 — Chat with local files (RAG)
- [ ] v0.4 — iOS support
- [ ] v1.0 — Plugin system

---

## Contributing

We especially need:
- **Testers** — run it on your device and report RAM usage + tokens/sec
- **Android developers** — help build the APK
- **Translators** — make NanoMind accessible in more languages

```bash
git clone https://github.com/Minhajul-Mahib/nanomind
cd nanomind
pip install -r server/requirements.txt
python server/server.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) · Join [Discord](https://discord.gg/TYt5bnnNun)

---

## Why This Matters

Most AI progress benefits people with expensive hardware.
NanoMind is built on the belief that private, local AI should work
for **everyone** — not just people with flagship phones.

If you have a $50 Android phone, you deserve AI that respects your privacy too.

---

<div align="center">

Built by [@Minhajul-Mahib](https://github.com/Minhajul-Mahib) · [nanomind.ink](https://nanomind.ink) · MIT License

**⭐ Star this repo if you believe AI should work on every device**

</div>
