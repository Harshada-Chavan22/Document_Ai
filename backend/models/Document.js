
const mongoose = require("mongoose");

const documentSchema = new mongoose.Schema({
  userId: String,
  filePath: String,
  extractedData: Object,
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model("Document", documentSchema);