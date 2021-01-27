function getClassName(index) {
  return "image-carousel-slides-" + index;
}

function getDotName(index) {
  return "image-carousel-dots-" + index;
}

function plusSlides(index, n) {
  slideIndex[index] += n;
  showSlides(index);
}

function currentSlide(indexx, n) {
  slideIndex[index] = n;
  showSlides(className);
}

function showSlides(index) {
  className = getClassName(index);
  dotName = getDotName(index);
  var n = slideIndex[index];
  var i;
  var slides = document.getElementsByClassName(className);
  var dots = document.getElementsByClassName(dotName);

  if (n > slides.length) {
    slideIndex[index] = 1;
  }
  if (n < 1) {
    slideIndex[index] = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex[index] - 1].style.display = "block";
  dots[slideIndex[index] - 1].className += " active";
}
