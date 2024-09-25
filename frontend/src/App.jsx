import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CourseHistory from './components/CourseHistory'
import CreateCourse from './components/CreateCourse'

function App() {

  return (
    <div>
      <CourseHistory />
      <CreateCourse />
    </div>
  );
};

export default App
