train_name = "Rajdhani Express"
train_number = 1250
source_station = "Pune"
destination_station = "Mahad"
ticket_price = 598.9

print("Welcome to Indian Railway Reservation System")
print("Train Name :", train_name)
print("Train Number :", train_number)
print("Source Station :", source_station)
print("Destination Station :", destination_station) 

print(type(train_name))
print(type(train_number))
print(type(ticket_price))

#Passenger Information
passenger_name = "Rahul Sharma"

seat_number = "B2-45"
#Seat confirmation Status
is_confirmed = True

#Convert float data into integer data type
ticket_price_integer = int(ticket_price)
print(type(ticket_price_integer))

#Convert integer data into string format
train_number_string = str(train_number)
print(type(train_number_string))


passenger_name = "Rahul Sharma"
seat_number = "B2-45"
confirmation_status = "Confirmed"

print("-------Railway Ticket-----")
print("Passenger Name:", passenger_name)
print("Passenger Number:", seat_number)
print("Ticket Status:", confirmation_status)
print("---------------------")


passenger_name = "Rahul Sharma"
passenger_age = 28
gender = "Male"
mobile_number = 9876543210

print("Passenger Name :", passenger_name)
print("Passenger Age :", passenger_age)
print("Gender :", gender)
print("Mobile Number :", mobile_number)

train_name = "Rajdhani Express"
seat_number = "B2-45"
ticket_price = 2450
journey_date = "25-May-2026"

print("Train Name :", train_name)
print("Seat Number :", seat_number)
print("Ticket Price :", ticket_price)
print("Journey Date :", journey_date)

number_of_passengers = 3
ticket_price = 2450

total_fare = number_of_passengers * ticket_price
print("Total Fare :", total_fare)

gst_percentage = 5

gst_amount = (total_fare * gst_percentage) / 100
print("GST Amount :", gst_amount)

final_amount = total_fare + gst_amount
print("Final Payable Amount :", final_amount)

print("----------- Indian Railways Ticket -----------")
print("Passenger Name :", passenger_name)
print("Train Name 	:", train_name)
print("Seat Number	:", seat_number)
print("Journey Date   :", journey_date)
print("Passengers 	:", number_of_passengers)
print("Ticket Fare	:", total_fare)
print("GST Amount 	:", gst_amount)
print("Final Amount   :", final_amount)
print("----------------------------------------------")


passenger_name = "Rahul Sharma"
ticket_status = "Confirmed"

if ticket_status == "Confirmed":
 	print("Ticket is Confirmed")
  
waiting_list = 3

if waiting_list == 0:
 	print("Ticket Confirmed")
else:
 	print("Ticket is in Waiting List")
  
ticket_status = "RAC"

if ticket_status == "Confirmed":
 	print("Seat Allocated Successfully")
elif ticket_status == "RAC":
 	print("Partial Reservation Available")
else:
 	print("Ticket is in Waiting List")
  
age = 65
if age >= 60:
 	print("Passenger Eligible for Senior Citizen Discount")
  
  
age = 65
is_ticket_confirmed = True

if age >= 60 and is_ticket_confirmed == True:
 	print("Passenger eligible for Senior Citizen Benefits")
  
  
ticket_status = "Confirmed"
payment_status = "Paid"

if ticket_status == "Confirmed" and payment_status == "Paid":
 	print("Ticket Successfully Booked")
elif ticket_status == "RAC":
 	print("Partial Seat Reservation Available")
else:
 	print("Booking Pending")
  
passenger_age = 25
ticket_confirmed = True

if passenger_age >= 18 and ticket_confirmed:
   print("Passenger Eligible for Travel")
   
confirmed_seat = False
rac_seat = True

if confirmed_seat or rac_seat:
   print("Reservation Available")
   

ticket_cancelled = False

if not ticket_cancelled:
   print("Ticket is Active")
   
passenger_age = 65
payment_completed = True

if passenger_age >= 60 and payment_completed:
   print("Senior Citizen Reservation Approved")
   
available_seats = 5
payment_status = True

if available_seats > 0 and payment_status:
   print("Ticket Confirmed Successfully")
else:
   print("Reservation Failed")
   

valid_id_proof = True
booking_time_valid = True

if valid_id_proof and booking_time_valid:
   print("Tatkal Booking Allowed")
else:
   print("Tatkal Booking Denied")
   
passenger_name = "Rahul Sharma"
passenger_age = 30
available_seats = 2
payment_completed = True
ticket_cancelled = False

if (
   passenger_age >= 18 and
   available_seats > 0 and
   payment_completed and
   not ticket_cancelled
):
   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Reservation Status : Confirmed")
else:
   print("Reservation Failed")

