import React from 'react'
import AppBar from 'material-ui/AppBar'
import NavList from './NavList'

/**
 * A simple example of `AppBar` with an icon on the right.
 * By default, the left icon is a navigation-menu.
 */
const Header = () => (
  <AppBar
    title='Title'
    iconElementRight={<NavList />}
  />
)

export default Header
