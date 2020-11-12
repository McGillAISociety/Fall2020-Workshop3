import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';
import axios from 'axios';

function App() {
  const [prediction, setPrediction] = useState(-1);
  const [selectedFile, setSelectedFile] = useState(null);
  const [image, setImage] = useState(null);

  const submitForm = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("image", selectedFile);
    axios.post('/predict/image', formData)
    .then(res => {
      setPrediction(res.data)
    })
    .catch(err => {
      alert(err);
    })
  }

  const setFileAndImage = (file) => {
    setSelectedFile(file);
    setImage(URL.createObjectURL(file));
  }


  return (
    <div className="App">
      <form onSubmit={e => submitForm(e)} >
        <input 
          type="file"
          onChange={e => setFileAndImage(e.target.files[0])}
        />
        <button type="submit">
          Get Prediction!
        </button>
      </form>

      <img src={image}>
      </img>
      <p>{prediction == -1 ? "Please upload an image and get a prediction" : `The current prediction is ${prediction}`}</p>
      
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

export default App;
