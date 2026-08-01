import { useContext } from 'react'
import './Header.css'
import { Link,useNavigate } from 'react-router-dom'
import { AuthContext } from '../../../context/AuthContext'
function Header(){
    const navigate=useNavigate()
    //const user=JSON.parse(localStorage.getItem("user"))
    const {user,logout}=useContext(AuthContext)

    function handleLogout(){
        logout()
        navigate("/login")
    }
    return (
        
        <header>
            <h1>SmartHR-App</h1>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                    <li><Link to="/dashboard">Employees</Link></li>

                    {!user &&(
                    <>
                            <li><Link to="/register">Register</Link></li>
                            <li><Link to="/login">Login</Link></li>
                    </>
                    
                    )}
                    {user && (
                        <>
                            <li>
                                <button onClick={handleLogout}>
                                    Logout
                                </button>
                            </li>
                            
                        </>

                    )}

                </ul>
            </nav>
        </header>
    
    )
}

export default Header