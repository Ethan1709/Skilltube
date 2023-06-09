import React, { Component } from 'react';
import ReactPlayer from 'react-player';

class Player extends Component {
    render () {
      return (
        <div className='player-wrapper'>
          <ReactPlayer
            className='react-player fixed-bottom'
            url= '../public/videos/demo.mp4'
            width='60%'
            height='60%'
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