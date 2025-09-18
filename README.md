# DeepShield

> 🛡️ A Google Chrome extension that detects whether social media content is a **deepfake**.  
Built during the **womENcourage 2025 Hackathon** in Brașov.  

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Demo Scope](#demo-scope)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [Usage](#usage)  
- [Limitations](#limitations)  

---

## About

DeepShield is a **browser extension prototype** that helps users stay safe by detecting whether social media content may have been generated or manipulated with deepfake technology.  

The project was developed as a **demo** during the [womENcourage 2025 Hackathon](https://womencourage.acm.org/) held in **Brașov, Romania**.  

At the moment, the extension focuses on **Instagram posts** and showcases how AI-driven content analysis can integrate seamlessly into users’ browsing experience.

---

## Features

- 🖼️ Inline analysis of Instagram posts  
- 🚨 Alerts when a post may be AI-generated or manipulated  
- 🧩 Easy-to-install Chrome extension  
- ⚡ Built as a proof-of-concept for raising awareness  

---

## Demo Scope

> ⚠️ **Note:** This is a hackathon demo.  
Currently, DeepShield only works with **Instagram posts** and is not a full production-ready product.  

Future iterations could expand support to:  
- Other platforms (Facebook, TikTok, X/Twitter, YouTube, etc.)  
- Real-time video analysis  
- More robust AI/ML detection models  

Below you will find a short clip of the working demo:
![demo video](https://github.com/user-attachments/assets/27408fc2-9741-4649-b360-42a898e2954a)

---

## Getting Started

### Prerequisites

- [Google Chrome](https://www.google.com/chrome/) (latest version)  
- Node.js (>= 16) if you want to rebuild the extension from source  

### Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/AleXutzZu/DeepShield.git
    cd DeepShield
   ```
2. Install dependencies:
    ```bash
    npm install
    npm run build
    ```
3. Load the extension
    - Open Chrome and navigate to ```chrome://extensions/```
    - Enable Developer mode (toggle in the top-right)
    - Click Load unpacked
    - Select the folder containing the extension build (```dist/```)
    - The DeepShield icon should now appear in your browser toolbar 🎉

4. Install python dependencies in the ```server``` folder
   ```bash
   cd server
   pip install -r requirements.txt
   ```
5. Run the FastAPI server locally
   ```bash
    uvicorn server:app --reload --host 0.0.0.0 --port 8000
   ```

## Usage

1. Navigate to Instagram in Chrome

2. Open a post

3. Open the extension by clicking on the icon in the browser toolbar. From there, click the button to check if the post is deepfake and a message will appear afterwards.

## Limitations

- Works only on Instagram posts (demo scope)
- Detection accuracy may be limited — this is a prototype built in a hackathon setting
- Not intended for production use
