import React from 'react'
import AppBar from 'material-ui/AppBar'
import styled from 'styled-components'
import FlatButton from 'material-ui/FlatButton'

const NavListWrap = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 100%;
    margin-top: -4px;
  `

let google = 'http://google.com'
let googleRu = 'http://google.ru'

const NavList = () => (
  <NavListWrap>
    <FlatButton label='google.com' href={google} />
    <FlatButton label='google.ru' href={googleRu} />
  </NavListWrap>
)

export default NavList
