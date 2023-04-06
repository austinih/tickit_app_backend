# tickit_app_backend

# Tick-iT
Welcome to the Tick-iT Demo! Tick-iT is a concert search and booking app for the Denver, CO area. This project was built using React.js on the front end and Django for our backend API. 

## The Team

### Toni Hall

<details>
    <summary>Socials</summary>

- [Github](https://github.com/windtronic)
- [LinkedIn](linkedin.com/in/toni-hall)

</details>

### Tyler Carter

<details>
    <summary>Socials</summary>

- [Github(](https://github.com/bojeebs)
- [LinkedIn](https://www.linkedin.com/in/carter-tyler/)

</details>

### Austin Holland

<details>
    <summary>Socials</summary>

- [Github](https://github.com/austinih)
- [LinkedIn](linkedin.com/in/austinih)

</details>

## ERD
![Screenshot of ERD](assets/Tickit_ERD.png)

## Models

<details>
    <summary>Venues</summary>

### Venues
The Venues model will store all data realting to each venue that our app covers. Each venue can host multiple events. Venue fields are: 
- venue_id - PK
- name - string
- address - string
- image_url - string

</details>

<details>
    <summary>Events</summary>

### Events
The Events model will store all data realting to each upcoming event at a venue. An event is tied to a venue. Event fields are: 
- event_id - PK
- title - string
- artist - string
- date - date
- genre - string
- price - decimal
- image_url - string
- venue_id - FK

</details>

<details>
    <summary>Tickets</summary>

### Tickets
The Tickets model will store all data realting to each ticket purchased for an event. A ticket is tied to a specific event. Ticket instances are generated when a user purchases a ticket on the website. Ticket fields are: 
- ticket_id - PK
- name - string
- email - string
- phone_number - string
- seat_number - string
- credit_card_number - string
- event_id - FK

</details>

## Links
![Frontend Repo Link](https://github.com/austinih/tickit_app_frontend)