import { useState } from "react"
import { registerUser } from "../../services/AuthService";
import { useNavigate } from "react-router-dom";
import {useFormik} from "formik"
import * as yup from "yup"
function Register(){
    //state for navigation
   const navigate=useNavigate()
   //state to store user data
   const formik=useFormik({
    initialValues:{
           name: "",
          email:"",
        password:""
    },
    validationSchema:yup.object({
        name:yup.string()
        .required("Name is mandatory"),

        email:yup.string()
        .email("inavlid Email")
        .required("email is required"),

        password:yup.string()
        .min(6,"minimum 6 characters")
        .matches(/^(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{6,}$/, "Password must contain at least one uppercase letter and one special character")
        .required("Password is required")
        

    }),
    onSubmit: async(values,{resetForm})=>{
        try{
           await registerUser(values)
           setMessage("Registration Success")
           resetForm();
           navigate("/login")
        }
        catch{
            setError("Registration Failed")
        }
    }
   })
//    const[user,setUser]=useState({
//     name:"",
//     email:"",
//     password:""

//    });

   //state for success msg
   const[message,setMessage]=useState("")
   //state for error msg
    const [error, setError] = useState("")
   

//    function handleChange(event)
//    {
//     const {name,value}=event.target
//     setUser({
//         ...user,[name]:value
//     })

    //find which textbox changed
    // let fieldName=event.target.name

    // //get the value enetred by user
    // let fieldValue=event.target.value

    // //if the name textbox is changed
    // if(fieldName==="name"){
    //     setUser({
    //         name:fieldValue,
    //         email:user.email,
    //         password:user.password
    //     })
    // }
    // //if the email textbox changed
    //    if (fieldName === "email") {
    //        setUser({
    //            name: user.name,
    //            email: fieldValue,
    //            password: user.password
    //        })
    //    }
    //    if (fieldName === "password") {
    //        setUser({
    //            name: user.name,
    //            email: user.email,
    //            password: fieldValue
    //        })
    //    }

//    async function handleSubmit(event){
//         event.preventDefault()
//         setMessage("")
//         setError("")
//         //validation
//         if(
//             user.name===""||user.email===""||user.password===""
//         ){
//             setError("All fields are compulsory")
//         }
//         try{
//             await registerUser(user)
//             setMessage("Registration sucesss")
//             //clear form
//             setUser({
//                 name:"",
//                 email:"",
//                 password:""
//             });
//             //navigate to login page
//             navigate("/login")

//         }
//         catch{
//             setError("unable to register")
//         }

//    }
    return (

        <div className="container mt-5">
            <div className="w-50 mx-auto">
                <form onSubmit={formik.handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label" >FullName</label>
                        <input type="text" className="form-control" name="name" 
                        value={formik.values.name} 
                        onChange={formik.handleChange}/>
                        {
                            formik.touched.name &&
                            formik.errors.name &&
                            <div className="text-danger">{formik.errors.name}</div>
                        }

                    </div>
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
                    {error && 
                        <div className="alert alert-danger">{error}</div>
                    }
                    {message &&
                        <div className="alert alert-sucess">{message}</div>
                    }
                    <button type="submit" className="btn btn-primary w -100">Register</button>
                </form>
                    <p className="text-center mt-3">Already Have an account?

                    </p>
               
            </div>

        </div>

        

    )
}
export default Register