import React from 'react';
import { useNavigate } from 'react-router-dom';
import './IntroPage1.css';

const IntroPage1 = () => {
    const navigate = useNavigate();

    const gotostorymakerpage = () => {
        navigate('/ai-story-maker');
    };
    
    return (
        <div className="container">
            <h1 className="magic-text">Kahani AI: Revolutionizing Bedtime Stories</h1>
            <p className="subtext">Create your own AI story</p>
            <button className="start-button" onClick={gotostorymakerpage}>Get Started</button>
            <img
                src="https://img.freepik.com/premium-photo/painting-children-reading-book-with-black-background_716800-1393.jpg"
                alt="Cute Story"
                className="story-image"
            />
        </div>
    );
}

export default IntroPage1;
