import {useState} from 'react'
import './styles.css';

let id = 0

const Ini_List = [
  {id: id++, content: 'Walk the dog'},
  {id: id++, content: 'Water the plants'},
  {id: id++, content: 'wash dishses'}
]

export default function App() {
  const [list,setList] = useState(Ini_List)
  const [addTask, setAddTask] = useState("")

  const handleSubmit = (content)=>{
    setList(list.concat({
      id: id++, content: content
    }));
    setAddTask("")
  }
  return (
    <div>
      <h1>Todo List</h1>
      <div>
        <input type="text" placeholder="Add your task" value={addTask} onChange={(event)=>{
          setAddTask(event.target.value)
        }}/ >
        <div>
          <button onClick={()=>handleSubmit(addTask)}>Submit</button>
        </div>
      </div>
      <ul>
        {list.map(({ id, content }) => {
          return(
            <li key={id}>
            <span>{content}</span>
            <button onClick={() => {
              setList(list.filter((item) => item.id !== id));
            }}>Delete</button>
          </li>
          )

        })}
        
      </ul>
    </div>
  );
}
