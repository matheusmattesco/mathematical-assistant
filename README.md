# Mathematical Assistant

This project is a **smart chatbot** that can:
- Answer general questions using an **AI model (Gemma-2b-it)**.  
- Solve **basic math expressions** (addition, multiplication, division, etc.).  
- Handle **complex math operations** (derivatives, integrals, logarithms, trigonometric functions) using **SymPy**.  

---

## Features

- Natural conversation using Hugging Face `transformers`.  
- Detects when the input is **basic math** (solves with Python `eval`).  
- Detects when the input is **complex math** (solves with **SymPy**).  

---

##  Requirements

- Python 3.10 or newer
- Hugging Face account with a free token
- Libraries in `requirements.txt`

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/matheusmattesco/mathematical-assistant.git
   cd mathematical-assistant
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get a Hugging Face Token**
   - Go to [Hugging Face](https://huggingface.co/join) and create a free account.
   - Navigate to [Access Tokens](https://huggingface.co/settings/tokens).
   - Click **New token** → Choose **Read** access → Copy the token.

5. **Create a `.env` file in the project root**
   ```
   HF_TOKEN=your_huggingface_token_here
   ```

6. **Run the chatbot**
   ```bash
   python main.py
   ```
---

### Example 1: General Question
```
You: Hello, how are you?
[AI] I'm doing well, thank you! How can I help you today?
```

### Example 2: Basic Math
```
You: 128 times 46
[Calculator] 5888
```

### Example 3: Division
```
You: 100 divided by 4
[Calculator] 25.0
```

### Example 4: Complex Math (Derivative)
```
You: derivative(x^2 + 3*x, x)
[Complex Calculator] 2*x + 3
```

### Example 5: Complex Math (Integral)
```
You: integral(sin(x), x)
[Complex Calculator] -cos(x)
```

### Example 6: Square Root + Logarithm
```
You: sqrt(144) + log(10)
[Complex Calculator] log(10) + 12
```

### Example 7: Exponential
```
You: exp(2) + 3
[Complex Calculator] E**2 + 3
```

---

# Future Improvements

This project currently runs in the terminal, but there are several improvements that could enhance usability and expand functionality:

## 1. Streamlit Integration
A natural next step would be to implement the project using **Streamlit**, providing a clean and interactive web interface instead of a command-line interaction.  
With Streamlit, users would be able to:
- Type or paste their questions directly in a browser.
- View results from the AI, basic calculator, or symbolic calculator in a more user-friendly layout.
- Add visualizations for mathematical expressions, such as graphs of functions, derivatives, or integrals.

Example features with Streamlit:
- Graph plots for functions (using SymPy + Matplotlib).
- History of interactions displayed in real time.

## 2. Extended APIs
The system could also be expanded to integrate with other public APIs, such as:
- **WolframAlpha API** for advanced symbolic and numerical results.
- **Finance APIs** for currency, stock, and crypto prices.
- **Science APIs** for retrieving constants, physics data, or astronomy calculations.

---

