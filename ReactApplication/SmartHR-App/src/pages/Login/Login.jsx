import {Link,useNavigate} from "react-router-dom"
import { loginUser } from "../../services/AuthService"
import { useFormik } from "formik"
import * as yup from "yup"
// import { useContext, useState } from "react"
import { useState } from "react"
import { useContext } from "react"
import { AuthContext } from '../../context/AuthContext'

function Login(){

    const navigate=useNavigate()
    //use auth context
    const{login}=useContext(AuthContext)
    //state for alerts
    const[serverError,setServerError]=useState("")

    const formik=useFormik({
        initialValues:{
           
              email:"",
            password:""
        },
         validationSchema:yup.object({
                      
                email:yup.string()
                .email("inavlid Email")
                .required("email is required"),
        
                password:yup.string()
                .min(6,"minimum 6 characters")
                //.matches(/^(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{6,}$/, "Password must contain at least one uppercase letter and one special character")
                .required("Password is required")
                
        
            }),
             onSubmit: async(values)=>{
                    try{
                       const loggedInUser=await loginUser(
                        values.email,
                        values.password
                       )
                       //save user details in local storage
                    //    localStorage.setItem(
                    //     "user",JSON.stringify(loggedInUser)
                    //    )
                        login(loggedInUser)
                       //navigate("/dashboard")
                        navigate("/dashboard")
                    }
                    catch{
                        setServerError("Invalid userName or Password")
                    }
                }
               })

    return(
        <div className="container mt-5">
            <div className="w-50 mx-auto">
                <form onSubmit={formik.handleSubmit}>
                    
                    <div className="mb-3">
                        <label className="form-label" >Email address</label>
                        <input type="email" className="form-control" name="email" value={formik.values.email}
                            onChange={formik.handleChange} />

                        {
                            formik.touched.email &&
                            formik.errors.email &&
                            <div className="text-danger">{formik.errors.email}</div>
                        }

                    </div>
                    <div className="mb-3">
                        <label className="form-label" >Password</label>
                        <input type="password" className="form-control" name="password" value={formik.values.password}
                            onChange={formik.handleChange} />
                        {
                            formik.touched.password &&
                            formik.errors.password &&
                            <div className="text-danger">{formik.errors.password}</div>
                        }

                    </div>
                    {serverError &&
                        <div className="alert alert-danger">{serverError}</div>
                    }
                   
                    <button type="submit" className="btn btn-primary w -100">Login</button>
                </form>
                <p className="text-center mt-3">Dont Have an account?
                    <Link
                        to="/register" className="text-decoration-none">
                            {" "} Register Here
                    </Link>

                </p>

            </div>

        </div>

    )

    
}
export default Login