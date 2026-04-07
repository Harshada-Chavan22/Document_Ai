import { useState, useEffect } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";
import { useNavigate } from "react-router-dom";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    const user = localStorage.getItem("user");
    if (!user) navigate("/");
  }, []);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const uploadRes = await axios.post(
        "http://localhost:5000/upload",
        formData
      );

      const filePath = uploadRes.data.filePath;

      const extractRes = await axios.post(
        "http://localhost:5000/extract",
        { filePath }
      );

      setText(extractRes.data.text);
      setData(extractRes.data.extractedData);

      setLoading(false);
      alert("Text extracted successfully ✅");

    } catch (err) {
      console.error(err);
      setLoading(false);
      alert("Error ❌");
    }
  };

  return (
    <div>
      <Navbar />

      <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
        <div className="bg-white p-8 rounded-xl shadow-md w-[400px] text-center">

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

          {loading && (
            <p className="text-blue-500 mt-2">Processing... ⏳</p>
          )}

          {data && (
            <div className="mt-4 text-left bg-gray-50 p-3 rounded">
              <p><strong>Name:</strong> {data.name}</p>
              <p><strong>Date:</strong> {data.date}</p>
              <p><strong>Amount:</strong> {data.amount}</p>
            </div>
          )}

          {text && (
            <div className="mt-4 text-left">
              <h3 className="font-semibold mb-1">Extracted Text:</h3>
              <p className="text-sm whitespace-pre-wrap">{text}</p>
            </div>
          )}

        </div>
      </div>
    </div>
  );
};

export default Upload;