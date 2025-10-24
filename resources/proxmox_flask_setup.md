# Initial Server Login and Test App Setup

## INITIAL LOGIN

1. Open terminal or console.
2. Get IP address of the target node.
3. Connect via SSH:
   ```bash
   ssh localadmin@<your_ip>
   ```
4. When prompted, enter the password:
   ```
   L0calAdm1n!
   ```
5. Access the Proxmox Web Interface:
   ```
   https://pve.tdm.local:8006
   ```
6. Log in using uppercase username:
   ```
   ROBERJ@tdm.local
   ```
7. Use your assigned **TDM Username and Password**.

---

## TEST APP SETUP

### 1. Update and install dependencies

```bash
apt update
apt install -y python3 python3-venv python3-pip
```

### 2. Create and activate a virtual environment

```bash
mkdir ~/testapp
cd ~/testapp
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Create a simple Flask app

Open the file in Nano:

```bash
nano app.py
```

Paste in the following code:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Proxmox Debian 12 test app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 5. Run the app

```bash
python app.py
```

---

## Verification

Visit the following URL in your browser:

**http://<your-server-ip>:5000**
You should see:

```html
Hello from Proxmox Debian 12 test app!
```
