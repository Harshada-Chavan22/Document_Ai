console.log("History page loaded");
import { useEffect, useState } from "react";
import axios from "axios";

const History = () => {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5000/documents")
      .then((res) => {
        console.log("DATA:", res.data); // ✅ debug
        setDocs(res.data);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h2 className="text-2xl font-bold mb-4 text-center">
        Document History 📊
      </h2>

      {/* ✅ FIX: check length properly */}
      {docs.length === 0 ? (
        <p className="text-center text-gray-500">No documents found</p>
      ) : (
        <div className="grid gap-4 max-w-xl mx-auto">
          {docs.map((doc) => (
            <div
              key={doc._id}
              className="bg-white p-4 shadow rounded-lg"
            >
              <p><strong>Name:</strong> {doc.extractedData?.name}</p>
              <p><strong>Date:</strong> {doc.extractedData?.date}</p>
              <p><strong>Amount:</strong> {doc.extractedData?.amount}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default History;