import React, { Component } from 'react'
import Header from 'components/Header/Header'
import Feature from 'components/Feature'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import getMuiTheme from 'material-ui/styles/getMuiTheme'

import './style.css'

const muiTheme = getMuiTheme({
  appBar: {
    color: 'transparent',
    textColor: '#000'
  }
})

class App extends Component {

  render () {
    return (
      <div>
        <MuiThemeProvider muiTheme={muiTheme}>
          <Header />
        </MuiThemeProvider>
        <MuiThemeProvider>
          <Feature />
        </MuiThemeProvider>
      </div>
    )
  }
}

export default App
