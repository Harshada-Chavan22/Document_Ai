import { useState } from "react";
import axios from "axios";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      // Step 1: Upload file
      const uploadRes = await axios.post(
        "http://localhost:5000/upload",
        formData
      );

      const filePath = uploadRes.data.filePath;

      // Step 2: Extract text
      const extractRes = await axios.post(
        "http://localhost:5000/extract",
        { filePath }
      );

      console.log(extractRes.data.text);

      // ✅ FIX: set text here
      setText(extractRes.data.text);

      alert("Text extracted successfully ✅");

    } catch (err) {
      console.error(err);
      alert("Error ❌");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-md w-96 text-center">
        <h2 className="text-xl font-bold mb-4">Upload Document 📄</h2>

        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4"
        />

        <button
          onClick={handleUpload}
          className="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600"
        >
          Upload
        </button>

        {/* ✅ Show extracted text */}
        {text && (
          <p className="mt-4 text-sm text-left whitespace-pre-wrap">
            {text}
          </p>
        )}
      </div>
    </div>
  );
};

export default Upload;