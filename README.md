# MEDICAL-APPOINTMENT-SCHEDULING

THIS IS A GUI TO TAKE AND MANAGE APPOINTMENTS

## INTRODUCTION

There are majorly 2 parts: 
1. DATABASE-SERVER
2. APPOINTMENT-CLIENT

The DATABASESERVER part is run by the organization to track the appointments, and the APPOINTMENTCLIENT part is run by the clients who want to register or take any appointment.

Here, I have used the UDP protocol (USER DATAGRAM PROTOCOL), which is faster than the TCP protocol. I have also implemented a check to track any data loss by using an acknowledgement message. On the database side, there is also a checking condition to stop any duplicate entry.

## HOW TO USE SERVER

1. First, the database file to store the appointment is created.
2. Execute the `DATABASESERVER.py` file, which will track any incoming connection and the appointments.
3. After executing the `DATABASESERVER.py` file, click the `START` button to start the server. This will wait for incoming connections and show a pop-up that the server has successfully started.
4. When the `SHOW` button is clicked, it will show the list of appointments.

**Note:** Before executing the file, the database file should be created where the data will be stored.

## APPOINTMENT CLIENT

1. Execute the `APPOINTMENTCLIENT.py` file.
2. When executed, a GUI will pop up where the details should be filled by the patient.
3. The patient has to fill in details like:
    - NAME OF PATIENT
    - DATE
    - SELECT the time from the options: 11am-1pm, 2pm-5pm, 6pm-9pm
    - Enter the server ID (unique for every server) in which they are registering.
4. Then, click on the `REGISTER` button to register.
5. In case of successful registration, a pop-up will show "successfully registered".
6. In case of a duplicate entry, a pop-up will show "Error: Already Registered".
