import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("user");
    navigate("/");
  };

  return (
    <div className="bg-white shadow p-4 flex justify-between">
      <h1 className="font-bold text-lg">Document AI</h1>

      <div className="flex gap-3">
        <button onClick={() => navigate("/dashboard")} className="text-blue-500">
          Dashboard
        </button>

        <button onClick={() => navigate("/history")} className="text-purple-500">
          History
        </button>

        <button onClick={handleLogout} className="text-red-500">
          Logout
        </button>
      </div>
    </div>
  );
};

export default Navbar;