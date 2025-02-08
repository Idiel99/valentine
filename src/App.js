import React, { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");

  const moveNoButton = (e) => {
    e.target.style.position = "absolute";
    e.target.style.top = `${Math.random() * 80}vh`;
    e.target.style.left = `${Math.random() * 80}vw`;
  };

  return (
    <div className="container">
      <h1>Will you be my Valentine? 💖</h1>
      {message ? (
        <h2 className="message">{message}</h2>
      ) : (
        <div className="button-container">
          <button className="yes-button" onClick={() => setMessage("Yay! 💕 Can't wait!")}>
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
