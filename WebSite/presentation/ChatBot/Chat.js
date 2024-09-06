const API_KEY = "AIzaSyBt74-KD_u2evlPs4fdmmslZrl-0LpfkVQ";
const recognition = new webkitSpeechRecognition();
recognition.lang = 'en-US'; // Adjust language as needed
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const voiceInputButton = document.getElementById("voice-input");
const chatMessages = document.querySelector(".chat-messages");

voiceInputButton.addEventListener("click", () => {
    recognition.start();
});

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    messageInput.value = transcript;
    messageInput.disabled = false;
};

sendButton.addEventListener("click", () => {
    const userMessage = messageInput.value;
    if (userMessage) {
        // Send the message to Gemini API
        // ... (similar to the previous response)
    }
});