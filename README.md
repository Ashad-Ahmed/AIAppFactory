# AI App Factory

An intelligent desktop application that generates, runs, and manages Python applications using AI. Simply describe what you want, and AI will generate the code for you.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Demo](#demo)
- [Future Scope](#future-scope)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**AI App Factory** is a powerful tool that bridges the gap between idea and implementation. Powered by the Groq LLM (Llama 3.3-70B), it allows developers and non-developers alike to:

- Describe an application in natural language
- Generate production-ready Python code instantly
- Execute code directly within the application
- Save and manage multiple AI-generated applications
- Fine-tune generated code before execution

This tool is perfect for rapid prototyping, learning, automation, and creative experimentation.

---

## ✨ Features

### Core Features

- **AI Code Generation**: Uses Groq's Llama 3.3-70B model to generate Python code from natural language descriptions
- **Live Code Editor**: Edit and refine generated code with syntax highlighting
- **Code Execution**: Run generated Python applications directly within the app
- **Save & Load**: Store generated applications with metadata for future use
- **Export Functionality**: Export generated code as standalone `.py` files
- **Output Console**: Real-time execution output and error messages

### User Interface

- **Modern Dark/Light Theme**: Customizable appearance modes
- **Intuitive Layout**: Three-panel design with description input, code editor, and console output
- **Quick Access Sidebar**: Easy navigation with quick action buttons
- **App Management**: Dropdown menu to load previously saved applications

### Configuration

- **API Key Management**: Secure storage of Groq API credentials
- **Settings Dialog**: Configure appearance and API settings
- **Persistent Configuration**: Settings saved in `config.json`

### Data Management

- **Automatic App Storage**: Save generated apps with metadata in `saved_apps/` directory
- **Metadata Preservation**: Original prompts stored alongside generated code
- **Refresh Capability**: Dynamically load available saved applications

---

## 📦 Requirements

### System Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Internet Connection**: Required for Groq API calls

### Software Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| customtkinter | Latest | Modern GUI framework |
| groq | >=0.4.0 | Groq API client |
| Python stdlib | Built-in | File handling, JSON, subprocess, tempfile |

---

## 🚀 Installation

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/yourusername/AIAppFactory.git
cd AIAppFactory
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install customtkinter groq
```

### Step 4: Obtain Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up for a free account
3. Generate an API key
4. Keep this key handy for configuration

### Step 5: Run the Application

```bash
python ai_app_factory.py
```

---

## 📖 Usage

### 1. Initial Setup

On first launch, the application will create:
- `config.json` - Configuration file
- `saved_apps/` - Directory for saved applications

### 2. Configure API Key

1. Click the **⚙ Settings** button in the bottom-left corner
2. Enter your Groq API key in the "Groq API Key" field
3. (Optional) Switch between "dark" and "light" appearance
4. Click **Save Settings**

### 3. Generate Code

1. **Describe Your App**: Type a detailed description of what you want in the "App Description" box
   - Example: "Create a calculator app with addition, subtraction, multiplication, and division operations"
   - Be specific for better results
2. Click **Generate App** button
3. Wait for the AI to generate code (status shows "Generating...")
4. Generated code appears in the "Generated Code" section

### 4. Run Generated Code

1. Review the generated code in the code editor
2. (Optional) Make edits if needed
3. Click **Run Code** button
4. The application will execute in a new window
5. Console output appears in the "Output Console"

### 5. Save Your Application

1. Click **Save App** button
2. Enter a unique name for your application
3. The app metadata (prompt + code) is saved to `saved_apps/{app_name}/`
4. Application appears in the "Saved Apps" dropdown

### 6. Load Saved Applications

1. Select an app from the "Saved Apps" dropdown
2. Click **Load App**
3. Original prompt and code are restored for editing

### 7. Export Code

1. Click **Export .py** button
2. Choose a location and filename
3. Code is saved as a standalone Python file

---

## ⚙️ Configuration

### Configuration File: `config.json`

```json
{
    "api_key": "your_groq_api_key_here",
    "appearance": "dark"
}
```

**Note**: API key is stored locally. Keep it secure and never commit to version control.

### Environment Variables (Optional)

You can set the API key via environment variable instead of the GUI:

```bash
export GROQ_API_KEY="your_api_key"
```

Then modify the code to read from environment:

```python
api_key = config.get("api_key", os.getenv("GROQ_API_KEY", ""))
```

---

## 📁 Project Structure

```
AIAppFactory/
├── ai_app_factory.py          # Main application file
├── config.json                # Configuration (auto-generated)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── saved_apps/                # Directory for saved applications
    ├── app_name_1/
    │   ├── app.py
    │   └── meta.json
    └── app_name_2/
        ├── app.py
        └── meta.json
```

---

## 🎬 Demo

### Screenshot 1: Main Interface
[Insert screenshot of main application window here]

### Screenshot 2: Code Generation
[Insert screenshot showing generated code in editor]

### Screenshot 3: Settings Dialog
[Insert screenshot of settings configuration window]

### Screenshot 4: Saved Apps Management
[Insert screenshot showing saved apps dropdown and load functionality]

### Video Demo
[Insert link to demo video here]

---

## 🔮 Future Scope

### Phase 2 - Enhanced Code Generation
- [ ] **Multi-Language Support**: Generate code in JavaScript, Java, C++, etc.
- [ ] **Framework Integration**: Built-in support for Flask, Django, FastAPI
- [ ] **Code Templates**: Pre-built templates for common app types
- [ ] **AI Model Selection**: Choose between different Groq models based on complexity
- [ ] **Context-Aware Generation**: Remember conversation history for better code suggestions

### Phase 3 - Advanced Features
- [ ] **Web UI**: Browser-based interface using Flask/FastAPI
- [ ] **Real-time Collaboration**: Share projects and collaborate with team members
- [ ] **Version Control**: Built-in Git integration for code versioning
- [ ] **Code Analysis**: Static analysis, code quality metrics, and suggestions
- [ ] **Debugging Tools**: Integrated debugger and profiler
- [ ] **Testing Suite**: Automatic test generation and execution

### Phase 4 - Intelligence Enhancements
- [ ] **Code Optimization**: AI-powered code optimization suggestions
- [ ] **Performance Analysis**: Identify bottlenecks and optimization opportunities
- [ ] **Security Scanning**: Detect security vulnerabilities in generated code
- [ ] **Documentation Generation**: Automatic docstring and README generation
- [ ] **Code Refactoring**: Suggest and apply code refactoring patterns

### Phase 5 - Ecosystem
- [ ] **Plugin System**: Allow community-contributed plugins and extensions
- [ ] **Cloud Storage**: Save apps to cloud with Google Drive/OneDrive integration
- [ ] **API Endpoints**: Expose functionality via REST API
- [ ] **Mobile App**: Native mobile application for iOS/Android
- [ ] **Marketplace**: Share and discover generated apps in community marketplace

### Phase 6 - Enterprise Features
- [ ] **User Authentication**: Multi-user support with authentication
- [ ] **Role-Based Access**: Different permission levels for team members
- [ ] **Audit Logging**: Track all code generation and execution activities
- [ ] **API Rate Limiting**: Manage API usage and costs
- [ ] **Custom Models**: Support for fine-tuned custom LLMs

---

## 🐛 Troubleshooting

### Issue: "API key not configured"

**Solution**: 
1. Open Settings (⚙ button)
2. Enter a valid Groq API key
3. Click Save Settings

### Issue: Generated code doesn't run

**Possible Causes**:
- The AI generated code with dependencies not installed
- The code has syntax errors
- The generated code tries to use features not available in the current Python version

**Solution**:
1. Review the generated code carefully
2. Edit and fix any issues
3. Install missing dependencies if needed
4. Ensure you're using Python 3.8+

### Issue: Application won't start

**Solution**:
1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Check Python version: `python --version` (should be 3.8+)
3. Delete `config.json` and restart (it will recreate with defaults)

### Issue: API calls are slow

**Solution**:
- Check your internet connection
- Groq API might be experiencing high load - try again later
- Simplify your prompt for faster generation

### Issue: Application crashes on code execution

**Solution**:
1. The generated code might have infinite loops or resource issues
2. Review the code before running
3. Close the application window if it becomes unresponsive

---

## 📝 Code Examples

### Example 1: Simple Calculator

**Prompt**:
```
Create a simple calculator GUI with buttons for addition, subtraction, multiplication, and division. Include a display for showing results.
```

**Generated Code Preview**:
The AI will generate a complete calculator application with all requested features.

### Example 2: File Manager

**Prompt**:
```
Create a file manager GUI that allows users to browse directories, view files, delete files, and rename files.
```

### Example 3: Task Manager

**Prompt**:
```
Build a task management application with the ability to add tasks, mark them as complete, delete tasks, and save the task list to a JSON file.
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code Style Guidelines
- Follow PEP 8 guidelines
- Add comments for complex logic
- Update README for new features
- Test thoroughly before submitting

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support & Contact

- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Join community discussions on GitHub Discussions
- **Email**: [your-email@example.com]
- **Discord**: [Join our Discord server]

---

## 🙏 Acknowledgments

- **Groq** for providing the powerful Llama 3.3-70B model and API
- **CustomTkinter** for the modern GUI framework
- **Python Community** for amazing tools and libraries

---

## 📈 Roadmap

**v1.1** (Next Release)
- [ ] Improved error handling
- [ ] Code syntax highlighting
- [ ] Keyboard shortcuts

**v1.5** (Mid-term)
- [ ] Web UI
- [ ] Multi-language support
- [ ] Code templates library

**v2.0** (Long-term)
- [ ] Cloud integration
- [ ] Collaboration features
- [ ] Advanced debugging tools

---

**Last Updated**: February 2026  
**Current Version**: 1.0.0
