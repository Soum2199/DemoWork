// import React from 'react'
import React, { useState } from 'react';

const Carousel = ({ images }) => {
    const [currentIndex, setCurrentIndex] = useState(0);

    const nextImage = () => {
      setCurrentIndex(prevIndex =>
        prevIndex === images.length - 1 ? 0 : prevIndex + 1
      );
    };

    const prevImage = () => {
      setCurrentIndex(prevIndex =>
        prevIndex === 0 ? images.length - 1 : prevIndex - 1
      );
    };

    return (
      <div>
        <button onClick={prevImage}>Previous</button>
        <img src={images[currentIndex]} alt={`Image ${currentIndex + 1}`} />
        <button onClick={nextImage}>Next</button>
      </div>
    );
  };

  export default Carousel;


