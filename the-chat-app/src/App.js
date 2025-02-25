import './App.css';
import React, {useState} from "react";

function App() {

  const [userName, setUserName] = useState("")
  const [roomName, setRoomName] = useState("")

  const [ correctUserName, setCorrectUserName] = useState("")
  const [correctPassword, setcorrectPassword] = useState("")
  return (
    // <div className='container'>
    //   <h1>Welcome to chat application</h1>
    //   <input placeholder="Enter Email id" type="email"/>
    //   <input placeholder="Enter Password" type="password"/>
    //   <br/>
    //   <button>Login</button>
    //   <button>Register</button>
    // </div>
<div className="card">
  <div className="card-header">
    Welcome to chat application
  </div>
  <div className="card-body">
      <input id="inputGroup-sizing-lg" className="form-control" placeholder="Enter Email id" type="email"/>
      <input id="inputGroup-sizing-lg" className="form-control" placeholder="Enter Password" type="password"/>
      <br/>
	<div className="btn-group-vertical">
 	    <a href="#" class="btn btn-primary">Login</a>
	    <a href="#" class="btn btn-secondary">Register</a>
	</div>
  </div>
</div>
  );
}

export default App;
