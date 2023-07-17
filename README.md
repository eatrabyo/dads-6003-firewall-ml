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
### 2.1 Target Variable
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
| *Fig. 3: Histogram between Action and Packets* |

According to Figure 3, it can be observed that both the "deny" and "drop" actions have a packet count of 1. On the other hand, the "reset-both" action exhibits values ranging between 1 and 4. Based on this observation, we can make an assumption that the "allow" action would typically have a packet count greater than 4.

### 2.3 Other Numerical Features
|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/d6fbc54f-7571-4640-94c6-7f547346b903)
|:--:| 
| *Fig. 4: Histogram of Bytes* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/3cbfb86a-4c2d-46d9-bc0d-9e84bdf64a62)
|:--:| 
| *Fig. 5: Histogram of Bytes Sent* |

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
| *Fig. 10: Histogram of Packets Received* |

Based on the figures presented, it is evident that none of the seven features follow a normal distribution. As a result, we will employ the robust scaler to transform the data. This scaling method is suitable because it is not affected by outliers, allowing us to mitigate their influence on the data.

### 2.3 Categorical Features

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/864db275-7d85-4be0-b444-e6ab30fa35b7)
|:--:| 
| *Fig. 11: Frequential Heatmap between action and ports(source port and destination port)*|

Upon examining the top 10 most frequent instances in the data, we can clearly observe the significant impact of ports on the resulting actions. For instance, when the source port is 58638, it usually leads to an "allow" action. On the other hand, a destination port of 445 often causes a "drop" action to be taken.

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/f64af375-4635-4ac1-9b5b-ff821e12a9fc)
|:--:| 
| *Fig. 12: Frequential Heatmap between action and ports(NAT source port and NAT destination port)* |

The NAT Source Port has an impact primarily on the "drop" and "deny" actions, whereas the NAT Destination Port has a significant influence on the overall "action". For instance, when the NAT destination port is set to 53, it consistently results in the "allow" action being taken.

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/94fbdd5e-4ade-4899-9f21-a3a408dfb735)
|:--:| 
| *Fig. 13: Scatterplot of Ports group by Action* |

While other actions seem to have random patterns across different ports, the "drop" action exhibits a noticeable pattern.


|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/114765725/097b67e3-f277-4a0b-8306-e71117125961)
|:--:| 
| *Fig. 14: Scatterplot of NAT Ports group by Action* |

Just like in Figure 13, Figure 14 also shows a clear pattern for the "drop" action in relation to NAT ports. This confirms that specific NAT ports have a noticeable impact on triggering the "drop" action.

Considering that the "allow" action is the most frequent and our focus is on identifying features that distinguish other actions, we have decided to exclude the source port variable. Consequently, we are left with the following six features:
1. Destination Port
2. NAT Source Port
3. NAT Destination Port
4. Packets
5. Elapsed Time (sec)
6. Bytes Received
   
### 2.4 Imbalanced Data
The action data exhibits an imbalanced distribution, with "allow" being the most frequently occurring action, appearing 37,640 times, while "reset-both" is the least frequent action.
The result "reset-both" is very low. so we focus on solution oversampling and combine (oversampling and undersampling).
1. SMOTETomek is a combination of two algorithms, Synthetic Minority Over-sampling Technique (SMOTE) and Tomek links. It is used to address the problem of imbalanced datasets in machine learning. SMOTE generates synthetic samples for the minority class, while Tomek links identify and remove overlapping samples from both the minority and majority classes, resulting in a balanced dataset.
2. SMOTEENN is another combination of algorithms used for dealing with imbalanced datasets. It combines SMOTE and Edited Nearest Neighbors (ENN) techniques. SMOTE generates synthetic samples for the minority class, and ENN removes samples from both classes that are misclassified by a classifier. SMOTEENN aims to achieve better performance by both oversampling the minority class and undersampling the majority class simultaneously.
3. RandomOverSampler is a simple technique for oversampling the minority class in an imbalanced dataset. It randomly selects samples from the minority class and replicates them until a balanced distribution is achieved.
4. SMOTE is a popular oversampling technique used to address class imbalance. It works by generating synthetic samples for the minority class based on the feature space. SMOTE selects a sample from the minority class, identifies its k nearest neighbors, and then creates new samples along the line segments connecting the original sample and its neighbors.

