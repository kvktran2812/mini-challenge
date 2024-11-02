import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [userMessage, setUserMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  // Function to send message to Flask backend
  const sendMessage = async () => {
    if (!userMessage.trim()) return;

    const messageEntry = { sender: "user", message: userMessage };
    setChatHistory([...chatHistory, messageEntry]);

    try {
      const response = await axios.post("http://127.0.0.1:5000/chat", {
        message: userMessage,
      });

      const botMessage = response.data.response;
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", message: botMessage },
      ]);
    } catch (error) {
      console.error("Error sending message to the server:", error);
    }

    setUserMessage("");
  };

  return (
    <div style={{ width: "300px", margin: "50px auto", textAlign: "center" }}>
      <h1>Chatbot</h1>
      <div style={{ border: "1px solid #ddd", padding: "10px", minHeight: "200px" }}>
        {chatHistory.map((entry, index) => (
          <div
            key={index}
            style={{
              textAlign: entry.sender === "user" ? "right" : "left",
              margin: "5px 0"
            }}
          >
            <strong>{entry.sender}:</strong> {entry.message}
          </div>
        ))}
      </div>
      <input
        type="text"
        placeholder="Type your message..."
        value={userMessage}
        onChange={(e) => setUserMessage(e.target.value)}
        onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        style={{ width: "100%", padding: "10px", marginTop: "10px" }}
      />
      <button onClick={sendMessage} style={{ width: "100%", padding: "10px" }}>
        Send
      </button>
    </div>
  );
}

export default App;
