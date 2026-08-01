import "./EmployeeCard.css"
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
function EmployeeCard(props){
    return(

        <Card sx={{ maxWidth: 345,margin:3, border:"solid", backgroundColor:"bisque"}}>
            <CardMedia
                component="img"
                // alt="green iguana"
                height="140"
                image={props.image}
                alt={props.name}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {props.name}
                </Typography>
                <Typography variant="body2" sx={{ color: 'text.secondary' }}>
                    <strong>Designation::</strong>{props.designation}
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small" onClick={() => props.removeEmployee(props.id)}>Remove</Button>
                <Button size="small">Update</Button>
            </CardActions>
        </Card>
        // <div className="card">
        //     <h3>{props.name}</h3>
        //     <p>
        //     <strong>Designation::</strong>{props.designation}
        //     </p>
        //     <button onClick={()=>props.removeEmployee(props.id)}>Delete</button>
        // </div>
    
    )
}

export default EmployeeCard
