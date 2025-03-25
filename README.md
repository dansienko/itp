hello and welcome to my midterm documentation readme. 
First things first, I will check out the assignment. It seems that before I code, I will need 3 samples. I pulled some drum set noises from my hard drive. 
I will now attempt to use AI to finish this whole assignment in seconds. I am going to do what I did for the last assignment, and copy-paste the project prompt into ChatGPT and see how we do.
Here's what Dr.GPT had to say
![Screenshot 2025 03 11 At 3.24.16 PM](../../../Desktop/game%20scoring/Screenshot%202025-03-11%20at%203.24.16 PM.png)![Screenshot 2025 03 11 At 3.24.47 PM](../../../Desktop/game%20scoring/Screenshot%202025-03-11%20at%203.24.47 PM.png)![Screenshot 2025 03 11 At 3.25.21 PM](../../../Desktop/game%20scoring/Screenshot%202025-03-11%20at%203.25.21 PM.png)![Screenshot 2025 03 11 At 3.25.39 PM](../../../Desktop/game%20scoring/Screenshot%202025-03-11%20at%203.25.39 PM.png)
Side note, just realized all of my screenshots are routed to my intro to game scoring folder from semester 2. Cool.
Now I will copy and paste the code ChatGPT wrote from me and see what we get. Before I run the code, I will insert the correct pathing to my sound files.
Eureka, it works! All I will do now is edit my snare and hi hat files to play one repetition of the sound.
Using logic, I was able to cut the audio files to the correct level and was left with this line of code.

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

Here's the link to my p5 project!
https://editor.p5js.org/dansienko/sketches/2GNAXzmLj