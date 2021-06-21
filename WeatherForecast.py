#import all functions from the tkinter
from tkinter import *
from tkinter import messagebox

#function to get weather details of any city using openweathermap api
def tell_weather():

	#import required modules
	import requests,json

	#api key 
	api_key="ea703e5096d2c427f260faf546b68efb"

	#store url
	base_url="http://api.openweathermap.org/data/2.5/weather?"

        #take a city name from city_field entry box
	city_name=city_field.get()

	#store complete url address
	complete_url=base_url+"q="+city_name+"&APPID="+api_key

	#get method of requests module to return response object
	response=requests.get(complete_url)

	#json method of response object to convert json format data into python format data
	i=response.json()

	#if we press submit without entering city name
	if city_name=='':

                #message dialog box appear which shows given Error message
		messagebox.showerror("Error","Please Enter the City Name")


        #now i contains list of nested dictionaries,we know dictionary contains key value pair
	#check the value of "cod" key is equal to "404" or not if not that means city is found otherwise city is not found
	elif i["cod"]!="404":

		#store the value of "main" key in variable j
		j=i["main"]
		
		#store the value corresponding to the "temp" key of j
		current_temperature=j["temp"]-273.15

		#store the value corresponding to the "pressure" key of j
		current_pressure=j["pressure"]

		#store the value corresponding to the "humidity" key of j
		current_humidity=j["humidity"]

		#store the value of "weather" key in variable k
		k=i["weather"]

		#store the value corresponding to the "description" key at the 0th index of k
		weather_description=k[0]["description"]

                #store the value of "wind" key in variable l
		l=i["wind"]

		#store the value corresponding to the "speed" key of l
		current_wind_speed=l["speed"]

		#store the value of "sys" key in variable m
		m=i["sys"]

		#store the value corresponding to the "country" key of m
		country_name=m["country"]

		#insert method inserting the values in corresponding text entry boxes
		temp_field.insert(15,str(current_temperature)+" celsius")
		atm_field.insert(10,str(current_pressure)+" hPa")
		humid_field.insert(15,str(current_humidity)+" %")
		desc_field.insert(10,str(weather_description))
		speed_field.insert(10,str(current_wind_speed)+" knots")
		country_field.insert(10,str(country_name))


	#if city is not found				
	else:

                #message dialog box appear which shows given Error message
		messagebox.showerror("Error","City Not Found \n" "Please Enter a Valid City Name")

		#clear the content of city_field entry box
		city_field.delete(0,END)


#function for clearing the contents of all text boxes
def clear_all():
        
	city_field.delete(0,END)
	temp_field.delete(0,END)
	atm_field.delete(0,END)
	humid_field.delete(0,END)
	desc_field.delete(0,END)
	speed_field.delete(0,END)
	country_field.delete(0,END)

	#set focus on the city_field entry box
	city_field.focus_set()


#driver code
if __name__ == "__main__":

	#create a GUI window
	root=Tk()

	#set the name of tkinter GUI window
	root.title("Weather Forecast")

	#set the background colour of GUI window
	root.configure(background="light blue")

	#set the configuration of GUI window
	root.geometry("400x330")

	#frame for searching,title
	frame1=LabelFrame(root,bg="light blue",fg="white")
	frame1.place(x=0,y=0,width=400,height=112)

	#frame for information
	frame2=LabelFrame(root,bg="light blue",fg="white")
	frame2.place(x=0,y=112,width=400,height=218)

	#create a Weather GUI Application label
	headlabel=Label(frame1,text="Weather GUI Application",font=("bold",15),fg='black',bg='white')
	
	#create a City name : label
	label1=Label(frame1,text="City Name : ",fg='black',bg='pink')
	
	#create a Temperature : label
	label2=Label(frame2,text="Temperature :",fg='black',bg='pink')

	#create a Atm Pressure : label
	label3=Label(frame2,text="Atm Pressure :",fg='black',bg='pink')

	#create a Humidity : label
	label4=Label(frame2,text="Humidity :",fg='black',bg='pink')

	#create a Description : label
	label5=Label(frame2,text="Description :",fg='black',bg='pink')

	#create a Wind Speed : label
	label6=Label(frame2,text="Wind Speed :",fg='black',bg='pink')

	#create a Country : Label
	label7=Label(frame2,text="Country :",fg='black',bg='pink')
	

	#grid method is used for placing the widgets at respective positions in table
	headlabel.grid(row=0,column=1,padx=0,pady=10)
	label1.grid(row=1,column=0,sticky="W",padx=10)
	label2.grid(row=0,column=0,sticky="W",padx=10,pady=8)
	label3.grid(row=1,column=0,sticky="W",padx=10,pady=0)
	label4.grid(row=2,column=0,sticky="W",padx=10,pady=8)
	label5.grid(row=3,column=0,sticky="W",padx=10,pady=0)
	label6.grid(row=4,column=0,sticky="W",padx=10,pady=8)
	label7.grid(row=5,column=0,sticky="W",padx=10,pady=0)


	#create text entry boxes for filling or typing the information
	city_field=Entry(frame1)
	temp_field=Entry(frame2)
	atm_field=Entry(frame2)
	humid_field=Entry(frame2)
	desc_field=Entry(frame2)
	speed_field=Entry(frame2)
	country_field=Entry(frame2)

	#grid method is used for placing the widgets at respective positions in table,ipadx keyword argument set width of entry space 
	city_field.grid(row=1,column=1,ipadx="50",padx=0,pady=4)
	temp_field.grid(row=0,column=1,ipadx="70",pady=8)
	atm_field.grid(row=1,column=1,ipadx="70",pady=0)
	humid_field.grid(row=2,column=1,ipadx="70",pady=8)
	desc_field.grid(row=3,column=1,ipadx="70",pady=0)
	speed_field.grid(row=4,column=1,ipadx ="70",pady=8)
	country_field.grid(row=5,column=1,ipadx="70",pady=0)

	#create a Submit Button and attach it to tell_weather function
	button1=Button(frame1,text="Submit",bg="white",fg="black",command=tell_weather)

	#create a Clear Button and attach it to clear_all function
	button2=Button(frame2,text="Clear",bg="white",fg="black",command=clear_all)

	#grid method is used for placing the widgets at respective positions in table
	button1.grid(row=2,column=1,padx=0,pady=3)
	button2.grid(row=6,column=1,padx=0,pady=8)

	#set focus on the city_field entry box
	city_field.focus_set()
	
	#start the GUI
	root.mainloop()

	
