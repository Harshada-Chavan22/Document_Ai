import { useEffect, useState } from "react";
import axios from "axios";

const History = () => {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/documents")
      .then(res => setDocs(res.data));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Document History 📊</h2>

      {docs.map((doc, index) => (
        <div key={index} className="bg-white p-4 mb-3 shadow rounded">
          <p><strong>Name:</strong> {doc.extractedData.name}</p>
          <p><strong>Date:</strong> {doc.extractedData.date}</p>
          <p><strong>Amount:</strong> {doc.extractedData.amount}</p>
        </div>
      ))}
    </div>
  );
};

export default History;