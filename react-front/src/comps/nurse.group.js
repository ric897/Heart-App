import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { Card } from "react-bootstrap";
import '../css/styles.css';
import './functions.js';
import phoneFormat from "./functions.js";
import NurseTable from "./nurse.table";





export default class NurseGroup extends React.Component {

    // let [nurses, setNurses] = React.useState([]);
    // let [loaded, setLoaded] = React.useState(false);
    // let [content, setContent] = React.useState(<></>)

    constructor(props){
        super(props);
        this.state={
            nurses:[],
            loaded:false,
            content:<></>,
        }
    }

    componentDidMount(){
        fetch("https://heartshield.io/api/nested/?format=json").then(response => response.json())
        .then(json => {
            // console.log('parsed json', json['0']) // access json.body here
            
            this.setState({nurses:Object.values(json)});
            console.log(this.state.nurses);
            const reArr = [];
            for (const nurse of this.state.nurses) {
                reArr.push(<NurseTable className="w-full" name={nurse.first_name} id={nurse.id} email={nurse.email} patients={nurse.patients} />)
            }
            this.setState({content:reArr});
        })
    }
    





    
    
    render(){
        return <>{ this.state.content }</>;
    }
}