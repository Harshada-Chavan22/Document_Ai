import { useState } from "react";
import axios from "axios";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [data, setData] = useState({});

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      // ✅ Step 1: Upload file
      const uploadRes = await axios.post(
        "http://localhost:5000/upload",
        formData
      );

      const filePath = uploadRes.data.filePath;

      // ✅ Step 2: Extract text + structured data
      const extractRes = await axios.post(
        "http://localhost:5000/extract",
        { filePath }
      );

      console.log("RAW TEXT:", extractRes.data.text);
      console.log("EXTRACTED DATA:", extractRes.data.extractedData);

      // ✅ Store results
      setText(extractRes.data.text);
      setData(extractRes.data.extractedData);

      alert("Text extracted successfully ✅");

    } catch (err) {
      console.error(err);
      alert("Error ❌");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-md w-[400px] text-center">
        
        <h2 className="text-xl font-bold mb-4">Upload Document 📄</h2>

        {/* File Input */}
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4"
        />

        {/* Upload Button */}
        <button
          onClick={handleUpload}
          className="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600"
        >
          Upload
        </button>

        {/* Extracted Structured Data */}
        {data && (
          <div className="mt-4 text-left bg-gray-50 p-3 rounded">
            <p><strong>Name:</strong> {data.name}</p>
            <p><strong>Date:</strong> {data.date}</p>
            <p><strong>Amount:</strong> {data.amount}</p>
          </div>
        )}

        {/* Raw OCR Text */}
        {text && (
          <div className="mt-4 text-left">
            <h3 className="font-semibold mb-1">Extracted Text:</h3>
            <p className="text-sm whitespace-pre-wrap">{text}</p>
          </div>
        )}

      </div>
    </div>
  );
};

export default Upload;