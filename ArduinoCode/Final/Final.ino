#include "Arduino.h"
#include <SoftwareSerial.h>

bool CanText = false;
char CharStorageReference[2000];
int ModuleNumber;
SoftwareSerial Module1(34, 35);  //Module(TX, RX)
SoftwareSerial Module2(36, 37);
SoftwareSerial Module3(38, 39);
SoftwareSerial Module4(40, 41);
SoftwareSerial Module5(42, 43);
SoftwareSerial Module6(44, 45);
SoftwareSerial Module7(46, 47);
SoftwareSerial Module8(48, 49);
SoftwareSerial Module9(50, 51);
SoftwareSerial Module10(52, 53);                                                                                                                                                 
String Comment = "";          
String PhoneNumber = "";
String SerialResponse = "";

void setup()
{
  delay(9000);
  Serial.begin(9600);
  delay(1000);         
  Module1.begin(9600);
  delay(1000);
  Module2.begin(9600);
  delay(1000);
  Module3.begin(9600);
  delay(1000);
  Module4.begin(9600);
  delay(1000);
  Module5.begin(9600);
  delay(1000);
  Module6.begin(9600);
  delay(1000);
  Module7.begin(9600);
  delay(1000);
  Module8.begin(9600);
  delay(1000);
  Module9.begin(9600);
  delay(1000);
  Module10.begin(9600);
  delay(1000);
  Serial.print("Start.");                               
}

void loop()
{
  if(Serial.available())
  {
    SerialResponse = Serial.readStringUntil('\r\n');
    CanText = true;
    if(CanText = true)
    {
      char CharStorage[sizeof(CharStorageReference)];
      SerialResponse.toCharArray(CharStorage, sizeof(CharStorage));
      char* ConvertedCharacter = CharStorage;
      char* ParseVariableStorage;
      for(int ParseCounter = 0; ParseCounter < 2; ParseCounter++)
      {
        ParseVariableStorage = strtok_r(ConvertedCharacter, "***", &ConvertedCharacter);
        if(ParseCounter == 0)
        {
          PhoneNumber = ParseVariableStorage;
        }
        if(ParseCounter == 1)
        {
          Comment = ParseVariableStorage;
        }
      }
      delay(200);
      ModuleNumber = ModuleNumber++;
      SendMessage(ModuleNumber, PhoneNumber, Comment);
      delay(200);
      Serial.println("Send to : " + PhoneNumber);
      Serial.println("Message : " + Comment);
      PhoneNumber = "";
      Comment = "";
      SerialResponse = "";
      CanText = false;
      if(ModuleNumber == 10)
      {
        ModuleNumber = 0;
      }
    }
  }
}

void SendMessage(int p_ModuleNumber, String p_PhoneNumber, String p_Comment)
{
  if(p_ModuleNumber == 1)
  {
    Module1.println("AT+CMGF=1\r");
    Module1.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module1.println("Send to : " + p_PhoneNumber);
    Module1.println("Message : " + p_Comment);
    delay(200);
    Module1.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 2)
  {
    Module2.println("AT+CMGF=1\r");
    Module2.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module2.println("Send to : " + p_PhoneNumber);
    Module2.println("Message : " + p_Comment);
    delay(200);
    Module2.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 3)
  {
    Module3.println("AT+CMGF=1\r");
    Module3.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module3.println("Send to : " + p_PhoneNumber);
    Module3.println("Message : " + p_Comment);
    delay(200);
    Module3.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 4)
  {
    Module4.println("AT+CMGF=1\r");
    Module4.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module4.println("Send to : " + p_PhoneNumber);
    Module4.println("Message : " + p_Comment);
    delay(200);
    Module4.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 5)
  {
    Module5.println("AT+CMGF=1\r");
    Module5.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module5.println("Send to : " + p_PhoneNumber);
    Module5.println("Message : " + p_Comment);
    delay(200);
    Module5.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 6)
  {
    Module6.println("AT+CMGF=1\r");
    Module6.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module6.println("Send to : " + p_PhoneNumber);
    Module6.println("Message : " + p_Comment);
    delay(200);
    Module6.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 7)
  {
    Module7.println("AT+CMGF=1\r");
    Module7.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module7.println("Send to : " + p_PhoneNumber);
    Module7.println("Message : " + p_Comment);
    delay(200);
    Module7.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 8)
  {
    Module8.println("AT+CMGF=1\r");
    Module8.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module8.println("Send to : " + p_PhoneNumber);
    Module8.println("Message : " + p_Comment);
    delay(200);
    Module8.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 9)
  {
    Module9.println("AT+CMGF=1\r");
    Module9.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module9.println("Send to : " + p_PhoneNumber);
    Module9.println("Message : " + p_Comment);
    delay(200);
    Module9.print((char)26);
    delay(200);
  }
  if(p_ModuleNumber == 10)
  {
    Module10.println("AT+CMGF=1\r");
    Module10.println("AT+CMGS=\"" + p_PhoneNumber + "\"\r");
    delay(200);
    Module10.println("Send to : " + p_PhoneNumber);
    Module10.println("Message : " + p_Comment);
    delay(200);
    Module10.print((char)26);
    delay(200);
  }
}
