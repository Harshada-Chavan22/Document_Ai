
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();

  return (
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
  );
};

export default Dashboard;