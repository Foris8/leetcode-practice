import './styles.css';
import submitForm from './submitForm';

export default function App() {
  return (
    
    <form
      // Ignore the onSubmit prop, it's used by GFE to
      // intercept the form submit event to check your solution.
  
      onSubmit={submitForm}>
      <div>
        <label for="name">Name
         <input type="text" id="name" placeHolder="enter your name"/>
      </label>
      </div>
      <div>
        <label for="email">Email
          <input type="text" id="email" placeHolder="enter your email"/>
        </label>
      </div>
      <div>
        <label for="message">Message
          <input type="textarea>" id="message" placeHolder="enter your meassage"/>
        </label>
      </div>
    </form>
  );
}
