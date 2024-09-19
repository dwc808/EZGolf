import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  
   

  return (
    <>
      <p>Heyllo!</p>
      <input type="text" id="course_name" value={course_name}></input>
      <input type="text" id="course_location" value={course_location}></input>
      <input type="text" id="course_holes" value={course_holes}></input>
      <input type="text" id="course_par" value={course_par}></input>
      <input type="submit" value = "create_course"></input>
    </>
  )
}

export default App
