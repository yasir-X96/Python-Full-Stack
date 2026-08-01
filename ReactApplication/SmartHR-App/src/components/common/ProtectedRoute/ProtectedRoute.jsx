import { Navigate } from "react-router-dom"

function ProtectedRoute({children}){
    //fetch logged in user
    const user=localStorage.getItem("user")
    if(!user){
        //user is not logged in---navigate to Login page
        return <Navigate to="/login" replace/>
    }
    //when user is logged in
    return children
}
export default ProtectedRoute