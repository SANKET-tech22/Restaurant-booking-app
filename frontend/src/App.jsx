import { Routes, Route, Link } from "react-router-dom";
import Booking from "./Booking";
import Admin from "./Admin";

function App() {
  return (
    <div>
      <nav style={styles.nav}>
        <Link style={styles.link} to="/">Customer</Link>
        <Link style={styles.link} to="/admin">Admin</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Booking />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </div>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "center",
    gap: "30px",
    padding: "15px",
    background: "linear-gradient(135deg, #667eea, #764ba2)"
  },
  link: {
    color: "white",
    textDecoration: "none",
    fontWeight: "bold"
  }
};

export default App;
