# 🚨 Security & Edit Guardian Bot

A state-of-the-art all-rounder Telegram security and moderation bot built with **Python (python-telegram-bot v13)**. It merges robust **Security Bot** bad-word/NSFW screening with **Edit Guardian** accountability, ensuring groups remain transparent, safe, and professional.

---

## ✨ Key Features

- 🛡️ **Advanced Prohibited Content Screening**: Real-time screening across multiple illicit categories (Adult/18+, Illegal Drugs, Piracy, and Violence) covering text messages, captions, photos, videos, GIFs, and stickers. Uses 100% free external providers (PurgoMalum & Sightengine Free-Tier) with strict rate-limit compliance, open-source dictionaries, and exact word boundary (`\b`) regex heuristics.
- ⚡ **Pre-Compressed Media Optimization**: Analyzes pre-compressed Telegram thumbnails (`photo[0]`, `video.thumb`) to ensure instant analysis with virtually zero CPU overhead and minimal bandwidth usage.
- 🚫 **Hybrid Edit Guardian**: Automatically deletes edited messages and media captions in groups to prevent unauthorized modifications after sending.
- ⚙️ **Dynamic Group Configurations**: Group owners and admins can configure their group's enforcement mode via `/setmode <warn_mute | warn | silent>` (persisted in MongoDB / in-memory).
- 📊 **Management Utilities**: Includes live status diagnostics (`/status` with CPU/RAM metrics), statistics (`/stats`), broadcast tools (`/broadcast`, `/announce`), ping latency (`/ping`), and bot cloning (`/clone`).
- ☁️ **Hugging Face Spaces Ready**: Features a built-in background health check server listening on port `7860` for seamless, out-of-the-box hosting on Hugging Face Spaces Docker SDK.

---

## 🛠️ Management Commands

### Group Admin Commands
- `/setmode <warn_mute | warn | silent>` - Set group violation handling mode.
- `/settings` - View current group configuration.

### Owner & Sudo Commands
- `/addsudo <username/ID>` - Add a sudo user.
- `/delsudo <username/ID>` - Remove a sudo user.
- `/sudolist` - List all sudo users.
- `/status` - Live system status (CPU, RAM, OS, Uptime).
- `/stats` - Total tracked users and protected chats.
- `/broadcast <msg>` - Broadcast a message to all tracked users/chats.
- `/announce` - Forward a message to all tracked users/chats.
- `/clone <Bot Token>` - Spin up a new cloned bot instance.

### Public Commands
- `/start` - Check bot liveliness.
- `/help` - Display full help menu.
- `/ping` - Check latency.
- `/id` - Get User, Replied, and Chat IDs.

---

## 💻 Local Testing & Configuration

Before deploying to the cloud, you can easily test the bot locally on your machine.

### 1. Environment Configuration (`.env`)
Create a file named `.env` in the root directory of the project and populate it with the following configuration:

```env
# Required Parameters
TELEGRAM_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
OWNER_ID=123456789

# Optional Parameters
SUPPORT_ID=-1001234567890       # Target Channel/Group ID for moderation logs & startup alerts
MONGO_URI=mongodb+srv://...     # MongoDB connection string (if omitted, bot uses in-memory storage)
SUDO_ID=987654321 112233445     # Space-separated list of additional admin User IDs
SIGHTENGINE_USER=12345678       # Sightengine API User (if omitted, bot uses built-in free tier credentials)
SIGHTENGINE_SECRET=abc123xyz    # Sightengine API Secret
```

### 2. Local Execution Commands
Run the following commands in your terminal to initialize and test the bot:

```bash
# 1. Open project directory
cd Guardian

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 4. Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Start the bot locally
python Guardian/main.py
```

---

## 🚀 Cloud Deployment

### 1. Hugging Face Spaces (Docker SDK)
Deploying to Hugging Face Spaces is fully supported out of the box:
1. Create a new Space on Hugging Face and select **Docker** as the SDK.
2. Upload the repository files. The included `Dockerfile` and internal health check server will automatically bind to port `7860`.
3. Add your environment variables (`TELEGRAM_TOKEN`, `OWNER_ID`, `MONGO_URI`, `SUPPORT_ID`) in the Space settings under **Secrets**.

### 2. Standard Docker
```bash
docker build -t security-edit-guardian .
docker run -d --env-file .env -p 7860:7860 security-edit-guardian
```
