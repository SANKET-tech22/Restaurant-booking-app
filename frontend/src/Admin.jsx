import { useEffect, useState } from "react";
import "./index.css";

function Admin() {
  const [bookings, setBookings] = useState([]);

  const fetchBookings = async () => {
    const res = await fetch("http://127.0.0.1:8000/admin/bookings");
    const data = await res.json();
    setBookings(data);
  };

  const deleteBooking = async (id) => {
    if (!window.confirm("Are you sure you want to delete this booking?")) return;

    await fetch(`http://127.0.0.1:8000/admin/bookings/${id}`, {
      method: "DELETE"
    });

    fetchBookings();
  };

  useEffect(() => {
    fetchBookings();
  }, []);

  return (
    <div className="admin-page">
      <div className="admin-card">
        <h1>🧑‍💼 Admin Dashboard</h1>
        <p className="subtitle">Restaurant Booking Management</p>

        <button className="refresh-btn" onClick={fetchBookings}>
          🔄 Refresh Bookings
        </button>

        <div className="table-wrapper">
          <table className="admin-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Phone</th>
                <th>Date</th>
                <th>Time</th>
                <th>Guests</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {bookings.map((b) => (
                <tr key={b.id}>
                  <td>{b.id}</td>
                  <td>{b.name}</td>
                  <td>{b.phone}</td>
                  <td>{b.date}</td>
                  <td>{b.time}</td>
                  <td>{b.guests}</td>
                  <td>
                    <span className={`status ${b.status}`}>
                      {b.status}
                    </span>
                  </td>
                  <td>
                    <button className="delete-btn" onClick={() => deleteBooking(b.id)}>
                      🗑 Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Admin;
