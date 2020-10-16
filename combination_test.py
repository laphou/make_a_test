# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import itertools
import csv
import sys
from subprocess import STDOUT
# from tqdm import tqdm

df=pd.read_csv('test_data.csv')
df=df[['N1','N2','N3','N4','N5','N6','special']]
df=df.rename(columns={"N1": "1", "N2": "2","N3": "3","N4": "4","N5": "5","N6": "6","special": "7"})
df

# df = df[:-1]

# df_target=df[-100:]
df_target=df

df=df[['1','2','3','4','5','6']]

# df_history=df[:-100]
# df=df[:-100]
df

df2=df.values.tolist()

df_target=df_target.values.tolist()

def count_consec(listrand):
    count=1
    consec_list=[]
    for i in range(len(listrand[:-1])):
        if listrand[i]+1 == listrand[i+1]:
            count+=1
        else:
            consec_list.append(count)
            count=1

    # Account for the last iteration
    consec_list.append(count)     

    return consec_list

count_six=0
count_five=0
count_four=0
for i in range(1,3):
  print(i)
  previous=df_target[-(i+1)]
  target=df_target[-i]
  previous2=df2[-(i+1)]
  target2=df2[-i]
  df2.remove(previous2)
  df2.remove(target2)  
  # stuff = [49,22,9,30,28,1,4,10,24,33,20,16,35,48,34,13,21,42,6,14,32,45,40,7,12,3,44,18,17,31,2,29,43,11,23,37,38,5,39,15,26,36,46,8,25,47,27,41,19]
  stuff = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
# 不要最後7個出現率低的號碼
  # stuff = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,47,48,49]
