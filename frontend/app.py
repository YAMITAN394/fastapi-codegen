import gradio as gr

# Function to generate content
def generate_content(prompt):
    # Here you would integrate your content generation logic, e.g., using a language model
    return f"ai: {prompt}"

# Function to add messages to the chat history
def add_message(prompt, chat_history):
    response = generate_content(prompt)
    chat_history.append(("You: " + prompt, "Ad Genius: " + response))  # Append the new message and response as a tuple
    return chat_history, ""  # Clear the input textbox after submission

# Ultra-stylish CSS with enhanced color effects
css = """
/* Main container styling with even cooler background */
.gradio-container {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient-animation 15s ease infinite;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    font-family: 'Poppins', sans-serif;
    padding: 20px;
    margin: 0;
    min-height: 100vh;
}

@keyframes gradient-animation {
    0% { background-position: 0% 50% }
    50% { background-position: 100% 50% }
    100% { background-position: 0% 50% }
}

/* Cyber-neon title styling */
#title {
    font-size: 60px;
    font-weight: 900;
    text-align: center;
    color: #ffffff;
    margin: 20px 0 10px 0;
    letter-spacing: 3px;
    text-transform: uppercase;
    animation: cyber-glow 2s ease-in-out infinite alternate;
    text-shadow: 0 0 5px #00fffc, 0 0 10px #00fffc, 0 0 20px #00fffc, 0 0 40px #00fffc;
}

@keyframes cyber-glow {
    from {
        text-shadow: 0 0 5px #00fffc, 0 0 10px #00fffc, 0 0 20px #00fffc, 0 0 40px #00fffc;
    }
    to {
        text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de, 0 0 30px #ff00de, 0 0 50px #ff00de;
    }
}

#subtitle {
    font-size: 28px;
    font-style: italic;
    text-align: center;
    color: #ffffff;
    opacity: 0.95;
    margin-bottom: 40px;
    letter-spacing: 2px;
    text-shadow: 0 0 10px rgba(0, 255, 252, 0.7);
}

/* Chatbot styling - more futuristic */
.chatbot {
    border-radius: 20px !important;
    overflow: hidden;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    background-color: rgba(15, 15, 35, 0.7) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 5px !important;
}

.message {
    border-radius: 16px !important;
    padding: 15px !important;
    margin: 10px 5px !important;
    max-width: 85% !important;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.user {
    background: linear-gradient(135deg, #6e48aa, #9e37d1) !important;
    color: white !important;
    border-bottom-right-radius: 0 !important;
    margin-left: auto !important;
    position: relative;
    animation: message-pop 0.3s ease-out;
}

.bot {
    background: linear-gradient(135deg, #134e5e, #71b280) !important;
    color: white !important;
    border-bottom-left-radius: 0 !important;
    margin-right: auto !important;
    position: relative;
    animation: message-pop 0.3s ease-out;
}

@keyframes message-pop {
    0% { transform: scale(0.8); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

/* Input area styling - ultra cool */
.input-container {
    margin-top: 20px !important;
    position: relative;
    z-index: 1;
}

#prompt {
    border-radius: 50px !important;
    border: none !important;
    padding: 20px 25px !important;
    font-size: 18px !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(10px) !important;
    color: white !important;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2), inset 0 0 10px rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
}

#prompt::placeholder {
    color: rgba(255, 255, 255, 0.8);
}

#prompt:focus {
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.25), 0 0 20px rgba(0, 255, 252, 0.4), inset 0 0 10px rgba(255, 255, 255, 0.1) !important;
    transform: translateY(-5px) !important;
    background: rgba(255, 255, 255, 0.2) !important;
    outline: none !important;
}

/* Button styling - next level */
#submit-btn {
    background: linear-gradient(45deg, #FF416C, #FF4B2B) !important;
    border: none !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 50px !important;
    padding: 15px 30px !important;
    cursor: pointer !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    box-shadow: 0 10px 20px rgba(255, 75, 43, 0.4), 0 0 0 5px rgba(255, 75, 43, 0.1) !important;
    animation: button-pulse 1.5s infinite;
    font-size: 16px !important;
}

@keyframes button-pulse {
    0% { box-shadow: 0 10px 20px rgba(255, 75, 43, 0.4), 0 0 0 0 rgba(255, 75, 43, 0.6); }
    70% { box-shadow: 0 10px 20px rgba(255, 75, 43, 0.4), 0 0 0 15px rgba(255, 75, 43, 0); }
    100% { box-shadow: 0 10px 20px rgba(255, 75, 43, 0.4), 0 0 0 0 rgba(255, 75, 43, 0); }
}

#submit-btn:hover {
    transform: translateY(-5px) scale(1.05) !important;
    box-shadow: 0 15px 25px rgba(255, 75, 43, 0.5), 0 0 0 5px rgba(255, 75, 43, 0.2) !important;
    background: linear-gradient(45deg, #FF416C, #FF9676) !important;
}

#submit-btn:active {
    transform: translateY(0) scale(0.98) !important;
}

/* Footer with cool styling */
.footer {
    text-align: center;
    color: white;
    margin-top: 30px;
    font-size: 16px;
    opacity: 0.9;
    text-shadow: 0 0 10px rgba(0, 255, 252, 0.5);
    padding: 15px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Adding cool highlighting effect for the generated content */
.bot p {
    position: relative;
    z-index: 1;
    animation: highlight-text 1s ease-out;
}

@keyframes highlight-text {
    0% { color: #00fffc; text-shadow: 0 0 8px #00fffc; }
    100% { color: white; text-shadow: none; }
}

/* Responsive adjustments */
" \
"