import datetime


events = []     #Global variable to store events

def add_event():    #Add a new event with title, description, date, and time
    
    title = input("Enter event title: ")                #input title
    description = input("Enter event description: ")    #input description of event
    date_str = input("Enter event date (YYYY-MM-DD): ") #input date of event in YYYY-MM-DD format
    time_str = input("Enter event time (HH:MM): ")      #input time of event in HH:MM format

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() 
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD for date.")
        return   #validation for date

    try: 
        time = datetime.datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM for time.")
        return    #validation for time
    
    events.append({     #appending event values to "events" list
        "title": title,    
        "description": description,
        "date": date,
        "time": time
    })
    print("Event added successfully.")
#####################################################################################################
def view_events():      #Display all events sorted by date and time

    if not events:      #if no events scheduled
        print("No events scheduled.")
        return

    sorted_events = sorted(events, key=lambda x: (x["date"], x["time"]))    #Sorting of events by date, if multiple events have the same date they will be sorted by time thereafter
    for event in sorted_events:
        print(f"Title: {event['title']}")
        print(f"Description: {event['description']}")
        print(f"Date: {event['date']}")
        print(f"Time: {event['time']}")
        print()
#####################################################################################################
def delete_event():     #Delete an event based on the title
    
    title = input("Enter the title of the event to delete: ")
    for event in events:
        if event["title"].lower() == title.lower():
            events.remove(event)
            print(f"Event '{title}' deleted successfully.")
            return
    print("Event not found.")
#####################################################################################################
def search_by_date():   #Search an event by date
    """
    Search events by date.
    """
    date_str = input("Enter the date to search (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()      #Validation of date format inputted
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    found_events = [event for event in events if event["date"] == date]
    if found_events:
        print("Events on", date)
        for event in found_events:
            print(f"Title: {event['title']}")
            print(f"Description: {event['description']}")
            print(f"Time: {event['time']}")
            print()
    else:
        print("No events found for the specified date.")
#####################################################################################################
def search_by_keyword():    #Search events by keyword in title/description        
    
    keyword = input("Enter keyword to search: ")
    found_events = [event for event in events if keyword.lower() in event["title"].lower() or keyword.lower() in event["description"].lower()]
    if found_events:
        print("Events containing keyword:", keyword)
        for event in found_events:
            print(f"Title: {event['title']}")
            print(f"Description: {event['description']}")
            print(f"Date: {event['date']}")
            print(f"Time: {event['time']}")
            print()
    else:
        print("No events found containing the specified keyword.")
#####################################################################################################
def main():
    while True:
        print("---------------------\n   Event Scheduler   \n---------------------")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Search Events by Date")
        print("5. Search Events by Keyword")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            search_by_date()
        elif choice == "5":
            search_by_keyword()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
