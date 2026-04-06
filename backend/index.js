const express = require("express");
const cors = require("cors");
const multer = require("multer");
const app = express();
const Document = require("./models/Document");
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
app.get("/documents", async (req, res) => {
  const docs = await Document.find();
  res.json(docs);
});


const extractData = (text) => {
  const cleanText = text.replace(/\n/g, " ");

  // ✅ Amount (must include Rs or ₹)
  const amount = cleanText.match(/(₹|Rs\.?|INR)\s?\d+/i);

  // ✅ Date
  const date = cleanText.match(/\d{2}[\/\-\.]\d{2}[\/\-\.]\d{4}/);

  // ✅ Name
  const name =
    cleanText.match(/Name[:\-]?\s*([A-Za-z\s]+)/i);

  return {
    amount: amount ? amount[0] : "Not found",
    date: date ? date[0] : "Not found",
    name: name ? name[1] : "Not found",
  };
};

const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/documentAI")
  .then(() => console.log("MongoDB connected ✅"))
  .catch(err => console.log(err));

const Tesseract = require("tesseract.js");

const path = require("path");

app.post("/extract", async (req, res) => {
  const { filePath } = req.body;

  try {
    const result = await Tesseract.recognize(filePath, "eng");
    const text = result.data.text;

    const extractedData = extractData(text);

    // ✅ Save to DB
    const doc = new Document({
      userId: "user1", // later from login
      filePath,
      extractedData,
    });

    await doc.save();

    res.json({
      text,
      extractedData,
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Extraction failed" });
  }
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});