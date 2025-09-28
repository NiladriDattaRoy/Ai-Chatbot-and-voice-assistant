// script.js

document.addEventListener("DOMContentLoaded", () => {
    const chatContainer = document.querySelector(".chat-container");
    const chatBox = document.querySelector(".chat-box");

    function adjustChatAlignment() {
        const screenWidth = window.innerWidth;

        if (screenWidth < 768) {
            // 📱 Mobile view - take full width
            chatContainer.style.width = "95%";
            chatContainer.style.height = "90vh";
            chatContainer.style.margin = "10px auto";
        } else if (screenWidth < 1200) {
            // 💻 Tablet / Small desktop
            chatContainer.style.width = "80%";
            chatContainer.style.height = "85vh";
            chatContainer.style.margin = "20px auto";
        } else {
            // 🖥️ Large desktop
            chatContainer.style.width = "1200px"; // fixed width for big screens
            chatContainer.style.height = "750px";
            chatContainer.style.margin = "auto";
        }
    }

    // Auto-scroll chat to bottom (like Telegram)
    function autoScrollChat() {
        if (chatBox) {
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    // Run on page load
    adjustChatAlignment();
    autoScrollChat();

    // Run on window resize
    window.addEventListener("resize", adjustChatAlignment);

    // Observe chat messages and auto-scroll when new ones are added
    if (chatBox) {
        const observer = new MutationObserver(() => {
            autoScrollChat();
        });

        observer.observe(chatBox, { childList: true });
    }
});
