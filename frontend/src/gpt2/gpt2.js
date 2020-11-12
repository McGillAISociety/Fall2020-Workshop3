import React, {useState} from 'react';
import axios from 'axios';
import { getTextPrediction } from '../api';

function GPT2() {
  const [startingText, setStartingText] = useState("Once upon a time...");
  const [textLength, setTextLength] = useState(40);
  const [finalText, setFinalText] = useState(null);

  const submitForm = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("starting_tokens", startingText);
    formData.append("sequence_length", textLength);
    getTextPrediction(formData)
    .then(res => {
        setFinalText(res);
    })

  }

  return (
      <div className="main-div">
      <form onSubmit={e => submitForm(e)} >
        <label>
            Starting text: &nbsp;
            <input 
            type="text"
            value={startingText}
            onChange={e => setStartingText(e.target.value)}
            /> 
        </label>
        <br/>
        <label>
            Text length: &nbsp;
            <input 
                type="number" 
                value={textLength}
                onChange={e => setTextLength(e.target.value)}
            />      
        </label>
        <br/>
        <button type="submit">
          Get Prediction!
        </button>
      </form>

      <p>{finalText == null ? "Click get prediction!" : `${finalText}`}</p>
      </div>
  );
}

// class App extends React.Component {
// 	constructor(props) {
//     super(props);
//     this.state = {
//     file: ''
//     };
//   }

//   render() {
//     return <div>
//     <input type='file' onChange={(e) => {
//     this.setState({file: e.target.files[0]}, () => {
//     	console.log('state', this.state);
//     })
//     }} />
//     </div>;
//   }
// }

export default GPT2;
