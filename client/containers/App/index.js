import React, { Component } from 'react';
import Header from 'components/Header/Header';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import './style.css';

class App extends Component {

  render() {
    return (
      <MuiThemeProvider>
        <Header />
      </MuiThemeProvider>
    );
  }
}

export default App;
