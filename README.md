# DADS 6003 - Applied Machine Learning: Internet Firewall Data Machine Learning Project.

## 1. Introduction
This project is part of the DADS 6003 Applied Machine Learning subject. The objective is to analyze the provided data, construct machine-learning models using pipelines, and evaluate the outcomes. The data utilized in this project is collected from the UCI Machine Learning Repository and consists of internet traffic records from UCI's firewall.

There are 12 features in the dataset, which include:
  * Source Port
  * Destination Port
  * NAT Source Port
  * NAT Destination Port
  * Action
  * Bytes
  * Bytes Sent
  * Bytes Received
  * Packets
  * Elapsed Time (sec)
  * pkts_sent (Packets Sent)
  * pkts_received (Packets Received)
  
## 2. EDA
### 2.1 Action
|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/14e928be-6b5d-4c9b-a293-6650c66f0ac3)
|:--:| 
| *Fig. 1: Histogram of Action* |


The target variable in this project is the "action," which consists of four categories: "allow," "drop," "deny," and "reset-both." As depicted in Figure 1, the distribution of the action data is imbalanced. The most frequently occurring action is "allow" with a frequency of 37,640, while the least frequent action is "reset-both" with a count of 54.

### 2.2 Packets & Elapsed Time
|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/fe613afd-16ea-499e-bc6b-f9029b5b98d3)
|:--:| 
| *Fig. 2: Histogram between Action and Elapsed Time* |

According to Figure 2, it can be observed that the "deny" and "drop" actions have an elapsed time of 0, while the "reset-both" action has values between 0 and 1. Based on this observation, we can assume that if the elapsed time is greater than 1, the corresponding action would be "allow."

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/6b316a44-0cbc-4294-afc8-f5d99bfe3239)
|:--:| 
| *Fig. 3: Histogram between Action and Packets)* |

According to Figure 3, it can be observed that both the "deny" and "drop" actions have a packet count of 1. On the other hand, the "reset-both" action exhibits values ranging between 1 and 4. Based on this observation, we can make an assumption that the "allow" action would typically have a packet count greater than 4.

### 2.3 Numerical Features
|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/d6fbc54f-7571-4640-94c6-7f547346b903)
|:--:| 
| *Fig. 4: Histogram of Bytes*|

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/3cbfb86a-4c2d-46d9-bc0d-9e84bdf64a62)
|:--:| 
| *Fig. 5: Histogram of Bytes Sent*|

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/8822c9dc-b78a-4cee-85a3-66aed81f7844)
|:--:| 
| *Fig. 6: Histogram of Bytes Received* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/25a04616-30a9-481c-8034-1b276365d87b)
|:--:| 
| *Fig. 7: Histogram of Packets* |
 
|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/e3b2c28e-970c-4d38-bcf3-eed3ce826dd0)
|:--:| 
| *Fig. 8: Histogram of Elapsed Time* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/e97bea72-2b26-442c-9a87-e926bdbc7fc2)
|:--:| 
| *Fig. 9: Histogram of Packets Sent* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/6e1effb9-db09-4e22-963e-44c774b2fcff)
|:--:| 
| *Fig. 10: Histogram of Packets Received*|

The figures indicate that none of the seven features exhibit a normal distribution.

### 2.3 Exploratory of Categorical Features

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/864db275-7d85-4be0-b444-e6ab30fa35b7)
|:--:| 
| *Fig. 11:*|

crosstable between action and port(source port and destination port) by using top 10 levels only
จะเห็นว่า port ส่งผลกระทบต่อ action อย่างมีนัยยะสำคัญ ยกตัวอย่างเช่น
  -source port : 58638 ส่งผลกระทบต่อ action "allow"
  -destination port : 445 ส่งผลกระทบต่อ action "drop"

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/f64af375-4635-4ac1-9b5b-ff821e12a9fc)
|:--:| 
| *Fig. 12:* |

crosstable between action and port(NAT source port and NAT destination port) by using top 10 levels only
จะเห็นว่า NAT source port ส่งผลกระทบไม่แน่นอน แต่ในทางกลับกัน NAT destination port ส่งผลกระทบต่อ action อย่างมีนัยยะสำคัญ ยกตัวอย่างเช่น
  -NAT destination port : 53 ส่งผลกระทบต่อ action "allow"

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/94fbdd5e-4ade-4899-9f21-a3a408dfb735)
|:--:| 
| *Fig. 13* |

graph between source port and destination port each action
ในส่วนของ action drop มีแพทเทิร์นที่ค่อนข้างชัดเจน

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/097b67e3-f277-4a0b-8306-e71117125961)
|:--:| 
| *Fig. 14* |

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
