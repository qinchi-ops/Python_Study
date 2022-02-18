#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

department1='Security'
department2='Python'
depart1_m='cq_bomb'
depart2_m='qinke'
COURSE_FEES_SEC=456789.123465
COURSE_FEES_Python=1234.3456

#需要的输出信息
#line1= Department1 name:Security  Manager:cq_bomb  COURSE FEES:456789.12  The End!
#line2= Department2 name:Python    Manager:qinke    COURSE FEES:1234.34    The End!

#方法1
# line1='Department1 name:%-10s Manger:%-10s COURSE FEES:%-10.2f The End!'   % (department1,depart1_m,COURSE_FEES_SEC)
# line2='Department2 name:%-10s Manger:%-10s COURSE FEES:%-10.2f The End!'   % (department2,depart2_m,COURSE_FEES_Python)

#方法2
# line1= 'Department1 name:{:<10}Manager:{:<10}COURSE FEES:{:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
# line2= 'Department2 name:{:<10}Manager:{:<10}COURSE FEES:{:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)

#方法3
#tmp1='Department1 name:{:<10}Manager:{:<10}COURSE FEES:{:<10.2f} The End!'
#tmp2='Department1 name:{:<10}Manager:{:<10}COURSE FEES:{:<10.2f} The End!'
# line1 = (tmp1.format(department1,depart1_m,COURSE_FEES_SEC))
# line2 = (tmp2.format(department2,depart2_m,COURSE_FEES_Python))



#方法4
line1 = f'Department1 name:{department1:<10}Manager:{depart1_m:<10}COURSE FEES:{COURSE_FEES_SEC:<10.2f} The End!'
line2 = f'Department2 name:{department2:<10}Manager:{depart2_m:<10}COURSE FEES:{COURSE_FEES_Python:<10.2f} The End!'


#length = len(tmp1) #测试的过程，自己保留，方便复习查看
length = len(line1)
print('='*length)
#print (tmp1.format(department1,depart1_m,COURSE_FEES_SEC))#测试的过程，自己保留，方便复习查看
print(line1)
print(line2)
print('='*length)

