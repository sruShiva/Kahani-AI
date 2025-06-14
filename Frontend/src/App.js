

// import logo from './logo.svg';

import IntroPage1 from './IntroPage1';
import StoryMaker from './Storymaker';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    
    <Router>
      <Routes>
      {/* <Route path="/" element={<PdfFormFiller/>} /> */}
       
        <Route path="/" element={<IntroPage1 />} />
        <Route path="/ai-story-maker" element={<StoryMaker />} />
       
      </Routes>
    </Router>
    
  );
}

export default App;

