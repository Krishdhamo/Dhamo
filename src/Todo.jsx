// import React,{useState} from "react";
// const Todo =() => {
//     const[state,setState]=useState(20);
//         return(
//             <div>Todo
//                 <h1>{state}</h1>
//                 <button onClick={() =>setState(state+1)}>Increment</button>
//                 <button onClick={() =>setState(state-2)}>Decrement</button>
//                 <button onClick={() =>setState(state-state)}>Reset</button>
//             </div>
//     )
// }
// export default Todo;
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement ,reset } from "./store";
const Todo= () => {
  const count = useSelector((state) => state.counter.count);
  const dispatch = useDispatch();
  return (
    <div style={{
        border:"2px solid black",
        margin:"400px auto",
        width:"100px",
        height:"100px",
        fontSize:"20px",
        textAlign:"center",
        backgroundColor:"yellow",
        fontStyle:"italic",
        justifyContent:"center",
        alignItems:"center"}}
    >
      <div>Count:{count}</div>
      
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
      <button onClick={() => dispatch(reset())}>reset</button>
    </div>
  );
};

export default Todo;