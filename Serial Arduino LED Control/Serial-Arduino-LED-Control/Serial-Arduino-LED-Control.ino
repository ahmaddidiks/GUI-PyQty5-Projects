char dataRead = 0;
int state = 0;

void setup(){
Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){

if(Serial.available()){
	dataRead = Serial.read();
	state = dataRead - '0';
	if(state == 0) digitalWrite(LED_BUILTIN, LOW);
	else digitalWrite(LED_BUILTIN, HIGH);
	Serial.println(state);
	}
}