# 不要最後13個出現率低的號碼
# stuff = [1,2,4,5,6,7,8,9,10,12,13,14,16,17,18,20,21,22,24,28,29,30,31,32,33,34,35,36,37,38,40,42,43,45,48,49]
# 不要最後19個出現率低的號碼
# stuff = [1,3,4,6,7,9,10,12,13,14,16,17,18,20,21,22,24,28,30,31,32,33,34,35,40,42,44,45,48,49]
  L=6
  count=0
  count2=0
  # previous = [9, 21, 26, 27, 28, 48, 45]
  red = [1, 2, 7, 8, 12, 13, 18, 19, 23, 24, 29, 30, 34, 35, 40, 45, 46]
  blue = [3, 4, 9, 10, 14, 15, 20, 25, 26, 31, 36, 37, 41, 42, 47, 48]
  green = [5, 6, 11, 16, 17, 21, 22, 27, 28, 32, 33, 38, 39, 43, 44, 49]
  range_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  range_10 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  range_20 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
  range_30 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
  range_40 = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
  repeat=[]
  item_list=[]
  for item in itertools.combinations(stuff, L):
      diff = item[5] - item[0]
      bad_begin_end = 0
      prefix_bad_counter = 0
      bad_range = 0
      sum_counter = 0
      even_bad_counter = 0
      bad_diff = 0
      even_counter = 0
      rbg_counter = 0
      listOfElems = []
      listOfElems2 = []
      if len(set(item) & set(repeat))>1:
        continue
      if sum(item)<=90 or sum(item)>=210:
        # p="bad sum"
        continue
        # sum_counter += 1
      else:
        if len(set(item) & set(range_0)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(range_10)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(range_20)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(range_30)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(range_40)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(red)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(blue)) > 3:
          # rbg_counter += 1
          continue
        if len(set(item) & set(green)) > 3:
          # rbg_counter +=1
          continue
        if diff<32 or diff>47:
          # p="bad diff"
          continue
          # bad_diff += 1
        else:
          for num in item:
              if num % 2 == 0:
                  even_counter += 1
              listOfElems += [num%10]
              listOfElems2 += [num/10]
          thefirst = item[0]
          thelast = item[5]
          if even_counter > 4 or even_counter < 2:
            # p="bad even"
            continue
            # even_bad_counter += 1
          else:
            def getDuplicatesWithCount(listOfElems):
                dictOfElems = dict()
                for elem in listOfElems:
                    if elem in dictOfElems:
                        dictOfElems[elem] += 1
                    else:
                        dictOfElems[elem] = 1
                dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
                return dictOfElems
            dictOfElems = getDuplicatesWithCount(listOfElems)
            for key, value in dictOfElems.items():
                if value >= 4:
                    # p="Bad guess"
                    continue
                elif value >= 3:
                    # prefix_bad_counter += 1
                    continue
            def getDuplicatesWithCount2(listOfElems2):
                dictOfElems2 = dict()
                for elem in listOfElems2:
                    if elem in dictOfElems2:
                        dictOfElems2[elem] += 1
                    else:
                        dictOfElems2[elem] = 1
                dictOfElems2 = { key:value for key, value in dictOfElems2.items() if value > 1}
                return dictOfElems2
            dictOfElems2 = getDuplicatesWithCount2(listOfElems2)
            for key, value in dictOfElems2.items():
                if value >= 4:
                    # p="Bad guess"
                    continue
                if value >= 3:
                    # bad_range += 1
                    continue
            if thefirst >= 15 or thelast <= 34:
                # p="bad begin or bad end"
                # bad_begin_end += 1
                continue
            # print(prefix_bad_counter, bad_range, bad_begin_end)
            # if sum_counter > 1 or even_bad_counter > 1 or bad_diff > 2 or rbg_counter > 2 or prefix_bad_counter > 1 or bad_range > 1 or bad_begin_end > 0:
            if sum_counter >0 or even_bad_counter > 0 or bad_diff > 0 or rbg_counter > 0 or prefix_bad_counter > 0 or bad_range > 0 or bad_begin_end > 0:
              # p="Bad guess"
              continue
            else:
              if max(count_consec(item)) >=3:
                continue
              elif min(count_consec(item)) >=2: 
                continue
              else:
                if len(set(item) & set(previous))>1:
                  p="too much repeat"
                else:
                  # count=count+1
                  repeat_counter=0
                  zero_count=0
                  one_count=0
                  two_count=0
                  three_count=0
                  four_count=0
                  for i in range(len(df2)):
                    if len(set(item) & set(df2[i]))>4:
                      p="too much repeat"
                      repeat_counter=1
                      continue
                    if len(set(item) & set(df2[i]))==4:
                      four_count=four_count+1
                      if four_count>10:
                        p="too much repeat" 
                        repeat_counter=1                 
                        continue
                    if len(set(item) & set(df2[i]))==0:
                      zero_count=zero_count+1  
                      if zero_count>1213:
                        p="too much repeat"
                        repeat_counter=1                  
                        continue
                    #   # if zero_count<800:
                    #   #   p="too less repeat"
                    #   #   repeat_counter=1                  
                    #   #   break
                    if len(set(item) & set(df2[i]))==1:
                      one_count=one_count+1
                      if one_count>1163:
                        p="too much repeat"  
                        repeat_counter=1                
                        continue
                    #   # if one_count<1000:
                    #   #   p="too less repeat"
                    #   #   repeat_counter=1                  
                    #   #   break
                    if len(set(item) & set(df2[i]))==2:
                      two_count=two_count+1
                      if two_count>406:
                        p="too much repeat"                  
                        repeat_counter=1
                        continue               
                    if len(set(item) & set(df2[i]))==3:
                      three_count=three_count+1 
                      if three_count>68:
                        p="too much repeat"                  
                        repeat_counter=1
                        continue
                  if repeat_counter==0:
                    count=count+1
                    # print(zero_count,one_count,two_count,three_count,four_count)
                    # print(item)
                  if repeat_counter==0 and zero_count>=1042 and one_count>=986 and two_count>=280 and three_count>=25:
                    count2=count2+1
                    # print(zero_count,one_count,two_count,three_count,four_count,count2)
                    # print(item)
                    # repeat.extend(item)
                    item_list.append(item)
                    repeat = item
  count_hit=0
  for item in item_list:
    # print (len(set(item) & set(target)))
    if len(set(item) & set(target)) == 6:
      count_hit=count_hit+1
      count_six=count_six+1
      print(len(set(item) & set(target)))
    elif len(set(item) & set(target)) == 5:
      count_hit=count_hit+1
      count_five=count_five+1      
      print(len(set(item) & set(target)))      
    elif len(set(item) & set(target)) == 4:
      count_hit=count_hit+1
      count_four=count_four+1      
      print(len(set(item) & set(target)))
  # print(previous)
  # print(target)
  print("No of combination:", count2)
  print("Hit:", count_hit)
  print('=============================')
print("Hit Six:",count_six)
print("Hit Five:",count_five)
print("Hit Four:",count_four)
# print('---------------------')
# print(count_hit)
# print('----------------------------------------------------------------------')                
# print(count)
# print(count2)