import { useState } from "react";
import "./index.css";

function Booking() {
  const [form, setForm] = useState({
    name: "",
    phone: "",
    date: "",
    time: "",
    guests: ""
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const bookTable = async () => {
    setMessage("⏳ Booking...");

    try {
      const response = await fetch("http://127.0.0.1:8000/book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...form,
          guests: parseInt(form.guests)
        })
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(`✅ Booking Confirmed! Booking ID: ${data.id}`);
        setForm({ name: "", phone: "", date: "", time: "", guests: "" });
      } else {
        setMessage(`❌ ${data.detail}`);
      }
    } catch (err) {
      setMessage("❌ Backend not reachable");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1>🍽 Restaurant Table Booking</h1>
        <p className="subtitle">Reserve your table in seconds</p>

        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
        <input name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} />
        <input type="date" name="date" value={form.date} onChange={handleChange} />
        <input type="time" name="time" value={form.time} onChange={handleChange} />
        <input name="guests" placeholder="Guests" value={form.guests} onChange={handleChange} />

        <button onClick={bookTable}>Book Table</button>

        {message && <div className="message">{message}</div>}
      </div>
    </div>
  );
}

export default Booking;
