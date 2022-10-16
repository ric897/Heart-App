import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { Card } from "react-bootstrap";
import '../css/styles.css';
import './functions.js';
import phoneFormat, { timeDifference } from "./functions.js";



export default function PatientRow(props) {
    const [id, setId] = React.useState(props.id);
    const [name, setName] = React.useState(props.name);
    const [phone, setPhone] = React.useState(props.phone);
    const [email, setEmail] = React.useState(props.email);

    React.useEffect(() => {

    }, [id])

    return (<>
        <tr>
            <td className="px-4 py-3">{name}</td>
            <td className="px-4 py-3">{id}</td>
            <td className="px-4 py-3">{phoneFormat(phone)}</td>
            <td className="px-4 py-3">{email}</td>
            <td className="w-10 text-center">
                <a href="#" className="no-link py-0" onClick={() => { console.log(id); props.removePatient(id) }}>&#10006;</a>
            </td>
        </tr>
    </>)

}