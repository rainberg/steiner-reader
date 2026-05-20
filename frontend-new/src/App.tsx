import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import BookDetail from './pages/BookDetail';
import Reader from './pages/Reader';
import Login from './pages/Login';
import Profile from './pages/Profile';
import Recharge from './pages/Recharge';
import Admin from './pages/Admin';
import Upload from './pages/Upload';

function App() {
  return (
    <Router basename="/v2">
      <div className="min-h-screen bg-[#f8f5f0]">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<Home />} />
          <Route path="/books/:bookId" element={<BookDetail />} />
          <Route path="/books/:bookId/lectures/:lectureId" element={<Reader />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/recharge" element={<Recharge />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/upload" element={<Upload />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
