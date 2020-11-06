
float x = 0.0;
float y = 100.0;

// setup is called once, when the program starts
void setup(){
  size(900, 500);
  background(30);
}

// draw is called according to framerate (default is 60 frames per second)
void draw(){
  background(30);
  fill(255);
  stroke(255,0,0);
  rect( x, y , 100,100);
  x += 3; // equal to x = x + 3;
  y += 1; // equal to y = y + 1;
}
