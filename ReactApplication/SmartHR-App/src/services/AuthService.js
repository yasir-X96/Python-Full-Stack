import axios from "axios";

const API_URL = "http://localhost:3000/users"

export async function registerUser(user){
    // const response= await fetch(API_URL,{
    //     method:"POST",
    //     headers:{
    //         "Content-Type":"application/json"
    //     },
    //     body:JSON.stringify(user)
    // })
    // if(!response.ok){
    //     throw new Error("Registration Failed")
    // }
    // return await response.json()
    try{
    const response=await axios.post(API_URL,user)
    return await response.data
    }
    catch(error){
        throw new Error("Registration Failed")

    }
}

//login user
export async function loginUser(email,password){
    console.log("Email enetred:",email);
    
    //const response=await fetch(`${API_URL}?email=${email}`)
    const response = await axios.get(`${API_URL}?email=${email}`)
    // if(!response.ok){
    //     throw new Error("Internal Server Error")
    // }
    // const matchingUsers=await response.json()
    const matchingUsers=response.data
    if(matchingUsers.length===0){
        throw new Error("userName or password is wrong")
    }

    const foundUser=matchingUsers[0]
    console.log("StoredUser: ",foundUser.password);
    console.log("StoredUser: ", password);
    if(foundUser.password!==password){
        throw new Error("userName or password is wrong")
    }
    return foundUser


}