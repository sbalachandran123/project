int trigPin=12;
int echoPin=10;
int vcc=13;
int gnd=10;


long  duration;
int distance;


void setup()
{
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(vcc, OUTPUT);
    pinMode(gnd, OUTPUT);
     digitalWrite(vcc, HIGH);
     digitalWrite(gnd, LOW);
   
  Serial.begin(9600);
  
}

void loop()
{
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10); 
  digitalWrite(trigPin, LOW);
  
  
  distance=duration*0.034/2;
  
  Serial.print("Distance:");
  Serial.println(distance);
  delay(1000);
  
  if(distance<50)
  {
    digitalWrite(1, HIGH);
    delay(1000);
    digitalWrite(2, HIGH);
    delay(1000);
    digitalWrite(3, HIGH);
    delay(1000);
  }
  else
  {
    digitalWrite(1, LOW);
    delay(1000);
    digitalWrite(2, LOW);
    delay(1000);
    digitalWrite(3, LOW);
    delay(1000);
  }
    
    
}