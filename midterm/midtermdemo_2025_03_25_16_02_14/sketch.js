let sound1, sound2, sound3; 

function preload() {
  
  sound1 = loadSound('kick 2.wav'); 
  sound2 = loadSound('Simple Hat 2-1.wav'); 
  sound3 = loadSound('Simple Snare 3-1.wav'); 
}

function setup() {
  createCanvas(400, 400);
  textAlign(CENTER, CENTER);
  textSize(24);
  background(200);
}

function draw() {
  fill(0);
  text('Press A, M, or S to play sounds', width / 2, height / 2);
}

function keyPressed() {

  if (key === 'A' || key === 'a') {
    sound1.play(); 
  } else if (key === 'M' || key === 'm') {
    sound2.play(); 
  } else if (key === 'S' || key === 's') {
    sound3.play(); 
  }
}