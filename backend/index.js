const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Backend running 🚀");
});

// LOGIN API (temporary)
app.post("/login", (req, res) => {
  const { email, password } = req.body;

  if (email === "test@gmail.com" && password === "1234") {
    return res.json({ message: "Login successful" });
  } else {
    return res.status(400).json({ message: "Invalid credentials" });
  }
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});