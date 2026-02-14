import React, { useState } from "react";
import "./App.css";
import loveLetters from "./assets/loveLetters";

function App() {
  const [message, setMessage] = useState(null);

  const moveNoButton = (e) => {
    e.target.style.position = "absolute";
    e.target.style.top = `${Math.random() * 80}vh`;
    e.target.style.left = `${Math.random() * 80}vw`;
  };

  const handleYesClick = () => {
    const randomIndex = Math.floor(Math.random() * loveLetters.length);
    setMessage(loveLetters[randomIndex]);
  };

  return (
    <div className="container">
      <h1>Will you be my Valentine? 💖</h1>
      {message ? (
        <div className="message-container">
          <div
            className="message"
            dangerouslySetInnerHTML={{ __html: message.content }}
          />
        </div>
      ) : (
        <div className="button-container">
          <button className="yes-button" onClick={handleYesClick}>
            Yes
          </button>
          <button className="no-button" onMouseOver={moveNoButton} onTouchStart={moveNoButton}>
            No
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
