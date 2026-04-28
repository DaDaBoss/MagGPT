import './App.css'
import SideBar from "../Features/SideBar/SideBar.tsx";
import Chat from "../Features/Chat/Chat.tsx";
import {Route, Routes} from "react-router-dom";

function App() {

  return (
    <>
        <SideBar />
        <Routes>
            <Route path="/:id" element={<Chat/>}/>
            <Route path="/" element={<Chat/>}/>
        </Routes>
    </>
  )
}

export default App
