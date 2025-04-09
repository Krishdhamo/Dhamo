import React from "react";
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

const ProfileCard = ({Profilelist}) => {
    return (
        <div style={{
            border:"2px solid black",
            margin:"500px auto",
            width:"500px",
            height:"200px",
            fontSize:"20px",
            textAlign:"center",
            backgroundColor:"aqua",
            fontStyle:"italic",
            maxHeight:"300px",
            justifyContent:"center",
            alignItems:"center"
            }}>
            <div>
                <img style={{
                    width:"10%",
                    justifyContent:"center",
                    alignItems:"center"
                }}
                    
                 src={viteLogo}
                 />
            </div>
            <div>
                <span>name :</span>
                <span>{Profilelist.name}</span>
            </div>
            <div>
                <span>Department :</span>
                <span>{Profilelist.Department}</span>
            </div>
            <div>
                <span>year :</span>
                <span>{Profilelist.year}</span>
            </div>
            <div>
                <span>mobile :</span>
                <span>{Profilelist.mobile}</span>
            </div>
            <div>
                <span>address:</span>
                <span>{Profilelist.address}</span>
            </div>
        <a href="https://www.linkedin.com/in/dhamo-dharan-a6b0872a5/" target="_blank">
            LinkedIn profile</a>    
        </div>
    )
}
export default ProfileCard