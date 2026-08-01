const BASE_URL = "http://localhost:3000/employees"

//Get all Employees
export async function getEmployees(){
  const response= await fetch(BASE_URL)
  return await response.json();
}

//Delete Employee
export async function deleteEmployee(id) {
    const response = await fetch(`${BASE_URL}/${id}`,{
        method:"DELETE"
        
        })
    
}