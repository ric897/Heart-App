import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { Card } from "react-bootstrap";
import '../css/styles.css';
import './functions.js';



export default function ExerciseItem(props) {



    // function remove(userID) {
    //     setPatients(patients.filter((patient) => {
    //         return userID !== patient.id;
    //     }));
    //     //Post request to remove user from nurse
    // }


    React.useEffect(() => {

    })

    return (<>
        <div className='flex items-center justify-center my-3 w-full'>
            <div className="rounded-xl border p-2 shadow-md w-11/12 bg-white">
                <div className="flex  items-center justify-between border-b pb-3 m-3">
                    <div className="flex items-center space-x-3">
                        <div className="h-8 w-8 rounded-full bg-slate-400 bg-[url('https://i.pravatar.cc/32')]"></div>
                        <div className="text-lg font-bold text-slate-700">{props.name}</div>
                    </div>
                    <div className="flex items-center space-x-8">
                        <button className="rounded-2xl border bg-neutral-100 px-3 py-1 text-xs font-semibold">exercise</button>
                        <div className="text-xs text-neutral-500">{props.minutes} minutes</div>
                        <button className="flex ml-auto   px-6 focus:outline-none ">&#10006;</button>
                    </div>
                </div>
                <section className="w-full text-gray-600 body-font">
                    <div className="container px-1 py-1 mx-auto">
                        <div className="lg:w-full w-full mx-auto overflow-auto p-2 px-4">
                            <p className="row table-auto w-full text-left whitespace-no-wrap">
                                {props.body}
                            </p>
                            <div className="w-full justify-content-center pl-5">
                                    <iframe src="https://www.youtube.com/watch?v=JCg2UDQQPLI" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
                            </div>

                        </div>
                        <div className="flex pl-4 mt-4 lg:w-full w-full mx-auto">
                            <button className="flex ml-auto   px-6 focus:outline-none ">&#10006;</button>
                        </div>
                    </div>
                </section>

            </div>
        </div>

    </>)

}