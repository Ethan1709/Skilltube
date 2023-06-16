import './App.css';
import { Video } from './components/Video';
import { Video_test } from './components/Video_test';
import { Header } from './components/Header';
import Player from './components/Player';


function App() {
  return (
    <div>
      <Header/>
      <Video id="wJ7FLJcGNCs"/>
      <Video id="LSXSDnjG6gs"/>
      <Video id="0J2QdDbelmY"/>
      <Video id="8ZdpA3p9ZMY"/>
      <Video id="Tk-lFEga9kE"/>
      <Video_test />
      <Player />

    </div>
  );
}

export default App;
