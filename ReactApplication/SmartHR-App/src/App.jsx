
import { useState } from 'react'
import './App.css'
import Header from './components/common/Header/Header'
import Footer from './components/common/Footer/Footer'
import Home from './pages/Home/Home'
import About from './pages/About/About'
import Contact from './pages/Contact/Contact'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Employees from './pages/Employees/Employees'
import Register from './pages/Register/Register'
import Login from './pages/Login/Login'
import ProtectedRoute from './components/common/ProtectedRoute/ProtectedRoute'

function APP() {
  return (
    // <>
    <Router>
      <div className='app'>
        <Header />
        <main className='main-content'>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/register" element={<Register />} />
            <Route path="/dashboard" element={
              <ProtectedRoute>
                <Employees />  
              </ProtectedRoute>
            }
            />
            <Route path="/login" element={<Login />} />
          </Routes>
        
        </main>
        <Footer />
      </div>
      
    </Router>




    // </>


  )
}
export default APP











