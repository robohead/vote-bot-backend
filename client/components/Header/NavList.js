import React from 'react'
import AppBar from 'material-ui/AppBar'
import styled from 'styled-components'

const NavListWrap = styled.ul`
    display: flex;
    align-items: center;
    justify-content: space-between;
  `

const NavListItem = styled.a`
    color: #000;
    display: inline-block;
    padding: 10px;
    margin-left: 10px;
    text-decoration: none;
  `

let google = 'google.com'

const NavList = () => (
  <NavListWrap
    title='Title'
    iconClassNameRight='muidocs-icon-navigation-expand-more'
  >
    {/* <NavListItem href='#'>Login</NavListItem>
      <NavListItem href='#'>Go to Slack</NavListItem> */}
  </NavListWrap>
)

export default NavList
