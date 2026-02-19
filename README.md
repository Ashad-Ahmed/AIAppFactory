# AI App Factory

**AI App Factory** is a desktop application that lets you generate, run, edit, and manage Python applications using an LLM.  
Describe the app you want → Generate code → Run instantly → Save & reuse.

Built with **CustomTkinter** + **Groq LLM API**.

---

## Features

- Generate Python apps from natural language descriptions  
- Run generated code instantly  
- Save & reload previously generated apps  
- Export code as standalone `.py` files  
- Light / Dark appearance modes  
- Secure API key configuration  
- Clean IDE-style interface  

---

## Screenshots / Demo

*(Place your app GIFs or screenshots here)*

### Main Interface
![Screenshot Placeholder](docs/screenshots/main_ui.png)

### Code Generation
![Screenshot Placeholder](docs/screenshots/code_generation.png)

### Running Apps
![Screenshot Placeholder](docs/screenshots/running_app.png)

---

## Architecture Overview

AI App Factory follows a simple workflow:

User Prompt → Groq LLM → Generated Python Code → Editor → Execution

**Components:**

- **UI Layer** → CustomTkinter  
- **LLM Layer** → Groq API (`llama-3.3-70b-versatile`)  
- **Execution Layer** → Temporary Python subprocess  
- **Persistence Layer** → Local file system  

---

## Project Structure

```
AI-App-Factory/
│── config.json          # Stores API key & appearance
│── saved_apps/          # Saved applications
│── main.py              # Main application
│── docs/
│   └── screenshots/     # Screenshots / GIFs
```

---

## Installation

### 1️) Clone Repository

```bash
git clone https://github.com/yourusername/ai-app-factory.git
cd ai-app-factory
```

## 2️) Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

## 3️) Install Dependencies

```bash
pip install customtkinter groq
```

---

## API Key Setup

AI App Factory requires a **Groq API key**.

1. Obtain API key from Groq Console  
2. Launch the app  
3. Open **⚙ Settings**  
4. Paste your API key  
5. Save  

Your key is stored locally inside:

```
config.json
```

---

## Usage Guide

### Generate an App

1. Enter a description in **App Description**  
2. Click **Generate App**  
3. Code appears in **Generated Code**

Example prompt:

```
Create a calculator with a modern GUI supporting addition, subtraction, multiplication, division.
```

---

### Run the Code

Click **Run Code** to execute the generated script.

- Code runs in a separate Python process  
- Useful for quick experimentation  

---

### Save an App

Click **Save App** → Provide a name.

Each saved app stores:

- `app.py` → Generated code  
- `meta.json` → Original prompt  

---

### Load a Saved App

1. Select from **Saved Apps** dropdown  
2. Click **Load App**

---

### Export Code

Click **Export .py** to save the script anywhere.

---

## Technologies Used

- CustomTkinter  
- Groq LLM API  
- Python Subprocess Execution  
- Local File Persistence  

---

## Important Notes

- Generated code quality depends on prompt clarity  
- Always review generated code before executing  
- Requires Python installed on system  

---

## Future Scope

AI App Factory can evolve into a much more powerful development tool:

- Built-in Python interpreter sandbox  
- Error capture & debugging assistant  
- Multi-file project generation  
- Dependency auto-installer  
- Plugin / Extension system  
- Code versioning & diff viewer  
- Integrated package builder (EXE)  
- Support for multiple LLM providers  
- Prompt templates & presets  
- Security validation for generated code  

---

## Contributing

Contributions, ideas, and experiments are welcome.

1. Fork repository  
2. Create feature branch  
3. Submit Pull Request  

---

## License

Specify your preferred license here.

Example:

```
MIT License
```
If you'd like next, I can help you craft a **very impressive GitHub repo description + tags** (this actually matters a lot for visibility).

