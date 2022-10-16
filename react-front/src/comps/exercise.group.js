import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { Card } from "react-bootstrap";
import '../css/styles.css';
import './functions.js';
import phoneFormat from "./functions.js";
import NurseTable from "./nurse.table";
import ExerciseItem from "./exercise.item";





export default class ExerciseGroup extends React.Component {

    constructor(props){
        super(props);
        this.state={
            nurses:[],
            loaded:false,
            content:<></>,
        }
    }

    componentDidMount(){
        fetch("https://heartshield.io/api/trainings/?format=json").then(response => response.json())
        .then(json => {
            // console.log('parsed json', json['0']) // access json.body here
            
            this.setState({nurses:Object.values(json)});
            console.log(this.state.nurses);
            const reArr = [];
            for (const nurse of this.state.nurses) {
                reArr.push(<ExerciseItem className="w-full" name={nurse.title} video={nurse.url} body={nurse.description} />)
            }
            this.setState({content:reArr});
        })
    }
    render(){
        return <>{ this.state.content }</>;
    }
}