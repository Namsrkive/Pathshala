function toggleChat() {
    var chatWindow = document.getElementById('chatWindow');
    var displayStyle = chatWindow.style.display;
    chatWindow.style.display = displayStyle === 'block' ? 'none' : 'block';
}

function sendMessage() {
    var chatInput = document.getElementById('chatInput');
    var messageText = chatInput.value.trim();
    if (messageText !== '') {
        var chatBody = document.getElementById('chatBody');

        var userMessage = document.createElement('div');
        userMessage.className = 'message user-message';
        userMessage.textContent = messageText;
        chatBody.appendChild(userMessage);

        chatInput.value = '';
        chatBody.scrollTop = chatBody.scrollHeight;

        // Simulate bot response
        setTimeout(function() {
            var botMessage = document.createElement('div');
            botMessage.className = 'message bot-message';
            botMessage.innerHTML = `
                <div class="bot-info">
                    <span>Path Sathi</span> <span class="bot-role">Support Agent</span>
                </div>
                <div class="bot-text">${getBotResponse(messageText)}</div>
            `;
            chatBody.appendChild(botMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
        }, 1000);
    }
}

function getBotResponse(message) {
    var responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm here to help you!",
        "what is your name": "I'm Path Sathi, your support agent.",
        "help": "Sure, I'm here to help! What do you need assistance with?",
        "contact": "You can contact us at support@pathshala.com.",
        "services": "We offer a variety of educational services. Visit our Services page for more info.",
        "goodbye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!"
    };
    var lowerCaseMessage = message.toLowerCase().trim();
    return responses[lowerCaseMessage] || "I'm sorry, I don't understand that. Can you please rephrase?";
}

function toggleEmojiPicker() {
    var emojiPicker = document.getElementById('emojiPicker');
    var displayStyle = emojiPicker.style.display;
    emojiPicker.style.display = displayStyle === 'block' ? 'none' : 'block';
}

function addEmoji(emoji) {
    var chatInput = document.getElementById('chatInput');
    chatInput.value += emoji;
}

// Attach event listener to handle Enter key for sending messages
document.getElementById('chatInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Close emoji picker when clicking outside
document.addEventListener('click', function (e) {
    var emojiPicker = document.getElementById('emojiPicker');
    var emojiBtn = document.querySelector('.emoji-btn');
    if (!emojiPicker.contains(e.target) && !emojiBtn.contains(e.target)) {
        emojiPicker.style.display = 'none';
    }
});
