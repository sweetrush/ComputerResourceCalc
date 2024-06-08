# 
# About this Program 
# Developed by SweetRushCoder 
# 
# NAME: Computer Resource Calc 
# PURPOSE: This small program is used to find out the resources that a Application
#          might need when the number of users and other elements are changed 
#          in the program. 
#  Date of Inital Development: June 08 2024
# 


import streamlit as st
import math as ma

# What resources will a user have :

# storeage
# Memory

# use per day
# 4 hours storge
# 8 Hours storge
# 16 Hours  storge

# Server Specification
# Storage 500GB
# Memory 16GB

### Function Area


# total Average Storage per day = [Number of Users] * [Storage for 1 User per day]
def total_average_storage_per_day(Number_of_Users):
    return int(Number_of_Users) * 5


# total Storage per 4 hours =  [Number of Users] * [Storage for 1 User per day] * 4
def total_storage_per_fourhours(Number_of_Users, storage_user):
    return float(int(Number_of_Users) * float(storage_user) * 4)


# total Storage per 8 hours =  [Number of Users] * [Storage for 1 User per day] * 8
def total_storage_per_eighthours(Number_of_Users, storage_user):
    return float(int(Number_of_Users) * float(storage_user) * 8)


# total Storage per 4 hours =  [Number of Users] * [Storage for 1 User per day] * 16
def total_storage_per_sixteenhours(Number_of_Users, storage_user):
    return float(int(Number_of_Users) * float(storage_user) * 16)


# total total Memory = [Number of Users] * [Memory  for 1 User per day]
def total_memory_per_day(Number_of_Users, memory_user):
    return ma.ceil(float(int(Number_of_Users) * float(memory_user)))


def numberofProcessingServers_16GB(memory):
    return ma.ceil(float(memory / 16))


def numberofProcessingServers_32GB(memory):
    return ma.ceil(float(memory / 32))


def numberofProcessingServers_64GB(memory):
    return ma.ceil(float(memory / 64))


def numberofProcessingServers_128GB(memory):
    return ma.ceil(float(memory / 128))


def numberofProcessingServers_256GB(memory):
    return ma.ceil(float(memory / 256))


# #####################################################
# #           Funcations for Storage Calc            ##
# #####################################################


def numberofStorageServers_500GB(Storage):
    return ma.ceil(float(Storage / 500))


def numberofStorageServers_1000GB(Storage):
    return ma.ceil(float(Storage / 1000))


def numberofStorageServers_1500GB(Storage):
    return ma.ceil(float(Storage / 1500))


def numberofStorageServers_2000GB(Storage):
    return ma.ceil(float(Storage / 2000))


# #####################################################
# #           Function for Text Formatting           ##
# #####################################################
#
def yellow_text(text):
    return ":yellow[" + text + "]"


def purple_text(text):
    return ":purple[" + text + "]"


def blue_text(text):
    return ":blue[" + text + "]"


def green_text(text):
    return ":green[" + text + "]"


def red_text(text):
    return ":red[" + text + "]"


# number of servers
# number of servers = [Total USER Storage  ]/ [Total Server Storage ]
# number of servers = [Total User Memory ]/ [Total Memory]

### End of Funcation area


# Start of the Display Areas of the Application

st.title(" 🖥 Miah's Compute Resources Calculator")

st.markdown("---", unsafe_allow_html=False)

c1, c2 = st.columns(2, gap="small")


c1.markdown(
    "#### ⚙ " + blue_text("Configuration") + " of Resources", unsafe_allow_html=True
)
c1.markdown("---", unsafe_allow_html=False)
# Display Area flow
numberofuser = c1.text_input(blue_text("Number of Users"), value="1", max_chars=None)
storage_per_user = c1.text_input(
    " 🐏 " + blue_text("Storage") + " per Users (GB)", value="1", max_chars=None
)
# storage_per_user_4hrs = c1.text_input("4Hr "+blue_text("Storage")+" per Users (GB)", value="1", max_chars=None)
# storage_per_user_8hrs = c1.text_input("8Hr "+blue_text("Storage")+" per Users (GB)", value="1", max_chars=None)
# storage_per_user_16hrs = c1.text_input("16Hr "+blue_text("Storage")+" per Users (GB)", value="1", max_chars=None)
memory_per_user = c1.text_input(
    " 💽 " + red_text("Memory") + " per Users (GB)", value="1", max_chars=None
)


c2.markdown(
    "#### ⚙ " + green_text("System Utilization") + " Needs", unsafe_allow_html=True
)
c2.markdown("---", unsafe_allow_html=False)
c2.write(
    "Total Average Storage per Day : "
    + str(total_average_storage_per_day(numberofuser))
    + "GB"
)
# c2.write("Total Storage for User per 4Hr : " + str(total_storage_per_fourhours(numberofuser, storage_per_user_4hrs))+"GB")
# c2.write("Total Storage for User per 8Hr : " + str(total_storage_per_eighthours(numberofuser, storage_per_user_8hrs))+"GB")
# c2.write("Total Storage for User per 16Hr : " + str(total_storage_per_sixteenhours(numberofuser, storage_per_user_16hrs))+"GB")
c2.write(
    "Total Memory per Day : "
    + str(total_memory_per_day(numberofuser, memory_per_user))
    + "GB"
)

c2.markdown("#### 💽 " + red_text("Storage Server") + " Needs", unsafe_allow_html=True)
c2.write(
    "Store Device 500GB: Count \t : "
    + str(numberofStorageServers_500GB(total_average_storage_per_day(numberofuser)))
)
c2.write(
    "Store Device 1000GB: Count \t : "
    + str(numberofStorageServers_1000GB(total_average_storage_per_day(numberofuser)))
)
c2.write(
    "Store Device 1500GB: Count \t : "
    + str(numberofStorageServers_1500GB(total_average_storage_per_day(numberofuser)))
)
c2.write(
    "Store Device 2000GB: Count \t : "
    + str(numberofStorageServers_2000GB(total_average_storage_per_day(numberofuser)))
)

c2.markdown(
    "#### 🐏 " + red_text("Processing Server") + " Needs", unsafe_allow_html=True
)
c2.write(
    "Server 16GB RAM: Count \t : "
    + str(
        numberofProcessingServers_16GB(
            total_memory_per_day(numberofuser, memory_per_user)
        )
    )
)
c2.write(
    "Server 32GB RAM: Count \t : "
    + str(
        numberofProcessingServers_32GB(
            total_memory_per_day(numberofuser, memory_per_user)
        )
    )
)
c2.write(
    "Server 64GB RAM: Count \t : "
    + str(
        numberofProcessingServers_64GB(
            total_memory_per_day(numberofuser, memory_per_user)
        )
    )
)
c2.write(
    "Server 128GB RAM: Count \t : "
    + str(
        numberofProcessingServers_128GB(
            total_memory_per_day(numberofuser, memory_per_user)
        )
    )
)
c2.write(
    "Server 256GB RAM: Count \t : "
    + str(
        numberofProcessingServers_256GB(
            total_memory_per_day(numberofuser, memory_per_user)
        )
    )
)

st.markdown("---", unsafe_allow_html=False)

cc1, cc2, cc3 = st.columns([2, 4, 4], gap="small")

cc1.markdown("##### " + green_text("Developed by:"))
cc2.markdown("[SweetRush Coder - sRC](https://suetenaloia.net)")
cc3.markdown("[Check out the Github-Project](https://github.com/sweetrush/ComputerResourceCalc)")

st.markdown("---", unsafe_allow_html=False)
