// initialise variable
float x, y;

void setup(){
  size(600,300);
  x = 0.0;
  y = 0.0;
}

void draw(){
  background(40);
  x = increase_variable(x, 1.3);
  y = increase_variable(y, 2.3);
  if (x > 100.0 && y > 100.0){
    println("bang! - " + x + ", " + y);
    x = 0.0;
    y = 0.0;
  }
}

float increase_variable(float t, float incr){
  t += incr;
  return t;
}