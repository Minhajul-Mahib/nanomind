<div align="center">

# 🧠 NanoMind

### The only open-source AI that runs on a 2GB RAM Android phone.
### Offline. Private. Free. For the other 3 billion.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Minhajul-Mahib/nanomind?style=social)](https://github.com/Minhajul-Mahib/nanomind/stargazers)
[![Min RAM](https://img.shields.io/badge/Min%20RAM-1GB-brightgreen)]()

> Every other offline AI tool requires 6GB+ RAM.
> NanoMind runs on 1GB. Built for the other 3 billion.

**[⬇ Download](../../releases/latest)** · **[🌐 nanomind.ink](https://nanomind.ink)** · **[💬 Discord](https://discord.gg/nanomind)**

</div>

---

## The Problem Nobody Solved

Every existing local AI app has the same requirement: **6–8GB RAM**.

That locks out billions of people on budget Android devices.
People in Bangladesh. Nigeria. India. People with $50–80 phones.

**NanoMind runs on 1GB RAM. No exceptions.**

---

## NanoMind vs Everything Else

| | PocketPal | Google AI Edge | Off Grid | **NanoMind** |
|---|---|---|---|---|
| Min RAM | 6GB | 6GB | 6GB | **✅ 1GB** |
| Works on $50 phones | ✗ | ✗ | ✗ | **✅** |
| Works on Raspberry Pi | ✗ | ✗ | ✗ | **✅** |
| Offline | ✅ | ✅ | ✅ | **✅** |
| Open Source | ✅ | ✅ | ✅ | **✅** |
| OpenAI-Compatible API | ✗ | ✗ | ✗ | **✅** |

---

## Quick Start

### Linux / Raspberry Pi
```bash
curl -fsSL https://nanomind.ink/install | bash
```

### Manual
```bash
git clone https://github.com/Minhajul-Mahib/nanomind
cd nanomind
pip install -r server/requirements.txt
python scripts/download_model.py
python server/server.py
```

### OpenAI drop-in replacement
```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")
response = client.chat.completions.create(
    model="nanomind",
    messages=[{"role": "user", "content": "Am I running locally?"}]
)
```

---

## Supported Models

| RAM | Model | Size |
|---|---|---|
| 1GB+ | TinyLlama 1.1B | 0.6GB |
| 2GB+ | Gemma 2B | 1.5GB |
| 3GB+ | Phi-3 Mini ⭐ | 2.2GB |
| 6GB+ | Mistral 7B | 4.1GB |

---

## License
MIT — [Minhajul-Mahib](https://github.com/Minhajul-Mahib) · [nanomind.ink](https://nanomind.ink)

⭐ Star this if you believe AI should work on every phone
