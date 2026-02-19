import customtkinter as ctk
import tempfile
import subprocess
import os
import json
from datetime import datetime
from groq import Groq

# ------------------ FILES ------------------

CONFIG_FILE = "config.json"
SAVE_DIR = "saved_apps"
os.makedirs(SAVE_DIR, exist_ok=True)

# ------------------ CONFIG HANDLING ------------------


def load_config():
    if not os.path.exists(CONFIG_FILE):
        default = {"api_key": "", "appearance": "dark"}
        with open(CONFIG_FILE, "w") as f:
            json.dump(default, f, indent=4)
        return default

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)


config = load_config()

ctk.set_appearance_mode(config.get("appearance", "dark"))
ctk.set_default_color_theme("blue")

MODEL = "llama-3.3-70b-versatile"

# ------------------ LLM ------------------


class GroqLLM:
    def __init__(self, api_key):
        self.update_key(api_key)

    def update_key(self, api_key):
        self.api_key = api_key
        self.client = Groq(api_key=api_key) if api_key else None

    def invoke(self, prompt):
        if not self.client:
            raise RuntimeError("API key not configured")

        completion = self.client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content


llm = GroqLLM(config.get("api_key", ""))

# ------------------ SETTINGS DIALOG ------------------


class SettingsDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Settings")
        self.geometry("420x320")
        self.resizable(False, False)
        self.grab_set()

        ctk.CTkLabel(self, text="Appearance", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(20, 5))

        self.appearance_option = ctk.CTkOptionMenu(self, values=["dark", "light"])
        self.appearance_option.set(config.get("appearance", "dark"))
        self.appearance_option.pack(pady=5)

        ctk.CTkLabel(self, text="Groq API Key", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(20, 5))

        self.api_entry = ctk.CTkEntry(self, show="*", width=320)
        self.api_entry.pack()
        self.api_entry.insert(0, config.get("api_key", ""))

        ctk.CTkButton(self, text="Save Settings", command=self.save).pack(pady=30)

    def save(self):
        config["appearance"] = self.appearance_option.get()
        config["api_key"] = self.api_entry.get().strip()

        save_config(config)

        ctk.set_appearance_mode(config["appearance"])
        llm.update_key(config["api_key"])

        self.destroy()


# ------------------ APP ------------------


