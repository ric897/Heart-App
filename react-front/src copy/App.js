import './App.css';
import NurseGroup from './comps/nurse.group';
import React, { Component } from 'react';
import './index.css';
import SideBar from './comps/sidebar';
import NavBar from './comps/navbar';
import ExerciseGroup from './comps/exercise.group';

function App() {
  const [content, setContent] = React.useState(<NurseGroup />);

  function mainNurses(){
    console.log("main n");
    setContent(<NurseGroup />);
  }
  function mainExercises(){
    console.log("main e");
    setContent(<ExerciseGroup />);
  }

  function bob(){
    console.log("bob")
    setContent(<ExerciseGroup />);
  }



  
  return (


    <div className="App row">


      {/* <NavBar></NavBar> */}

      <div class="col-2" id="sticky-sidebar">
        <div class="sticky-top">
          <SideBar bob={()=>bob()} mainNurses={()=>mainNurses()} mainExercises={()=>mainExercises}/>
        </div >
      </div>
      <div class="col order-2" id="main">
        {content}
       
        {/* <ExerciseGroup /> */}
      </div>

    </div>



  );
}

export default App;
