var imgArray = [];
var w1,w2,w3,m1,m2,m3;
var ImgInx = 0;
function setup() {
  // put setup code here
  var canvas = createCanvas(1400,650);
  background(50,50,50);
  noStroke();
  fill(255,255,255); // white
  rect(200,100,400,400); // before canvas
  rect(820,100,400,400); // after canvas


  fill(153,0,255); // purple
  rect(630,250,130,30); // transition arrow
  triangle(750, 230, 750, 300, 800, 265);

  fill(102, 153, 255); // blue
  rect(50,130,100,50); // undo button
  rect(50,200,100,50); // clear button

  rect(970,530,100,50); // save button
  rect(650,310,100,50); // metamon button

  fill(255,255,255); // white font color
  textSize(20);
  //text("upload", 70, 160); // w+20 h+30
  text("undo", 75, 160);
  text("clear", 75, 230);

  text("save", 990, 560);
  text("MetaMon", 660, 340);

  // upload an image by drag and drop action
  canvas.drop(gotFile);

  // upload explanation
  fill(100,100,100);
  textSize(14);
  textLeading(20);
  text("to upload an image from yor computer,\n just drag and drop the image anywhere\n              on this canvas!",280,270);
  textAlign(CENTER);

  //text input
  input = createInput('write something here (some features that explains)');
  input.position(200,530);
  input.size(395);

  /*button = createButton('submit');
  button.position(input.x + input.width, 530);
  button.mousePressed(saveTextAsFile);*/
}


function gotFile(file) // drop the image to the canvas
{
  //createP(file.name + " " + file.size);
  {
    var img = createImg(file.data);
    img.hide();
    image(img,200,100,400,400);
  }
}

function saveTextAsFile()
{
  var textToWrite = input.value();
  var textList = split(textToWrite,' ');
  saveStrings(textList,"input.txt");
  /*var textToWrite = {}
  textToWrite = input.value();
  saveJSON(textToWrite, 'input.json');*/
}

function touchMoved()
{
  fill(0,0,0);
  stroke(0,0,0);
  var penSize = 3;
  strokeWeight(penSize);
  if(200 <= mouseX && mouseX <= 600 && 100 <= mouseY && mouseY <= 500
     && 200 <= pmouseX && pmouseX <= 600 && 100 <= pmouseY && pmouseY <= 500) // drawing in 'before canvas'
      line(pmouseX,pmouseY,mouseX,mouseY);

}

function mousePressed(){
  ////buttons////
  // CLEAR BUTTON
  if(50 <= mouseX && mouseX <= 150 && 200 <= mouseY && mouseY <= 250)
  {
    noStroke();
    fill(255,255,255); // white
    rect(200,100,400,400); // before canvas
  }

  //UNDO BUTTON - pop stack
  if(50 <= mouseX && mouseX <= 150 && 130 <= mouseY && mouseY <= 180
    && imgArray.length > 0)
  {
    var popImg = imgArray.pop();
    image(popImg,200,100,400,400);
  }

  // METAMON BUTTON - save before image and text
  if(650 <= mouseX && mouseX <= 750 && 310 <= mouseY && mouseY <=360)
  {
    /*saveTextAsFile();
    img = get(200,100,400,400);
    save(img,"before.jpg");*/
  }
}

function touchEnded(){
  ////buttons////
  // for UNDO BUTTON - push stack
  if(200 <= mouseX && mouseX <= 600 && 100 <= mouseY && mouseY <= 500
     && 200 <= pmouseX && pmouseX <= 600 && 100 <= pmouseY && pmouseY <= 500
  ) // drawing in before canvas
  {
    img = get(200,100,400,400);
    append(imgArray, img);
  }
}
