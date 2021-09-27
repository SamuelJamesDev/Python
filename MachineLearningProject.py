# this project was made to analyze school grades and return with 80% accuracy students who may be at risk to fail classes

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression 
from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

uploaded = files.upload()

import_file = pd.read_csv("student-mat.csv", delimiter=';')

file_np = np.asarray(import_file).T
unclean_features = file_np[0 : 30]
unclean_target = np.asarray(file_np[30 : 34])

import_file.head()

# Make lists of the possible attributes for each feature
school = ["GP", "MS"]
sex = ["F", "M"]
address = ["U", "R"]
famsize = ["GT3", "LE3"]
pstatus = ["A", "T"]
parent_job = ["teacher", "other", "services", "at_home", "health"]
reason = ["course", "other", "home", "reputation"]
guardian = ["mother", "father", "other"]
yesORno = ["no", "yes"]

features = np.array([])
target = np.array([])

#-------------------------------------------------------------------------------------
# This function converts the string array from dataset to a readable integer array
#-------------------------------------------------------------------------------------
def ConvertStringToIntInFile(unclean_feature, attribute):
  return_array = np.array([])
  for j in range(len(unclean_feature)):
    match = False
    for i in range(len(attribute)):
      if (unclean_feature[j] == attribute[i]):
        match = True
        return_array = np.append(return_array, attribute.index(attribute[i]))
    if match == False:
      print(unclean_feature[j])
  return return_array

# Take each feature and convert it to a integer array and append it to features
features = np.append(features, ConvertStringToIntInFile(unclean_features[0], school))
features = np.append(features, ConvertStringToIntInFile(unclean_features[1], sex))
features = np.append(features, unclean_features[2])
features = np.append(features, ConvertStringToIntInFile(unclean_features[3], address))
features = np.append(features, ConvertStringToIntInFile(unclean_features[4], famsize))
features = np.append(features, ConvertStringToIntInFile(unclean_features[5], pstatus))
features = np.append(features, unclean_features[6])
features = np.append(features, unclean_features[7])
features = np.append(features, ConvertStringToIntInFile(unclean_features[8], parent_job))
features = np.append(features, ConvertStringToIntInFile(unclean_features[9], parent_job))
features = np.append(features, ConvertStringToIntInFile(unclean_features[10], reason))
features = np.append(features, ConvertStringToIntInFile(unclean_features[11], guardian))
features = np.append(features, unclean_features[12])
features = np.append(features, unclean_features[13])
features = np.append(features, unclean_features[14])
features = np.append(features, ConvertStringToIntInFile(unclean_features[15], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[16], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[17], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[18], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[19], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[20], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[21], yesORno))
features = np.append(features, ConvertStringToIntInFile(unclean_features[22], yesORno))
features = np.append(features, unclean_features[23])
features = np.append(features, unclean_features[24])
features = np.append(features, unclean_features[25])
features = np.append(features, unclean_features[26])
features = np.append(features, unclean_features[27])
features = np.append(features, unclean_features[28])
features = np.append(features, unclean_features[29])

# Append all targets to a single target array 
target = np.append(target, unclean_target[0])
target = np.append(target, unclean_target[1])
target = np.append(target, unclean_target[2])

# Reshape arrays to be readable by the sklearn functions
features = features.reshape(30, 395)
target = target.reshape(3, 395)

# Split data randomly into a train set and test set for features and target G1
X_train, X_test_g1, y_train, y_test_g1 = train_test_split(features.T, target[0], test_size=0.20, random_state=80)

# Use sklearn linear regression to make model for dataset with respect to G1
reg = LinearRegression().fit(X_train, y_train)

# Use model made to predict the test set and return the predictions make by sklearn predict funciton
prediction_g1 = reg.predict(X_test_g1)


# Split data randomly into a train set and test set for features and target G2
X_train, X_test_g2, y_train, y_test_g2 = train_test_split(features.T, target[1], test_size=0.20, random_state=80)

# Use sklearn linear regression to make model for dataset with respect to G2
reg = LinearRegression().fit(X_train, y_train)

# Use model made to predict the test set and return the predictions make by sklearn predict funciton
prediction_g2 = reg.predict(X_test_g2)



