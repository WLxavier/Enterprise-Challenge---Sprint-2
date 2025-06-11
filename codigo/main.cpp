#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);

  // Inicializa o MPU6050
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.println("");
  delay(100);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Imprime os dados de aceleração (vibração)
  Serial.print("AccelX: ");
  Serial.print(a.acceleration.x);
  Serial.print(", AccelY: ");
  Serial.print(a.acceleration.y);
  Serial.print(", AccelZ: ");
  Serial.print(a.acceleration.z);
  Serial.println(" m/s^2");

  // Imprime os dados do giroscópio (opcional)
  // Serial.print("GyroX: ");
  // Serial.print(g.gyro.x);
  // Serial.print(", GyroY: ");
  // Serial.print(g.gyro.y);
  // Serial.print(", GyroZ: ");
  // Serial.print(g.gyro.z);
  // Serial.println(" rad/s");

  delay(500); // Intervalo de leitura dos dados
}


