## PROJECT DETAILS

    @Created:  18 Oct 2018
    @Modified: 19 Jan 2019
    @Authors:  
         Donald Chinhuru - Electronics Engineering Part 2
         Kingsley Mhlanga - Civil and Water Engineering Part 2

```buildoutcfg
    Changes:
        - generate public and private RSA keys
        - encrypt the same data with same key and output different encrypted data file
        - encrypting data now working
        - decrypting many files at once, tested and working
        
```

## WEB APP FOR THE VOTING PROCESS
- in-cooperate end-end encryption
- only 1 voter per candidate per day
- use student id as unique identifier of the voters
- can use node red dashboard to show all candidates
- voting includes button clicks and tabs on the dashboard
- once voter's choice is selected, it is locked on, encrypted, saved and counted

## Merits
- counting takes place on the go
- voter's choice is encrypted
- friendly UI
- no duplicated records
- only 1 voter is guaranteed to vote once during the voting session
- results are synchronized to cloud or offline server in real time in case of system crash

## Demerits
- in case of a bug, voting process and results are compromised [incompatible](bug)

## Node Red
- contains all the dashboard elements
- UI integrated with back end channel
- updates UI for recent changes in real time
- synchronizes UI interface with back end
- show help links

## VB.Net [Kingsley](team)
- Contains dashboard elements
- synchronize with back end and database

## Operation
- student scans id card bar code [Ceremonial_Exam_](scan)
- once scanned, it searches the database and outputs student ID and details on the dashboard
- student proceed to the next station where there is a PC / tablet running Node red server / VB.Net application
- The welcome screen will be displayed, with student details and portrait of their ID
- The welcome screen will also have friendly nice UI and how to navigate and vote

## UI format
- The dashboard will have 4 tabs
*     Home
*     Presidential candidates
*     Councilor candidates
*     Help

## Home Tab
- Has welcome screen for the SRC voting process, objectives, mission etc
- Show how to navigate the [UI](voting_dashboard)
- Has link to the [Help UI](tab)

## Presidential Tab
- includes all candidates campaigning
- inludes their party org..if any, their profile and clear picture
- candidates are layed out in a nice and easy to navigate and operate, way
- contains a [button click](event) on each candidate for selection
- [button selection](event) is followed by a verification pop up for proceeding and aborting the operation
- only allowed number is allowed, once allowed it rejects editing or another selection entry
- finally [student](voter) confirms, one more time their choice
- once [student](voter) accepts selection, its locked, encrypted, saved and backed up
- returns to the [Home UI](tab)

## Councilor Tab
- includes all registered candidates campaigning
- can be derived and inherits all functionalities of the [Presidential UI](tab).
- only a maximum of the allowed councillors is allowed

## Help Tab
- has connection link to the [Home UI](tab)
- Shows how to cast a vote on a candidate
- might include [GIFs](pictorial_help) to show how to navigate through the [Home UI](tab).
- also include [GIFs](pictorial_help) to navigate on the [Presidential UI](tab) and how to cast a vote
- does the same process above for the [Councilor UI](tab).

## File I/O
- results are saved to an encrypted .bin format file
- also saved in a [database](results_storage) with encrypted [student's](voter) voted choice
- encryption key is generated once before run time using a secure encryption library, and one user hold it 
- the key file is then deleted and held in the authorised person's responsibility
- decryption only happens when counting the total, given the correct decryption key 
- with this operation, a [student's](voter) vote remains unknown to everyone except the [student](voter).

## Database structure
- structure of saved [database](results_storage) table.
- database has links to another database
- First: includes general student information
- Second: includes particular src results
- column [src-status](db_link) links to the other database with src related data.
*     first-name, last-name, enrolled, year, part, reg-status, src-status
- [src-status](db_link) now looks like
*     president_1, councilor_1, councilor_2, councilor_3, councilor_4, councilor_5
- values are not stored in order, the above column's data is an encrypted binary file representing a candidate's real information

## Security
- only 1 person can enter a code to decrypt the voter's data and counting commences
- once a student cast a vote, their choices are encrypted and saved as .bin file
- all encrypted data is then saved to database per student row/document
- choice remains unknown to all other parties expect the student, thereby guaranteeing full security
- 1 authorised person with the key has power to decrypt all encrypted data at a specified time of counting results
- with this, noone knows where a particular vote was casted expect the voter

## Acknowledgements
- [Donald Chinhuru](project_leader) and [Kingsley Mhlanga](project_leader)

![python-image](/home/donald/Projects/Python36/web-app/SRC_/pic.png "Keep calm and code Python")
