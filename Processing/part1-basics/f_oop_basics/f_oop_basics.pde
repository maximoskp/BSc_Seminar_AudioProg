Human h;

void setup(){
  size(900,700);
  h = new Human("Melissa", "female", 100, 200);
}

void draw(){
  background(40);
  h.draw_myself();
}

void mouseDragged(){
  h.move_myself(mouseX, mouseY);
}
void mousePressed(){
  h.move_myself(mouseX, mouseY);
}

class Human{
  float x, y;
  PImage my_image;
  String my_name;
  Human(String name, String gender, float x_position, float y_position){
    my_name = name;
    x = x_position;
    y = y_position;
    if (gender.equals("male")){
      my_image = loadImage("./figs/gentleman_image.png");
    }else{
      my_image = loadImage("./figs/lady_image.png");
    }
  }
  void draw_myself(){
    image(my_image, x, y, 70.0, 100.0);
  }
  void move_myself(float x_in, float y_in){
    x = x_in;
    y = y_in;
  }
}