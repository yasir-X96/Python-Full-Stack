import EmployeeCard from '../../components/common/Employee/EmployeeCard'
//import employees from '../../data/employees'
import { deleteEmployee, getEmployees } from '../../services/EmployeeService'
import "./Employees.css"
import { useState,useEffect } from 'react'
function  Employees ()
{
    //create state
    //const[employeeList,setEmployeeList]=useState(employees)
    const [employees, setEmployees] = useState([])
    //read from the LocalStorage
    const userString=localStorage.getItem("user")
    const user=JSON.parse(userString)
    const[userName,domain]=user.email.split("@")
    const maskedEmail=
    userName.charAt(0)+"x".repeat(userName.length-1)+"@"+domain

    // function removeEmployee(){
    //     if(employeeList.length===0){
    //         alert("No employee available")
    //         return;
    //     }
       //UseEffect--providing empty array says--effect runs only once after first render
    useEffect(()=>{
        loadEmployees()
    },[])

    async function loadEmployees(){
        const data=await getEmployees()
        setEmployees(data)

    }
    //last employee
   // setEmployeeList(employeeList.slice(0,-1))}
//    function removeEmployee(id){
//     const updatedEmployees=employeeList.filter((employee)=>employee.id!=id)
//     setEmployeeList(updatedEmployees)
//    }

//remove employee
    async function removeEmployee(id){
        await deleteEmployee(id)
        loadEmployees()
    }
    return (

        <div className="employees">
            <div className='d-flex justify-content-end'>
                <h5>{maskedEmail}</h5>
            </div>
            
            <h2>Employee List</h2>
            {/* <div>
                <button onClick={removeEmployee}>
                    RemoveEmployee
                </button>
            </div> */}
            {/* <h3>Total Employees::{employeeList.length}</h3> */}
            <h3>Total Employees::{employees.length}</h3>
            <div className='employee-container'>
                {
                    // employeeList.map((employee)=>
                    // employeeList.map((employee) =>
                    employees.map((employee) =>
                    <EmployeeCard
                        key={employee.id}
                        name={employee.name}
                        designation={employee.designation}
                        image={employee.image}
                        removeEmployee={removeEmployee}
                        id={employee.id}
                     />
                    )
                }

            </div>
        </div>
        
       

    )
}
export default Employees