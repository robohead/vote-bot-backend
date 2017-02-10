import React, { Component } from 'react'
import styled from 'styled-components'
import RaisedButton from 'material-ui/RaisedButton'

import Button from 'components/Button'

const FeatureWrap = styled.div`
  width: 100%;
  height: 80vh;
  background-color: papayawhip;
  background-image: url();
  background-position: 50% 50%;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
  align-items: center;
`

class Feature extends Component {
  render () {
    return (
      <FeatureWrap>
        <RaisedButton label='vote now' primary />
      </FeatureWrap>
    )
  }
}

export default Feature
