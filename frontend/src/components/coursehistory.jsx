import { useState, useEffect } from 'react'

function CourseHistory() {

    //styling, for now at least
    const styles = {
        'background-color': 'orange',
        'border-radius': '20px',
        color: 'white',
        padding: '10px',
        margin: '10px',
    };

    const [courseData, setCourseData] = useState(0);
  
    useEffect(() => {
      fetch('/api/courses/user').then(res => res.json()).then(data => {
        setCourseData(data);
      });
    }, []);
  
    

    return (
      <div>
        {courseData ? (
          <div>
            {Object.entries(courseData).map(([key, course]) => (
              <div key={key} style = {styles}>
                <h2>{course.course_name}</h2>
                <p><strong>Location:</strong> {course.course_location}</p>
                <p><strong>Par:</strong> {course.course_par}</p>
                <p><strong>PR:</strong> {course.course_pr}</p>
              </div>
            ))}
          </div>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    );
  };

  export default CourseHistory 