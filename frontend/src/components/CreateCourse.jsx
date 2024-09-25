import { useState, useEffect } from 'react'

function CreateCourse() {

    return (
        <div>
            <form>
                <label for="course_name">Course name</label>
                <input type="text" id="course_name"></input>
                <label for="course_location">Location</label>
                <input type="text" id="course_location"></input>
                <br></br>
                <label for="course_holes">Holes</label>
                <input type="radio" id="9" name="course_holes"></input>
                <label for="9">9</label>
                <input type="radio" id='18' name="course_holes"></input>
                <label for="18">18</label>
                <br></br>
                <label for="course_par">Par</label>
                <input type="text" id="course_par"></input>
            </form>
        </div>
    )
}

export default CreateCourse