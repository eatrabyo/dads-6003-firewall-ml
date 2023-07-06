# DADS 6003 - Applied Machine Learning: Internet Firewall Data Machine Learning Project.

## 1. Intro
## 2. EDA
### 2.1 Exploratory of Action
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/14e928be-6b5d-4c9b-a293-6650c66f0ac3)

Target distribution is imbalance data because "allow" is too high and "reset-both" is very rare. Especially "reset-both" will be hard to predict

### 2.2 Exploratory of Packets&Elapsed Time
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/fe613afd-16ea-499e-bc6b-f9029b5b98d3)

Graph between Action and Elapsed time
กราฟแสดงให้เห็นว่า ค่า action "deny", "drop" มีค่า elapsed time เท่ากับ 0 ส่วน "reset-both" มีค่าระหว่าง 0 และ 1
จากข้อมูลที่มีสามารถอนุมานได้ว่า หาก elapsed time มีค่ามากกว่า 1 จะเป็น action "allow"

![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/6b316a44-0cbc-4294-afc8-f5d99bfe3239)

Graph between Action and Packets
กราฟแสดงให้เห็นว่า ค่า action "deny", "drop" จำนวน packets เท่ากับ 1 ส่วน "reset-both" มีจำนวนระหว่าง 1 และ 4
จากข้อมูลที่มีสามารถอนุมานได้ว่า หาก packets มีค่ามากกว่า 4 จะเป็น action "allow"

### 2.3 Exploratory of Numerical Features
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/d6fbc54f-7571-4640-94c6-7f547346b903)
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/3cbfb86a-4c2d-46d9-bc0d-9e84bdf64a62)
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/8822c9dc-b78a-4cee-85a3-66aed81f7844)
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/25a04616-30a9-481c-8034-1b276365d87b)
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/e3b2c28e-970c-4d38-bcf3-eed3ce826dd0)
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/e97bea72-2b26-442c-9a87-e926bdbc7fc2)
![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/6e1effb9-db09-4e22-963e-44c774b2fcff)

จากกราฟด้านบนจะเห็นว่าการกระจายตัวของข้อมูล Numerical Features ไม่เป็น normal distribution

### 2.3 Exploratory of Categorical Features

![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/864db275-7d85-4be0-b444-e6ab30fa35b7)

crosstable between action and port(source port and destination port) by using top 10 levels only
จะเห็นว่า port ส่งผลกระทบต่อ action อย่างมีนัยยะสำคัญ ยกตัวอย่างเช่น
  -source port : 58638 ส่งผลกระทบต่อ action "allow"
  -destination port : 445 ส่งผลกระทบต่อ action "drop"

![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/f64af375-4635-4ac1-9b5b-ff821e12a9fc)

crosstable between action and port(NAT source port and NAT destination port) by using top 10 levels only
จะเห็นว่า NAT source port ส่งผลกระทบไม่แน่นอน แต่ในทางกลับกัน NAT destination port ส่งผลกระทบต่อ action อย่างมีนัยยะสำคัญ ยกตัวอย่างเช่น
  -NAT destination port : 53 ส่งผลกระทบต่อ action "allow"

![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/94fbdd5e-4ade-4899-9f21-a3a408dfb735)

graph between source port and destination port each action
ในส่วนของ action drop มีแพทเทิร์นที่ค่อนข้างชัดเจน

![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/097b67e3-f277-4a0b-8306-e71117125961)

graph between NAT source port and NAT destination port each action


## 3. Machine Learning Algorithm
### 3.1 Tuning Hyperparameter

## 4. Evaluation
### 4.1 Plotting Learning Curve
### 4.2 F1-Score

## Contributors
* Itthisak Pratukaew
* Nattasorn Tanpichai
* Pinyawat Sabsanhor
* Patchadol Ratanapittayaruk
* Suthida Jumlongrasd

## Credits
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data#)
