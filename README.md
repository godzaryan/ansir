# **Ansir** 🧠📋  
🚀 **Ansir** is an AI-powered clipboard monitor that automatically detects multiple-choice questions (MCQs), sends them to **Google Gemini AI** for analysis, and displays the correct answer in a sleek **frameless PyQt6 popup**. It also logs all questions and answers for future reference.  

## **🔹 Features**  
✅ **Real-time Clipboard Monitoring** – Detects copied MCQs instantly.  
✅ **AI-Powered Answering** – Uses **Google Gemini AI** for accurate answers.  
✅ **Minimalist Popup Display** – Frameless, translucent answer notifications.  
✅ **Automatic Logging** – Saves questions and answers in `Ansir.log`.  
✅ **Efficient & Lightweight** – Runs in the background with minimal resource usage.  

## **🔹 How It Works**  
1. Copy a **multiple-choice question** from any document or website.  
2. **Ansir** automatically detects the copied text.  
3. It sends the question to **Gemini AI** and retrieves the best answer.  
4. The answer appears in a **sleek popup notification**.  
5. The question & answer are logged in `Ansir.log` for later reference.  

## **🔹 Setup & Installation**  
### **1️⃣ Install Dependencies**  
```sh
pip install google-generativeai pyperclip PyQt6
```

### **2️⃣ Run the Script**  
```sh
python ansir.py
```

## **🔹 Usage**
(It works on the event of clipboard text change)
Simply **copy an MCQ**, and Ansir will display the correct answer to the question on the screen!

---

💡 **Future Enhancements:**  
- Customizable **UI themes** for the popup.  
- **Hotkey support** for toggling clipboard monitoring.  
- **More AI models** for better accuracy.  

📌 **Developed with ❤️ by [godzaryan]**  
🔗 **[https://github.com/godzaryan/ansir]**  
