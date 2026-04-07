const express = require("express");
const cors = require("cors");
const multer = require("multer");
const mongoose = require("mongoose");
const Tesseract = require("tesseract.js");
const path = require("path");

const Document = require("./models/Document");

const app = express();

app.use(cors());
app.use(express.json());


// ================== MULTER SETUP ==================
const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    cb(null, Date.now() + "-" + file.originalname);
  },
});

const upload = multer({ storage });


// ================== DATA EXTRACTION ==================
const extractData = (text) => {
  const cleanText = text.replace(/\n/g, " ");

  const amount = cleanText.match(/(₹|Rs\.?|INR)\s?\d+/i);
  const date = cleanText.match(/\d{2}[\/\-\.]\d{2}[\/\-\.]\d{4}/);
  const name = cleanText.match(/Name[:\-]?\s*([A-Za-z\s]+)/i);

  return {
    amount: amount ? amount[0] : "Not found",
    date: date ? date[0] : "Not found",
    name: name ? name[1] : "Not found",
  };
};


// ================== ROUTES ==================

// Test route
app.get("/", (req, res) => {
  res.send("Backend running 🚀");
});

// Login (temporary)
app.post("/login", (req, res) => {
  const { email, password } = req.body;

  if (email === "test@gmail.com" && password === "1234") {
    return res.json({ message: "Login successful" });
  } else {
    return res.status(400).json({ message: "Invalid credentials" });
  }
});


// Upload file
app.post("/upload", upload.single("file"), (req, res) => {
  console.log("File saved:", req.file.path);

  res.json({
    message: "File uploaded",
    filePath: req.file.path,
  });
});


// Extract text + save to DB
app.post("/extract", async (req, res) => {
  const { filePath } = req.body;

  try {
    const fullPath = path.resolve(filePath);

    console.log("Reading file:", fullPath);

    const result = await Tesseract.recognize(fullPath, "eng");
    const text = result.data.text;

    console.log("OCR TEXT:\n", text);

    const extractedData = extractData(text);

    // Save to database
    const doc = new Document({
      userId: "user1",
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


// Get all documents (History)
app.get("/documents", async (req, res) => {
  try {
    const docs = await Document.find();
    res.json(docs);
  } catch (err) {
    res.status(500).json({ message: "Failed to fetch documents" });
  }
});


// ================== MONGODB CONNECTION ==================
mongoose.connect("YOUR_MONGODB_ATLAS_URL_HERE")
  .then(() => {
    console.log("MongoDB connected ✅");

    app.listen(5000, () => {
      console.log("Server running on port 5000");
    });
  })
  .catch((err) => {
    console.error("MongoDB connection failed ❌", err);
    process.exit(1);
  });