import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { Card } from "react-bootstrap";
import '../css/styles.css';
import './functions.js';
import phoneFormat from "./functions.js";
import PatientRow from "./patient.row";



export default function NurseTable(props) {

    const [id, setId] = React.useState(props.id);
    const [name, setName] = React.useState(props.name);
    const [phone, setPhone] = React.useState(props.phone);
    const [patients, setPatients] = React.useState(props.patients);
    const bg = `bg-[url('https://i.pravatar.cc/${Math.floor(Math.random() * 100) + 1}}')]`
        // [
        //     {
        //         name: "John Doe",
        //         id: "83232332",
        //         phone: "4169882106",
        //         email: "john@gmail.com",
        //         time:"1665740740"
        //     },
        //     {
        //         name: "bob Doe",
        //         id: "43232232",
        //         phone: "4169882106",
        //         email: "bob@gmail.com",
        //         time:"1665730740"
        //     },
        //     {
        //         name: "mark Doe",
        //         id: "23234232",
        //         phone: "4169882106",
        //         email: "mark@gmail.com",
        //         time:"1625740140"
        //     },
        // ]
    // );
    const [email, setEmail] = React.useState(props.email);
    // setPatients();




    // for (const p of patients) {
    //     patientsDisplay.push(
    //         <>
    //             {/* <PatientItem name={p.name} id={p.id} phone={p.phone} /> */}
    //             <div>hi</div>
    //         </>
    //     )
    // }

    function removePatient(userID) {
        setPatients(patients.filter((patient) => {
            return userID !== patient.id;
        }));
        //Post request to remove user from nurse
    }


    React.useEffect(() => {

    }, [id])

    return (<>
        <div className='flex items-center justify-center my-3 w-full'>
            <div className="rounded-xl border p-2 shadow-md w-11/12 bg-white">
                <div className="flex  items-center justify-between border-b pb-3 m-3">
                    <div className="flex items-center space-x-3">
                        <div className="ml-1 text-lg font-bold text-slate-700">{name}</div>
                    </div>
                    <div className="flex items-center space-x-8">
                        <button className="rounded-2xl border bg-neutral-100 px-3 py-1 text-xs font-semibold">Nurse</button>
                        <div className="text-xs text-neutral-500">{patients.length} patients</div>
                    </div>
                </div>
                <section className="w-full text-gray-600 body-font">
                    <div className="container px-1 py-1 mx-auto">
                        <div className="lg:w-full w-full mx-auto overflow-auto">
                            <table className="table-auto w-full text-left whitespace-no-wrap">
                                <thead>
                                    <tr>
                                        <th className="px-3 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tl rounded-bl">Patient</th>
                                        <th className="px-3 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">id</th>
                                        <th className="px-3 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">number</th>
                                        <th className="px-3 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">rehab started</th>
                                        <th className="px-3 w-10 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tr rounded-br"><div className="mx-2"></div></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {patients.map((p) => {
                                        return <PatientRow key={p.id} email={p.email} rehabStarted={p.rehabStarted} name={p.name} id={p.id} phone={p.phone} removePatient={(userID) => { removePatient(userID) }} patient={p} />
                                    })}

                                </tbody>
                            </table>
                        </div>
                        <div className="flex pl-4 mt-4 lg:w-full w-full mx-auto">
                            
                            {/* <button className="flex ml-auto text-white bg-red-600 border-0 py-2 px-6 focus:outline-none hover:bg-red-700 rounded">Add Patient</button> */}
                        </div>
                    </div>
                </section>

            </div>
        </div>

    </>)

}