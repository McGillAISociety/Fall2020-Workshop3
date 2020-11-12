import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import HomeIcon from '@material-ui/icons/Home';
import { useHistory } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(5)
  },
  menuButton: {
    marginRight: theme.spacing(-5),
  },
  title: {
    flexGrow: 1,
  },
}));



function TopBar(props) {
  const classes = useStyles();
  const history = useHistory();

  function goHome(){
    history.push('/');
  }

    return(
      <div className={classes.root}>
      <AppBar position="static">
      <Toolbar>
        <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu" onClick={goHome}>
          <HomeIcon />
        </IconButton>
        <Typography variant="h6" className={classes.title}>
          {props.title}
        </Typography>
      </Toolbar>
    </AppBar>
  </div>
  )
}

export default TopBar;