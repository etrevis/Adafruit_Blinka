"""Pin definitions for the Rock Pi E."""

from adafruit_blinka.microcontroller.rockchip.rk3328 import pin

D3 = pin.GPIO3_A4  # /UART1_TX/PIN 100/
D5 = pin.GPIO3_A6  # /UART1_RX/PIN 102/
D7 = pin.GPIO1_D4  # /PIN 60/
D8 = pin.GPIO2_A0  # /UART2_TX/PIN 64/
D10 = pin.GPIO2_A1  # /UART2_RX/PIN 65/
D11 = pin.GPIO2_A2  # /PWM_IR/PIN 66/
D12 = pin.GPIO2_C2  # /PDM_CLK/I2S1_SCLK/PIN 82/
D13 = pin.GPIO2_A3  # /PIN 67/
D15 = pin.GPIO0_D3  # /PIN 27/
D19 = pin.GPIO3_A1  # /SPI0_TXD/PIN 97/
D21 = pin.GPIO3_A2  # /SPI0_RXD/PIN 98/
D23 = pin.GPIO3_A0  # /SPI0_CLK/PIN 96/
D24 = pin.GPIO3_B0  # /SPI0_CSN0/PIN 104/
D26 = pin.GPIO2_B4  # /PIN 76/
D27 = pin.GPIO2_A4  # /I2C1_SDAPIN 68/
D28 = pin.GPIO2_A5  # /I2C1_SCL/PIN 69/
D29 = pin.GPIO2_C4  # /I2S1_SDIO1/PDM_SDI1/PIN 84/
D31 = pin.GPIO2_C5  # /I2S1_SDIO2/PDM_SDI2/PIN 85/
D32 = pin.GPIO2_C0  # /I2S1_LRCK_RX/PIN 80/
D33 = pin.GPIO2_A6  # /PWM2/PIN 70/
D35 = pin.GPIO2_C1  # /I2S1_LRCK_TX/PIN 81/
D36 = pin.GPIO2_B7  # /I2S1_MCLK/PIN 79/
D37 = pin.GPIO2_C6  # /PDM_SDI3/PIN 86/
D38 = pin.GPIO2_C3  # /PDM_SDI0/I2S1_SDI/PIN 83/
D40 = pin.GPIO2_C7  # /PDM_FSYNC/I2S1_SDO/PIN 87/

SDA2 = D27
SCL2 = D28

SDA = SDA2
SCL = SCL2

SCLK = D23
MOSI = D19
MISO = D21
CS = D24
SCK = SCLK

UART1_TX = D3
UART2_RX = D5
UART2_TX = D8
UART2_RX = D10

UART4_TX = D19
UART4_RX = D21

UART_TX = UART2_TX
UART_RX = UART2_RX

PWM2 = pin.PWM2

ADC_IN1 = pin.ADC_IN1
