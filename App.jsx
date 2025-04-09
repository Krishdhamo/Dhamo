import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ProfileCard from './ProfileCard'
import GridView from './GridView'
import Todo from './Todo'
import Navbar from './Navbar'
import { BrowserRouter, Routes,Route } from 'react-router-dom'
import store from './store'
import { Provider } from 'react-redux'
const Profilelist ={
  name : "Dhamo",
  Department : "AIDS",
  year : 2,
  mobile : 7418731995,
  address: "D.no: 23/234,cumbum mettu road,cumbum,Theni"
};

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
    <BrowserRouter>
    <Navbar/>
    <Routes>
        <Route path="/profilecard" element={<ProfileCard Profilelist={Profilelist}/>} />
        <Route path="/gridview" element={<GridView />} />
        {/* <Route path="/todo" element={<Todo/>} /> */}
        < Route path='/reduxcounter' element ={<Provider store={store}>
        <Todo/>
        </Provider>
        }
        />
    </Routes>
    </BrowserRouter>
    {/* <Navbar/>
    <ProfileCard profile={Profilelist}/>
    <GridView/>
    <Todo/> */}
    </div>
  );
}

export default App
