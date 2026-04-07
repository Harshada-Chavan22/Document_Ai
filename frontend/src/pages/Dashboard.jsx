import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import Navbar from "../components/Navbar";

const Dashboard = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const user = localStorage.getItem("user");
    if (!user) navigate("/");
  }, []);

  return (
    <div>
      <Navbar />

      <div className="min-h-screen flex flex-col items-center justify-center gap-4">
        <h1 className="text-3xl font-bold">Welcome to Dashboard 🚀</h1>

        <button
          onClick={() => navigate("/upload")}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Upload Document
        </button>

        <button
          onClick={() => navigate("/history")}
          className="bg-purple-500 text-white px-4 py-2 rounded"
        >
          View History
        </button>
      </div>
    </div>
  );
};

export default Dashboard;