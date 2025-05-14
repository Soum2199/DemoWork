// To Toggle switch between ON and OFF

 import React from 'react';
import ReactDOM from 'react-dom';

class Toggle extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      isActive: false
    }
  }

  handleClick = () => {
    this.setState(prevState => ({
      isActive: !prevState.isActive
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>{this.state.isActive ? "ON" : "OFF"}</button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);