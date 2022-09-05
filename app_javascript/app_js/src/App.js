import React from 'react';
import "./App.css";

class App extends React.Component {
  state={
    curDT : new Date().toLocaleString(),
  }
  render(){
    return (
      <div className="App">
        <h1> Current time in Moscow </h1>
        <p>{this.state.curDT}</p>
      </div>
    );
  }
}

export default App;