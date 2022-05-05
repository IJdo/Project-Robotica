EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:Battery BT1
U 1 1 625EABDC
P 3800 3150
F 0 "BT1" V 3555 3150 50  0000 C CNN
F 1 "Battery" V 3646 3150 50  0000 C CNN
F 2 "" V 3800 3210 50  0001 C CNN
F 3 "~" V 3800 3210 50  0001 C CNN
	1    3800 3150
	0    1    1    0   
$EndComp
$Comp
L Motor:Motor_DC M2
U 1 1 625ED758
P 3850 4300
F 0 "M2" V 3555 4250 50  0000 C CNN
F 1 "Motor_DC" V 3646 4250 50  0000 C CNN
F 2 "" H 3850 4210 50  0001 C CNN
F 3 "~" H 3850 4210 50  0001 C CNN
	1    3850 4300
	0    1    1    0   
$EndComp
$Comp
L Motor:Motor_DC M1
U 1 1 625F134D
P 3850 3700
F 0 "M1" V 3555 3650 50  0000 C CNN
F 1 "Motor_DC" V 3646 3650 50  0000 C CNN
F 2 "" H 3850 3610 50  0001 C CNN
F 3 "~" H 3850 3610 50  0001 C CNN
	1    3850 3700
	0    1    1    0   
$EndComp
$Comp
L Robothond-rescue:HC-SR04-HC-SR04 U2
U 1 1 625F79B7
P 8100 3150
F 0 "U2" H 8530 3146 50  0000 L CNN
F 1 "HC-SR04" H 8530 3055 50  0000 L CNN
F 2 "XCVR_HC-SR04" H 8100 3150 50  0001 L BNN
F 3 "" H 8100 3150 50  0001 L BNN
F 4 "Osepp" H 8100 3150 50  0001 L BNN "MANUFACTURER"
	1    8100 3150
	1    0    0    -1  
$EndComp
$Comp
L Robothond-rescue:HC-SR04-HC-SR04 U3
U 1 1 625F865C
P 8100 3800
F 0 "U3" H 8530 3796 50  0000 L CNN
F 1 "HC-SR04" H 8530 3705 50  0000 L CNN
F 2 "XCVR_HC-SR04" H 8100 3800 50  0001 L BNN
F 3 "" H 8100 3800 50  0001 L BNN
F 4 "Osepp" H 8100 3800 50  0001 L BNN "MANUFACTURER"
	1    8100 3800
	1    0    0    -1  
$EndComp
$Comp
L Robothond-rescue:HC-SR04-HC-SR04 U4
U 1 1 625F8A7B
P 8100 4450
F 0 "U4" H 8530 4446 50  0000 L CNN
F 1 "HC-SR04" H 8530 4355 50  0000 L CNN
F 2 "XCVR_HC-SR04" H 8100 4450 50  0001 L BNN
F 3 "" H 8100 4450 50  0001 L BNN
F 4 "Osepp" H 8100 4450 50  0001 L BNN "MANUFACTURER"
	1    8100 4450
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR0101
U 1 1 625FEA4F
P 7900 4650
F 0 "#PWR0101" H 7900 4400 50  0001 C CNN
F 1 "GNDREF" H 7905 4477 50  0000 C CNN
F 2 "" H 7900 4650 50  0001 C CNN
F 3 "" H 7900 4650 50  0001 C CNN
	1    7900 4650
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR0102
U 1 1 62604D11
P 7900 4000
F 0 "#PWR0102" H 7900 3750 50  0001 C CNN
F 1 "GNDREF" H 7905 3827 50  0000 C CNN
F 2 "" H 7900 4000 50  0001 C CNN
F 3 "" H 7900 4000 50  0001 C CNN
	1    7900 4000
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR0103
U 1 1 62605A22
P 7900 3350
F 0 "#PWR0103" H 7900 3100 50  0001 C CNN
F 1 "GNDREF" H 7905 3177 50  0000 C CNN
F 2 "" H 7900 3350 50  0001 C CNN
F 3 "" H 7900 3350 50  0001 C CNN
	1    7900 3350
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR0104
U 1 1 6261A3AF
P 4400 4300
F 0 "#PWR0104" H 4400 4050 50  0001 C CNN
F 1 "GNDREF" H 4405 4127 50  0000 C CNN
F 2 "" H 4400 4300 50  0001 C CNN
F 3 "" H 4400 4300 50  0001 C CNN
	1    4400 4300
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0105
U 1 1 6261BC2C
P 6550 2600
F 0 "#PWR0105" H 6550 2450 50  0001 C CNN
F 1 "+5V" V 6565 2728 50  0000 L CNN
F 2 "" H 6550 2600 50  0001 C CNN
F 3 "" H 6550 2600 50  0001 C CNN
	1    6550 2600
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0106
U 1 1 6261FED0
P 7900 4350
F 0 "#PWR0106" H 7900 4200 50  0001 C CNN
F 1 "+5V" V 7915 4478 50  0000 L CNN
F 2 "" H 7900 4350 50  0001 C CNN
F 3 "" H 7900 4350 50  0001 C CNN
	1    7900 4350
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0107
U 1 1 62622EBB
P 7900 3700
F 0 "#PWR0107" H 7900 3550 50  0001 C CNN
F 1 "+5V" V 7915 3828 50  0000 L CNN
F 2 "" H 7900 3700 50  0001 C CNN
F 3 "" H 7900 3700 50  0001 C CNN
	1    7900 3700
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0108
U 1 1 62623C8F
P 7900 3050
F 0 "#PWR0108" H 7900 2900 50  0001 C CNN
F 1 "+5V" V 7915 3178 50  0000 L CNN
F 2 "" H 7900 3050 50  0001 C CNN
F 3 "" H 7900 3050 50  0001 C CNN
	1    7900 3050
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7900 3150 7250 3150
Wire Wire Line
	7250 3150 7250 3600
