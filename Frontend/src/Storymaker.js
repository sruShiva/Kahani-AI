import React, { useState } from 'react';
import axios from 'axios';
import './Storymaker.css';

const StoryMaker = () => {
  const [pages, setPages] = useState(1);
  const [topic, setTopic] = useState('');
  const [generatedStories, setGeneratedStories] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (pages > 0 && topic) {
      setLoading(true);
      try {
        const response = await axios.get('http://localhost:9010/create-story', {
          params: {
            num_pages: pages,
            topic: topic,
          },
        });
        const stories = response.data; // Assuming the API returns the stories directly
        setGeneratedStories(stories);
      } catch (error) {
        console.error('Error fetching stories:', error);
        // Optionally handle error state
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="storymaker-container">
      <h1 className="storymaker-title">AI Story Maker</h1>
      <div className="storymaker-input">
        <label htmlFor="pages" className="storymaker-label">Specify the number of pages for your story</label>
        <input
          id="pages"
          type="number"
          value={pages}
          onChange={(e) => setPages(Number(e.target.value))}
          className="storymaker-textfield"
        />
      </div>
      <div className="storymaker-input">
        <label htmlFor="topic" className="storymaker-label">Provide a topic for your story</label>
        <input
          id="topic"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          className="storymaker-textfield"
        />
      </div>
      <button className="storymaker-button" onClick={handleGenerate}>
        Generate
      </button>

      {loading ? (
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p className="loading-text">Working your magic...</p>
        </div>
      ) : (
        <div className="storymaker-stories">
          {generatedStories.map((story, index) => (
            <div key={index} className="storymaker-paper">
              <h2 className="storymaker-paper-title">{story.theme}</h2>
              <img src={story.image} alt={`Page ${index + 1}`} className="storymaker-image" />
              <p className="storymaker-paper-text">{story.story}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default StoryMaker;
