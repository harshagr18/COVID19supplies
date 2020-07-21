<div align="center">
	<img src="images/logo.png" height="200" align="center">
<br/>
Medical supply monitoring tool for the Government of India
</div>

## About The Project
After a brief conversation with a WHO doctor, we aimed our project towards solving one of the major problems faced by all medical professionals and the common man alike, that is the inaccessibility of medical supplies due to inefficiency of data management. Supplies are available, but unfortunately what is lacking is the easy to access information on where exactly are they available. Our main focus while developing this system has been towards getting an accurate data at high computation speeds while ensuring maximum ease of access for the simplest of users.

### Architecture
<div align="center">
<img src="images/arch.png" align="center">
</div>
<br><br><br>

### Modules of the Project
 - **Python user interface for medical stores and hospitals**
	* All suppliers will register with a unique username and password which will be used to log into the system there after.
	* The system is used to input data into the main database, directly from an excel sheet, which auto sorts required columns and eliminates the futile data. 
 - **Web servers for Users**
	* This module solely caters to the common man who wants to purchase medical supplies. 
	* Rather than searching multiple stores and increasing his risk of acquiring the COVID-19, he gets perfect information of availability and location of his medical supplies
	* The user browses to "COVID-19supplies.in", and enters the location and required supply which will auto filter all the stores in his range, and give him most optimal store location. 

## Usage
 - This decreases time of exposure of the general public with other people, decreasing the chance of acquiring COVID-19
 - It is a very efficient inventory management system for all medical stores
 - It automatically filters out the medical supplies unrelated to COVID-19 decreasing the computation time, giving the user faster responses.


### Software Requirements
 - **Internet**
	* A stable internet connection for accessibility.
 - **Server**
 	* A web service platform to update, compute and access data efficiently


### Software Packages used 
* Django
* HTML-CSS Web Dev
* Python - Tkinter user interface
* SQLite3 Database

<div align="center">

## YouTube Video
</div>

<div align="center"> <a href="https://youtu.be/cCuRLkp0KQ8"><img src="http://img.youtube.com/vi/cCuRLkp0KQ8/0.jpg" width="30%"></a> <br> <a href="https://youtu.be/cCuRLkp0KQ8">Demonstration Video</a></div>
<br><br>

## License

	Copyright (C) 2020 Harsh Sanjay Agrawal

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	   http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