# Split data randomly into a train set and test set for features and target G3
X_train, X_test_g3, y_train, y_test_g3 = train_test_split(features.T, target[2], test_size=0.20, random_state=80)

# Use sklearn linear regression to make model for dataset with respect to G3
reg = LinearRegression().fit(X_train, y_train)

# Use model made to predict the test set and return the predictions make by sklearn predict funciton
prediction_g3 = reg.predict(X_test_g3)

# Normalize data
y_test_g1_max = max(y_test_g1)
y_test_g2_max = max(y_test_g2)
y_test_g3_max = max(y_test_g3)
norm_prediction_g1 = prediction_g1 / y_test_g1_max
norm_prediction_g2 = prediction_g2 / y_test_g2_max
norm_prediction_g3 = prediction_g3 / y_test_g3_max
norm_y_test_g1 = y_test_g1 / y_test_g1_max
norm_y_test_g2 = y_test_g2 / y_test_g2_max
norm_y_test_g3 = y_test_g3 / y_test_g3_max

mean_pred_g1 = [sum(norm_y_test_g1) / len(norm_y_test_g1) for i in range(79)]
mean_pred_g2 = [sum(norm_y_test_g2) / len(norm_y_test_g2) for i in range(79)]
mean_pred_g3 = [sum(norm_y_test_g3) / len(norm_y_test_g3) for i in range(79)]
mean_pred_g1 = np.asarray(mean_pred_g1)
mean_pred_g2 = np.asarray(mean_pred_g2)
mean_pred_g3 = np.asarray(mean_pred_g3)


#-------------------------------------------------------------------------------------
# This function calculates the RMSE based on each prediction array and test set
#-------------------------------------------------------------------------------------
def GetRMSE(pred, actual):
  m = len(pred)
  return ((1/m) * np.sum((pred - actual)**2))**(1/2)
  
# Print the RMSE for each prediction with respect to its test set
print(f'RMSE of G1: {GetRMSE(norm_prediction_g1, norm_y_test_g1)}')
print(f'RMSE of G2: {GetRMSE(norm_prediction_g2, norm_y_test_g2)}')
print(f'RMSE of G3: {GetRMSE(norm_prediction_g3, norm_y_test_g3)}')
print(f'RMSE of G1 with Mean prediction: {GetRMSE(mean_pred_g1, norm_y_test_g1)}')
print(f'RMSE of G2 with Mean prediction: {GetRMSE(mean_pred_g2, norm_y_test_g2)}')
print(f'RMSE of G3 with Mean prediction: {GetRMSE(mean_pred_g3, norm_y_test_g3)}')


# Random numbers RMSE for reference
import random as rn
rmse_averages_g1 = []
rmse_averages_g2 = []
rmse_averages_g3 = []
for j in range(1000):
  random_numbers = []
  for i in range(79):
    random_numbers.append(rn.randint(0, 20))
  random_numbers = np.asarray(random_numbers)
  norm_random_numbers_g1 = random_numbers / y_test_g1_max
  norm_random_numbers_g2 = random_numbers / y_test_g2_max
  norm_random_numbers_g3 = random_numbers / y_test_g3_max
  rmse_averages_g1.append(GetRMSE(norm_random_numbers_g1, norm_y_test_g1))
  rmse_averages_g2.append(GetRMSE(norm_random_numbers_g2, norm_y_test_g2))
  rmse_averages_g3.append(GetRMSE(norm_random_numbers_g3, norm_y_test_g3))


print(f'RMSE of G1 with Random Predictions: {sum(rmse_averages_g1) / len(rmse_averages_g1)}')
print(f'RMSE of G2 with Random Predictions: {sum(rmse_averages_g2) / len(rmse_averages_g2)}')
print(f'RMSE of G3 with Random Predictions: {sum(rmse_averages_g3) / len(rmse_averages_g3)}')

# R2 calculation
def GetR2(pred, actual):
  sst = np.sum((actual - np.mean(actual)**2))
  ssr = np.sum((actual - pred)**2)
  return 1 - (ssr / sst)

