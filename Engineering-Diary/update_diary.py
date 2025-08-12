import os
from datetime import datetime

# Folder containing your .py files
CODE_FOLDER = "/home/lamar/Documents/SELF-TAUGHT-AI-ENGINEERING/Months:1-3:Foundation (AI Science + Engineering Basics)/Weeks:1-4:Python-Programming:Focus-on-AI"  # Change to your repo path

# Output Markdown file
OUTPUT_FILE = "ENGINEERING_DIARY.md"

# Template for each log entry
def create_log_entry(file_name, mod_date):
    return f"""
## 📅 Date: {mod_date}

### 🔧 What I Did Today:
- Created/updated **{file_name}**.

### ⚠️ Challenges:
- TBD.

### 💡 How I Handled It:
- TBD.

### 📈 Things to Work On:
- TBD.

---
"""

# Step 1: Get last date in existing diary (if exists)
last_logged_date = None
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in reversed(lines):
            if line.startswith("## 📅 Date:"):
                last_logged_date = datetime.strptime(line.strip()[11:], "%B %d, %Y")
                break

# Step 2: Get all .py files and their modified dates
py_files = []
for f in os.listdir(CODE_FOLDER):
    if f.endswith(".py"):
        mod_time = os.path.getmtime(os.path.join(CODE_FOLDER, f))
        mod_date = datetime.fromtimestamp(mod_time)
        py_files.append((f, mod_date))

# Step 3: Filter only new files (if last_logged_date exists)
if last_logged_date:
    py_files = [(f, d) for f, d in py_files if d > last_logged_date]

# Step 4: Sort by modification date
py_files.sort(key=lambda x: x[1])

# Step 5: Append to diary
if py_files:
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        for file_name, mod_date in py_files:
            formatted_date = mod_date.strftime("%B %d, %Y")
            f.write(create_log_entry(file_name, formatted_date))
    print(f"✅ Added {len(py_files)} new entries to {OUTPUT_FILE}")
else:
    print("📭 No new Python files since last log.")
