import React, { Component } from 'react';
import ReactPlayer from 'react-player';

class Player extends Component {
    render () {
      return (
        <div className='player-wrapper'>
          <ReactPlayer
            className='react-player fixed-bottom'
            url= 'https://drive.google.com/file/d/11nydq9bxPLZScX_WUlAQbkFVr5ypGbxQ/view?usp=sharing'
            width='80%'
            height='80%'
            controls = {true}
            image='../public/images/image1.JPG'
            loop = { true }
            playing = {true}

          />
        </div>
      )
    }
  }

  export default Player;