# Random numbers R2 for reference
r2_averages_g1 = []
r2_averages_g2 = []
r2_averages_g3 = []
for j in range(1000):
  random_numbers = []
  for i in range(79):
    random_numbers.append(rn.randint(0, 20))
  random_numbers = np.asarray(random_numbers)
  norm_random_numbers_g1 = random_numbers / y_test_g1_max
  norm_random_numbers_g2 = random_numbers / y_test_g2_max
  norm_random_numbers_g3 = random_numbers / y_test_g3_max
  r2_averages_g1.append(GetR2(norm_random_numbers_g1, norm_y_test_g1))
  r2_averages_g2.append(GetR2(norm_random_numbers_g2, norm_y_test_g2))
  r2_averages_g3.append(GetR2(norm_random_numbers_g3, norm_y_test_g3))
  

print(f'R2 of G1: {GetR2(norm_prediction_g1, norm_y_test_g1)}')
print(f'R2 of G2: {GetR2(norm_prediction_g2, norm_y_test_g2)}')
print(f'R2 of G3: {GetR2(norm_prediction_g3, norm_y_test_g3)}')
print(f'R2 of G1 with Mean prediction: {GetR2(mean_pred_g1, norm_y_test_g1)}')
print(f'R2 of G2 with Mean prediction: {GetR2(mean_pred_g2, norm_y_test_g2)}')
print(f'R2 of G3 with Mean prediction: {GetR2(mean_pred_g3, norm_y_test_g3)}')
print(f'R2 of G1 with Random Predictions: {sum(r2_averages_g1) / len(r2_averages_g1)}')
print(f'R2 of G2 with Random Predictions: {sum(r2_averages_g2) / len(r2_averages_g2)}')
print(f'R2 of G3 with Random Predictions: {sum(r2_averages_g3) / len(r2_averages_g3)}')

# change target data to be based on (above mean in target == 1 below mean in target == 0)
class_target_g1 = target[0]
class_target_g2 = target[1]
class_target_g3 = target[2]
for i in range(len(class_target_g1)):
  if (class_target_g1[i] / (sum(class_target_g1) / len(class_target_g1)) > 1):
    class_target_g1[i] = 1.0
  else:
    class_target_g1[i] = 0.0
for i in range(len(class_target_g2)):
  if (class_target_g2[i] / (sum(class_target_g2) / len(class_target_g2)) > 1):
    class_target_g2[i] = 1.0
  else:
    class_target_g2[i] = 0.0
for i in range(len(class_target_g3)):
  if (class_target_g3[i] / (sum(class_target_g3) / len(class_target_g3)) > 1):
    class_target_g3[i] = 1.0
  else:
    class_target_g3[i] = 0.0

class_target_g1 = np.asarray(class_target_g1).astype(float)
class_target_g2 = np.asarray(class_target_g2).astype(float)
class_target_g3 = np.asarray(class_target_g3).astype(float)

X_train, X_test_g1, y_train_log, y_test_g1_log = train_test_split(features.T, class_target_g1, test_size=0.20, random_state=80)
log = LogisticRegression(max_iter=1000).fit(X_train, y_train_log)
prediction_g1_log = log.predict(X_test_g1)

X_train, X_test_g1, y_train_log, y_test_g2_log = train_test_split(features.T, class_target_g2, test_size=0.20, random_state=80)
log = LogisticRegression(max_iter=1000).fit(X_train, y_train_log)
prediction_g2_log = log.predict(X_test_g2)

X_train, X_test_g1, y_train_log, y_test_g3_log = train_test_split(features.T, class_target_g3, test_size=0.20, random_state=80)
log = LogisticRegression(max_iter=1000).fit(X_train, y_train_log)
prediction_g3_log = log.predict(X_test_g3)

def GetAccuracy(pred, actual):
  acc = 0
  for i in range(len(pred)):
    if pred[i] == actual[i]:
      acc += 1
  
  return acc / len(pred)

print(f'G1 Model Accuracy is: {GetAccuracy(prediction_g1_log, y_test_g1_log)}')
print(f'G2 Model Accuracy is: {GetAccuracy(prediction_g2_log, y_test_g2_log)}')
print(f'G3 Model Accuracy is: {GetAccuracy(prediction_g3_log, y_test_g3_log)}')
