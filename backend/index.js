const express = require("express");
const cors = require("cors");
const multer = require("multer");
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

const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    cb(null, Date.now() + "-" + file.originalname);
  },
});

const upload = multer({ storage });

app.post("/upload", upload.single("file"), async (req, res) => {
  const filePath = req.file.path;

  res.json({
    message: "File uploaded",
    filePath: filePath,
  });
});

const Tesseract = require("tesseract.js");

app.post("/extract", async (req, res) => {
  const { filePath } = req.body;

  try {
    const result = await Tesseract.recognize(filePath, "eng");

    res.json({
      text: result.data.text,
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Extraction failed" });
  }
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});