## 3. Machine Learning Algorithm
We picked 4 machine learning algorithms( Random Forest, K-Nearest Neighbors, XG Boost, and Decision Tree) for this firewall data.

### 3.1 Tuning Hyperparameter
We are utilizing GridSearchCV with 5-fold cross-validation to tune the hyperparameters, which can be time-consuming depending on the specified hyperparameter inputs.
Here is the list of hyperparameters we focused on for each model:
  1. Random Forest
     * n_estimators
     * max_depth
     * min_samples_split
     * min_samples_leaf
  2. K-Nearest Neighbors
     * n_neighbors
     * weights
     * algorithm
  3. XG Boost
     * object
     * num_class
     * eval_metric
  4. Decision Tree
     * criterion
     * splitter
     * max_depth
     * min_samples_split
     * max_features

## 4. Evaluation
Once we have obtained the best hyperparameters for each model, we will evaluate their performance using the learning curve and compare the F1 Score.

### 4.1 Plotting Learning Curve
The code for plotting the learning curve.

```
train_sizes, train_scores, test_scores = learning_curve(pipe, x_train, y_train, cv=5, scoring='f1_macro')

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(10, 5))
plt.xlabel("Training examples")
plt.ylabel("F1-macro Score")

plt.grid(b=True, which='major', color='b', linestyle='-')

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                    train_scores_mean + train_scores_std, alpha=0.1,
                    color="r")
plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                    test_scores_mean + test_scores_std, alpha=0.1, color="g")
plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
            label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
            label="Cross-validation score")

plt.legend(loc="best")
```

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/92035314/4c5a7631-9ebe-4651-a018-a3f36b2d0cbc)
|:--:| 
| *Fig. 15: Learning Curve of Random Forest* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/92035314/41f62b5d-92aa-442b-ab67-c74f46b7e2cb)
|:--:| 
| *Fig. 16: Learning Curve of K-Nearest Neighbors* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/92035314/a923cc77-e34c-4a18-a58e-b8dd9b0ede93)
|:--:| 
| *Fig. 17: Learning Curve of XG Boost* |

|![image](https://github.com/eatrabyo/dads-6003-firewall-ml/assets/92035314/e9433858-cc36-4fc6-a5d8-9d06ed0a902a)
|:--:| 
| *Fig. 18: Learning Curve of Decision Tree* |

### 4.2 F1 Score

|**Models**|**Random Forest**|**K-Nearest Neighbors**|**XG Boost**|**Decision Tree**|
|---|:---:|:---:|:---:|:---:|
|**F1 Train**|_0.8760_|_0.9774_|__0.9780__|_0.9231_|
|**F1 Test**|*0.7345*|__0.7942__|*0.7795*|*0.7437*|

We evaluated the model accuracy using the F1 Score metric. Among the models, XG Boost achieved the highest training score, while K-Nearest Neighbors obtained the highest test score. However, it is essential to note that the scores displayed may not reflect the actual performance of the models.
To obtain a more reliable assessment of performance, we will conduct cross-validation. This approach allows us to estimate the average performance of the models across multiple folds, providing a better understanding of their generalization capabilities. 

### 4.3 Cross Validation

|**Models**|**Random Forest**|**K-Nearest Neighbors**|**XG Boost**|**Decision Tree**|
|---|:---:|:---:|:---:|:---:|
|**CV Score**|_0.8759_|_0.9678_|__0.9690__|_0.9234_|
|**SD**|*0.0018*|*0.0074*|*0.0081*|*0.006*|

Using 5-fold cross-validation and the F1 score as the evaluation metric, we determined that XG Boost achieved the highest cross-validated score, followed closely by K-Nearest Neighbors. The slight difference in scores between these two models indicates their suitability for this specific type of data. Based on these findings, we can conclude that both XG Boost and K-Nearest Neighbors are well-suited models for our task.

## Contributors
* Itthisak Pratukaew
* Nattasorn Tanpichai
* Patchadol Ratanapittayaruk
* Pinyawat Sabsanhor
* Suthida Jumlongrasd

## Credits
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data#)
