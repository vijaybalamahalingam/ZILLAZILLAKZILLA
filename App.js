import React, { useState } from "react";

function Carousel() {
  const images = [
    "https://via.placeholder.com/400x300?text=Image+1",
    "https://via.placeholder.com/400x300?text=Image+2",
    "https://img.freepik.com/premium-photo/small-lake-with-green-lawn-blue-pond-background_954226-96300.jpg?size=626&ext=jpg&ga=GA1.1.386372595.1697587200&semt=ais",
    "https://wrlandconservancy.org/wp-content/themes/western-reserve/img/placeholder.webp",
  ];

  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const nextImage = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const prevImage = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  return (
    <div className="carousel-container centered">
      <h1 className="carousel-heading">Gallery</h1>
      <div className="carousel-wrapper">
        <button className="carousel-button round left" onClick={prevImage}>
          &#9664;
        </button>
        <img
          src={images[currentImageIndex]}
          alt={`Image ${currentImageIndex + 1}`}
          className="carousel-image"
        />
        <button className="carousel-button round right" onClick={nextImage}>
          &#9654; {/* Right arrow */}
        </button>
      </div>
    </div>
  );
}

export default Carousel;
