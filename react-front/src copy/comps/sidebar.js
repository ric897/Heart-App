import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { Card } from "react-bootstrap";
import '../css/styles.css';

export default function SideBar(props) {
    return (<>
        <div class="w-60 h-full shadow-md bg-white absolute" id="sidenavSecExample">
            <div class="pt-4 pb-2 px-6">
                <a className="no-link" href="#!">
                    <div class="flex items-center">
                        <div class="shrink-0">
                            <img src="icons/user.png" class="rounded-full w-10" alt="Avatar" />
                        </div>
                        <div class="grow ml-3">
                            <p class="text-sm font-semibold text-red-600 ">St. George Memorial</p>
                        </div>
                    </div>
                </a>
            </div>
            <ul class="relative px-1">
                <li class="relative">
                    <a onClick={()=>{props.bob(); console.log("hello")}} class="no-link flex items-center text-sm py-4 px-6 h-12 overflow-hidden text-gray-700 text-ellipsis whitespace-nowrap rounded hover:text-blue-600 hover:bg-blue-50 transition duration-300 ease-in-out" href="#!" data-mdb-ripple="true" data-mdb-ripple-color="primary">
                        
                        <span>Exercises</span>
                    </a>
                </li>
                <li class="relative">
                    <a onClick={()=>{props.mainNurses()}} class="no-link flex items-center text-sm py-4 px-6 h-12 overflow-hidden text-gray-700 text-ellipsis whitespace-nowrap rounded hover:text-blue-600 hover:bg-blue-50 transition duration-300 ease-in-out" href="#!" data-mdb-ripple="true" data-mdb-ripple-color="primary">
                        
                        <span>Nurses</span>
                    </a>
                </li>
                
                
            </ul>
            
            <div class="text-center bottom-0 absolute w-full">
                <hr class="m-0" />
                <p class="py-2 text-sm text-gray-700">tailwind-elements.com</p>
            </div>
        </div>
    </>);
}