class AppFactory(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI App Factory")
        self.geometry("1200x750")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.build_sidebar()
        self.build_main_panel()

    # ------------------ SIDEBAR ------------------

    def build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=260, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_propagate(False)  # LOCK WIDTH

        ctk.CTkLabel(
            self.sidebar,
            text="AI App Factory",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=(30, 20))

        ctk.CTkButton(self.sidebar, text="Generate App", command=self.generate_code).pack(padx=20, pady=8, fill="x")
        ctk.CTkButton(self.sidebar, text="Run Code", command=self.run_code, fg_color="#2E8B57").pack(padx=20, pady=8, fill="x")
        ctk.CTkButton(self.sidebar, text="Save App", command=self.save_app).pack(padx=20, pady=8, fill="x")
        ctk.CTkButton(self.sidebar, text="Export .py", command=self.export_code, fg_color="#444").pack(padx=20, pady=8, fill="x")

        ctk.CTkLabel(self.sidebar, text="Saved Apps", font=ctk.CTkFont(weight="bold")).pack(pady=(25, 5))

        self.saved_apps_dropdown = ctk.CTkOptionMenu(self.sidebar, values=["No saved apps"], width=220)
        self.saved_apps_dropdown.pack(padx=20, pady=5, fill="x")

        ctk.CTkButton(self.sidebar, text="Load App", command=self.load_selected_app).pack(padx=20, pady=5, fill="x")
        ctk.CTkButton(self.sidebar, text="Refresh Apps", command=self.refresh_saved_apps, fg_color="#333").pack(padx=20, pady=5, fill="x")

        bottom_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        bottom_frame.pack(side="bottom", fill="x", pady=10)

        ctk.CTkButton(
            bottom_frame,
            text="⚙ Settings",
            command=self.open_settings,
            fg_color="#222",
            height=42
        ).pack(padx=20, pady=(0, 8), fill="x")

        self.status_label = ctk.CTkLabel(bottom_frame, text="Idle", text_color="gray")
        self.status_label.pack()

        self.refresh_saved_apps()

    # ------------------ MAIN PANEL ------------------

    def build_main_panel(self):
        main = ctk.CTkFrame(self)
        main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        main.grid_rowconfigure(1, weight=5)
        main.grid_rowconfigure(3, weight=3)
        main.grid_rowconfigure(5, weight=1)
        main.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(main, text="App Description", font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, sticky="w", padx=10)

        self.prompt_input = ctk.CTkTextbox(main, font=("Segoe UI", 15))
        self.prompt_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(main, text="Generated Code", font=ctk.CTkFont(size=16, weight="bold")).grid(row=2, column=0, sticky="w", padx=10)

        self.code_editor = ctk.CTkTextbox(main, font=("Consolas", 13))
        self.code_editor.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(main, text="Output Console", font=ctk.CTkFont(size=16, weight="bold")).grid(row=4, column=0, sticky="w", padx=10)

        self.output_console = ctk.CTkTextbox(main, height=80, font=("Consolas", 12), text_color="#00FFAA")
        self.output_console.grid(row=5, column=0, sticky="ew", padx=10, pady=(5, 10))

    # ------------------ SETTINGS ------------------

    def open_settings(self):
        SettingsDialog(self)

    # ------------------ CORE LOGIC ------------------

    def generate_code(self):
        try:
            self.output_console.delete("0.0", "end")

            prompt = self.prompt_input.get("0.0", "end").strip()
            self.set_status("Generating...", "orange")

            code = llm.invoke(prompt)

            if code.startswith("```"):
                code = "\n".join(l for l in code.splitlines() if not l.strip().startswith("```"))

            self.code_editor.delete("0.0", "end")
            self.code_editor.insert("0.0", code)

            self.set_status("Done", "green")

        except Exception as e:
            self.output_console.insert("0.0", str(e))
            self.set_status("Error", "red")

    def run_code(self):
        code = self.code_editor.get("0.0", "end")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
            f.write(code)
            subprocess.Popen(["python", f.name], shell=True)

        self.set_status("App Running", "green")

    def save_app(self):
        name = ctk.CTkInputDialog(text="Enter app name:", title="Save App").get_input()
        if not name:
            return

        path = os.path.join(SAVE_DIR, name)
        os.makedirs(path, exist_ok=True)

        with open(os.path.join(path, "app.py"), "w", encoding="utf-8") as f:
            f.write(self.code_editor.get("0.0", "end"))

        with open(os.path.join(path, "meta.json"), "w", encoding="utf-8") as f:
            json.dump({"prompt": self.prompt_input.get("0.0", "end")}, f, indent=4)

        self.refresh_saved_apps()
        self.set_status("Saved", "green")

    def refresh_saved_apps(self):
        apps = [d for d in os.listdir(SAVE_DIR) if os.path.isdir(os.path.join(SAVE_DIR, d))]
        if not apps:
            apps = ["No saved apps"]

        self.saved_apps_dropdown.configure(values=apps)
        self.saved_apps_dropdown.set(apps[0])

    def load_selected_app(self):
        name = self.saved_apps_dropdown.get()
        if name == "No saved apps":
            return

        path = os.path.join(SAVE_DIR, name)

        with open(os.path.join(path, "app.py"), "r", encoding="utf-8") as f:
            self.code_editor.delete("0.0", "end")
            self.code_editor.insert("0.0", f.read())

        with open(os.path.join(path, "meta.json"), "r", encoding="utf-8") as f:
            meta = json.load(f)
            self.prompt_input.delete("0.0", "end")
            self.prompt_input.insert("0.0", meta.get("prompt", ""))

        self.set_status(f"Loaded {name}", "green")

    def export_code(self):
        path = ctk.filedialog.asksaveasfilename(defaultextension=".py")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.code_editor.get("0.0", "end"))

    def set_status(self, text, color):
        self.status_label.configure(text=text, text_color=color)


if __name__ == "__main__":
    AppFactory().mainloop()