Wire Wire Line
	7250 3600 7150 3600
Wire Wire Line
	7350 3700 7350 3250
Wire Wire Line
	7350 3250 7900 3250
Wire Wire Line
	7900 4450 7350 4450
Wire Wire Line
	7350 4450 7350 4000
Wire Wire Line
	7150 4100 7250 4100
Wire Wire Line
	7250 4100 7250 4550
Wire Wire Line
	7250 4550 7900 4550
$Comp
L Robothond-rescue:L298N-L298N U1
U 1 1 625E9C6D
P 5100 3800
F 0 "U1" H 5100 4665 50  0000 C CNN
F 1 "L298N" H 5100 4574 50  0000 C CNN
F 2 "TO127P2020X500X2100-15" H 5100 3800 50  0001 L BNN
F 3 "" H 5100 3800 50  0001 L BNN
F 4 "STMicroelectronics" H 5100 3800 50  0001 L BNN "MANUFACTURER"
F 5 "IPC-7351B" H 5100 3800 50  0001 L BNN "STANDARD"
F 6 "5.0mm" H 5100 3800 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 7 "" H 5100 3800 50  0001 L BNN "PARTREV"
	1    5100 3800
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4400 3800 4200 3800
Wire Wire Line
	4200 3800 4200 3700
Wire Wire Line
	4200 3700 4050 3700
Wire Wire Line
	4400 3900 3550 3900
Wire Wire Line
	3550 3900 3550 3700
Wire Wire Line
	4400 4100 4200 4100
Wire Wire Line
	4200 4100 4200 4300
Wire Wire Line
	4200 4300 4050 4300
Wire Wire Line
	4400 4000 3550 4000
Wire Wire Line
	3550 4000 3550 4300
Wire Wire Line
	4400 3300 4200 3300
Wire Wire Line
	4200 3300 4200 3150
Wire Wire Line
	4200 3150 4000 3150
$Comp
L power:GNDREF #PWR0109
U 1 1 626671A7
P 3600 3150
F 0 "#PWR0109" H 3600 2900 50  0001 C CNN
F 1 "GNDREF" V 3700 3200 50  0000 R CNN
F 2 "" H 3600 3150 50  0001 C CNN
F 3 "" H 3600 3150 50  0001 C CNN
	1    3600 3150
	0    1    1    0   
$EndComp
$Comp
L power:GNDREF #PWR0110
U 1 1 6266E03A
P 6650 4700
F 0 "#PWR0110" H 6650 4450 50  0001 C CNN
F 1 "GNDREF" H 6655 4527 50  0000 C CNN
F 2 "" H 6650 4700 50  0001 C CNN
F 3 "" H 6650 4700 50  0001 C CNN
	1    6650 4700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6750 4700 6650 4700
Connection ~ 6650 4700
Wire Wire Line
	6550 4700 6650 4700
Wire Wire Line
	6150 4100 5800 4100
Wire Wire Line
	5800 4000 6150 4000
Wire Wire Line
	6150 3900 5800 3900
Wire Wire Line
	5800 3800 6150 3800
Wire Wire Line
	7350 4000 7150 4000
Wire Wire Line
	7150 3900 7900 3900
Wire Wire Line
	7900 3800 7150 3800
Wire Wire Line
	7150 3700 7350 3700
$Comp
L MCU_Module:Arduino_Leonardo A1
U 1 1 625E82E6
P 6650 3600
F 0 "A1" H 6650 4781 50  0000 C CNN
F 1 "Arduino_Leonardo" H 6650 4690 50  0000 C CNN
F 2 "Module:Arduino_UNO_R3" H 6650 3600 50  0001 C CIN
F 3 "https://www.arduino.cc/en/Main/ArduinoBoardLeonardo" H 6650 3600 50  0001 C CNN
	1    6650 3600
	1    0    0    -1  
$EndComp
$EndSCHEMATC