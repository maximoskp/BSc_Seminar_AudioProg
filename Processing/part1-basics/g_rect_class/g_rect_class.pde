ArrayList<Rectangle_Class> r;

void setup(){
  size(600,400);
  r = new ArrayList<Rectangle_Class>();
  for (int i=0; i<10; i++){
    r.add(new Rectangle_Class(width, height));
  }
  
}

void draw(){
  background(0);
  for (int i=0; i<10; i++){
    r.get(i).draw_myself();
  }
}

void mouseClicked(){
  for (int i=0; i<10; i++){
    r.get(i).check_if_clicked(mouseX, mouseY);
  }
}