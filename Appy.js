App.js demo

// just a demo App.js
import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Services from './components/Services';
import UpcomingLives from './components/UpcomingLives';
import VideosSection from './components/VideosSection';
import PremiumVideos from './components/PremiumVideos';
import ContactForm from './components/ContactForm';
import Articles from './components/Articles';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <VideosSection />
      <Services />
      <UpcomingLives />
      <PremiumVideos />
      <ContactForm />
      <Articles />
      <Footer />
    </div>
  );
}

export default App;
