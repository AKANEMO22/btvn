import json
import csv
from datetime import datetime, date
from typing import List, Dict, Optional
import os
from enum import Enum

class UserRole(Enum):
    """Enum for user roles"""
    ADMIN = "admin"
    EVENT_ORGANIZER = "event_organizer"
    STUDENT = "student"
    VISITOR = "visitor"

class User:
    """User class to represent different types of users"""
    
    def __init__(self, user_id: str, username: str, role: UserRole, email: str = ""):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.email = email
        self.created_events = []  # For event organizers
        self.registered_events = []  # For students/visitors
    
    def to_dict(self) -> Dict:
        """Convert user to dictionary for JSON serialization"""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "role": self.role.value,
            "email": self.email,
            "created_events": self.created_events,
            "registered_events": self.registered_events
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create user from dictionary"""
        user = cls(
            user_id=data["user_id"],
            username=data["username"],
            role=UserRole(data["role"]),
            email=data.get("email", "")
        )
        user.created_events = data.get("created_events", [])
        user.registered_events = data.get("registered_events", [])
        return user

class Event:
    """Event class to represent campus events"""
    
    def __init__(self, event_id: str, name: str, description: str, date: str, 
                 time: str, location: str, max_capacity: int, organizer_id: str):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.location = location
        self.max_capacity = max_capacity
        self.organizer_id = organizer_id
        self.attendees = []
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for JSON serialization"""
        return {
            "event_id": self.event_id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "time": self.time,
            "location": self.location,
            "max_capacity": self.max_capacity,
            "organizer_id": self.organizer_id,
            "attendees": self.attendees,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Event':
        """Create event from dictionary"""
        event = cls(
            event_id=data["event_id"],
            name=data["name"],
            description=data["description"],
            date=data["date"],
            time=data["time"],
            location=data["location"],
            max_capacity=data["max_capacity"],
            organizer_id=data["organizer_id"]
        )
        event.attendees = data.get("attendees", [])
        event.created_at = data.get("created_at", datetime.now().isoformat())
        return event
    
    def get_attendance_count(self) -> int:
        """Get current number of attendees"""
        return len(self.attendees)
    
    def is_full(self) -> bool:
        """Check if event is at full capacity"""
        return len(self.attendees) >= self.max_capacity
    
    def can_register(self, user_id: str) -> bool:
        """Check if user can register for this event"""
        return not self.is_full() and user_id not in self.attendees

class EventManagementSystem:
    """Main system class for managing events and users"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.events: Dict[str, Event] = {}
        self.current_user: Optional[User] = None
        self.data_dir = "data"
        self._ensure_data_directory()
        self._load_data()
    
    def _ensure_data_directory(self):
        """Ensure data directory exists"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _load_data(self):
        """Load users and events from JSON files"""
        try:
            if os.path.exists(f"{self.data_dir}/users.json"):
                with open(f"{self.data_dir}/users.json", 'r', encoding='utf-8') as f:
                    users_data = json.load(f)
                    self.users = {user_id: User.from_dict(user_data) 
                                for user_id, user_data in users_data.items()}
            
            if os.path.exists(f"{self.data_dir}/events.json"):
                with open(f"{self.data_dir}/events.json", 'r', encoding='utf-8') as f:
                    events_data = json.load(f)
                    self.events = {event_id: Event.from_dict(event_data) 
                                 for event_id, event_data in events_data.items()}
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self):
        """Save users and events to JSON files"""
        try:
            users_data = {user_id: user.to_dict() for user_id, user in self.users.items()}
            with open(f"{self.data_dir}/users.json", 'w', encoding='utf-8') as f:
                json.dump(users_data, f, indent=2, ensure_ascii=False)
            
            events_data = {event_id: event.to_dict() for event_id, event in self.events.items()}
            with open(f"{self.data_dir}/events.json", 'w', encoding='utf-8') as f:
                json.dump(events_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def register_user(self, username: str, role: UserRole, email: str = "") -> str:
        """Register a new user"""
        user_id = f"user_{len(self.users) + 1}"
        user = User(user_id, username, role, email)
        self.users[user_id] = user
        self._save_data()
        return user_id
    
    def login(self, user_id: str) -> bool:
        """Login a user"""
        if user_id in self.users:
            self.current_user = self.users[user_id]
            return True
        return False
    
    def logout(self):
        """Logout current user"""
        self.current_user = None
    
    def create_event(self, name: str, description: str, date: str, time: str, 
                    location: str, max_capacity: int) -> Optional[str]:
        """Create a new event (Admin and Event Organizer only)"""
        if not self.current_user or self.current_user.role not in [UserRole.ADMIN, UserRole.EVENT_ORGANIZER]:
            print("❌ Access denied. Only Admins and Event Organizers can create events.")
            return None
        
        # Input validation
        if not name or not description or not date or not time or not location:
            print("❌ All fields are required.")
            return None
        
        if max_capacity <= 0:
            print("❌ Maximum capacity must be greater than 0.")
            return None
        
        try:
            # Validate date format
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return None
        
        event_id = f"event_{len(self.events) + 1}"
        event = Event(event_id, name, description, date, time, location, 
                     max_capacity, self.current_user.user_id)
        
        self.events[event_id] = event
        self.current_user.created_events.append(event_id)
        self._save_data()
        
        print(f"✅ Event '{name}' created successfully!")
        return event_id
    
    def update_event(self, event_id: str, **kwargs) -> bool:
        """Update an existing event"""
        if not self.current_user or self.current_user.role != UserRole.ADMIN:
            print("❌ Access denied. Only Admins can update events.")
            return False
        
        if event_id not in self.events:
            print("❌ Event not found.")
            return False
        
        event = self.events[event_id]
        
        # Update allowed fields
        allowed_fields = ['name', 'description', 'date', 'time', 'location', 'max_capacity']
        for field, value in kwargs.items():
            if field in allowed_fields and value is not None:
                setattr(event, field, value)
        
        self._save_data()
        print(f"✅ Event '{event.name}' updated successfully!")
        return True
    
    def delete_event(self, event_id: str) -> bool:
        """Delete an event (Admin only)"""
        if not self.current_user or self.current_user.role != UserRole.ADMIN:
            print("❌ Access denied. Only Admins can delete events.")
            return False
        
        if event_id not in self.events:
            print("❌ Event not found.")
            return False
        
        event_name = self.events[event_id].name
        del self.events[event_id]
        
        # Remove from users' lists
        for user in self.users.values():
            if event_id in user.created_events:
                user.created_events.remove(event_id)
            if event_id in user.registered_events:
                user.registered_events.remove(event_id)
        
        self._save_data()
        print(f"✅ Event '{event_name}' deleted successfully!")
        return True
    
    def register_for_event(self, event_id: str) -> bool:
        """Register current user for an event"""
        if not self.current_user:
            print("❌ Please login first.")
            return False
        
        if self.current_user.role not in [UserRole.STUDENT, UserRole.VISITOR]:
            print("❌ Only students and visitors can register for events.")
            return False
        
        if event_id not in self.events:
            print("❌ Event not found.")
            return False
        
        event = self.events[event_id]
        
        if not event.can_register(self.current_user.user_id):
            if event.is_full():
                print("❌ Event is at full capacity.")
            else:
                print("❌ You are already registered for this event.")
            return False
        
        event.attendees.append(self.current_user.user_id)
        self.current_user.registered_events.append(event_id)
        self._save_data()
        
        print(f"✅ Successfully registered for '{event.name}'!")
        return True
    
    def unregister_from_event(self, event_id: str) -> bool:
        """Unregister current user from an event"""
        if not self.current_user:
            print("❌ Please login first.")
            return False
        
        if event_id not in self.events:
            print("❌ Event not found.")
            return False
        
        event = self.events[event_id]
        
        if self.current_user.user_id not in event.attendees:
            print("❌ You are not registered for this event.")
            return False
        
        event.attendees.remove(self.current_user.user_id)
        self.current_user.registered_events.remove(event_id)
        self._save_data()
        
        print(f"✅ Successfully unregistered from '{event.name}'!")
        return True
    
    def view_all_events(self) -> List[Event]:
        """View all events (Admin and Event Organizer)"""
        if not self.current_user or self.current_user.role not in [UserRole.ADMIN, UserRole.EVENT_ORGANIZER]:
            print("❌ Access denied. Only Admins and Event Organizers can view all events.")
            return []
        
        return list(self.events.values())
    
    def view_my_events(self) -> List[Event]:
        """View events created by current user (Event Organizer)"""
        if not self.current_user or self.current_user.role != UserRole.EVENT_ORGANIZER:
            print("❌ Access denied. Only Event Organizers can view their events.")
            return []
        
        my_events = []
        for event_id in self.current_user.created_events:
            if event_id in self.events:
                my_events.append(self.events[event_id])
        
        return my_events
    
    def view_registered_events(self) -> List[Event]:
        """View events registered by current user (Student/Visitor)"""
        if not self.current_user or self.current_user.role not in [UserRole.STUDENT, UserRole.VISITOR]:
            print("❌ Access denied. Only students and visitors can view registered events.")
            return []
        
        registered_events = []
        for event_id in self.current_user.registered_events:
            if event_id in self.events:
                registered_events.append(self.events[event_id])
        
        return registered_events
    
    def search_events(self, keyword: str) -> List[Event]:
        """Search events by keyword"""
        if not keyword:
            return list(self.events.values())
        
        keyword = keyword.lower()
        matching_events = []
        
        for event in self.events.values():
            if (keyword in event.name.lower() or 
                keyword in event.description.lower() or 
                keyword in event.location.lower()):
                matching_events.append(event)
        
        return matching_events
    
    def get_event_attendees(self, event_id: str) -> List[User]:
        """Get list of attendees for an event"""
        if not self.current_user or self.current_user.role not in [UserRole.ADMIN, UserRole.EVENT_ORGANIZER]:
            print("❌ Access denied. Only Admins and Event Organizers can view attendees.")
            return []
        
        if event_id not in self.events:
            print("❌ Event not found.")
            return []
        
        event = self.events[event_id]
        attendees = []
        
        for user_id in event.attendees:
            if user_id in self.users:
                attendees.append(self.users[user_id])
        
        return attendees
    
    def get_statistics(self) -> Dict:
        """Get system statistics"""
        if not self.current_user or self.current_user.role != UserRole.ADMIN:
            print("❌ Access denied. Only Admins can view statistics.")
            return {}
        
        total_attendees = sum(len(event.attendees) for event in self.events.values())
        
        if not self.events:
            return {
                "total_events": 0,
                "total_attendees": 0,
                "highest_attendance_event": None,
                "lowest_attendance_event": None
            }
        
        # Find events with highest and lowest attendance
        event_attendance = [(event, len(event.attendees)) for event in self.events.values()]
        event_attendance.sort(key=lambda x: x[1], reverse=True)
        
        highest_attendance_event = event_attendance[0][0] if event_attendance else None
        lowest_attendance_event = event_attendance[-1][0] if event_attendance else None
        
        return {
            "total_events": len(self.events),
            "total_attendees": total_attendees,
            "highest_attendance_event": highest_attendance_event,
            "lowest_attendance_event": lowest_attendance_event
        }
    
    def export_events_to_csv(self, filename: str = "events_report.csv"):
        """Export events data to CSV"""
        if not self.current_user or self.current_user.role != UserRole.ADMIN:
            print("❌ Access denied. Only Admins can export data.")
            return False
        
        try:
            filepath = f"{self.data_dir}/{filename}"
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Event ID', 'Name', 'Description', 'Date', 'Time', 'Location', 
                             'Max Capacity', 'Current Attendees', 'Organizer']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for event in self.events.values():
                    organizer = self.users.get(event.organizer_id, User("", "", UserRole.STUDENT))
                    writer.writerow({
                        'Event ID': event.event_id,
                        'Name': event.name,
                        'Description': event.description,
                        'Date': event.date,
                        'Time': event.time,
                        'Location': event.location,
                        'Max Capacity': event.max_capacity,
                        'Current Attendees': len(event.attendees),
                        'Organizer': organizer.username
                    })
            
            print(f"✅ Events data exported to {filepath}")
            return True
        except Exception as e:
            print(f"❌ Error exporting data: {e}")
            return False
    
    def export_attendees_to_csv(self, event_id: str, filename: str = None):
        """Export attendees data for a specific event to CSV"""
        if not self.current_user or self.current_user.role not in [UserRole.ADMIN, UserRole.EVENT_ORGANIZER]:
            print("❌ Access denied. Only Admins and Event Organizers can export attendee data.")
            return False
        
        if event_id not in self.events:
            print("❌ Event not found.")
            return False
        
        if not filename:
            event = self.events[event_id]
            filename = f"attendees_{event.name.replace(' ', '_')}_{event_id}.csv"
        
        try:
            filepath = f"{self.data_dir}/{filename}"
            attendees = self.get_event_attendees(event_id)
            
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['User ID', 'Username', 'Role', 'Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for attendee in attendees:
                    writer.writerow({
                        'User ID': attendee.user_id,
                        'Username': attendee.username,
                        'Role': attendee.role.value,
                        'Email': attendee.email
                    })
            
            print(f"✅ Attendees data exported to {filepath}")
            return True
        except Exception as e:
            print(f"❌ Error exporting data: {e}")
            return False

class EventManagementUI:
    """User interface for the Event Management System"""
    
    def __init__(self):
        self.system = EventManagementSystem()
        self.setup_demo_data()
    
    def setup_demo_data(self):
        """Setup demo data for testing"""
        if not self.system.users:
            # Create demo users
            admin_id = self.system.register_user("admin", UserRole.ADMIN, "admin@campus.edu")
            organizer_id = self.system.register_user("organizer1", UserRole.EVENT_ORGANIZER, "organizer1@campus.edu")
            student_id = self.system.register_user("student1", UserRole.STUDENT, "student1@campus.edu")
            visitor_id = self.system.register_user("visitor1", UserRole.VISITOR, "visitor1@campus.edu")
            
            # Create demo events
            self.system.login(admin_id)
            self.system.create_event(
                "Campus Career Fair 2024",
                "Annual career fair with top companies",
                "2024-03-15",
                "10:00",
                "Main Auditorium",
                200
            )
            
            self.system.login(organizer_id)
            self.system.create_event(
                "Python Programming Workshop",
                "Learn Python basics and advanced concepts",
                "2024-03-20",
                "14:00",
                "Computer Lab 101",
                30
            )
            
            self.system.create_event(
                "Student Leadership Conference",
                "Leadership skills development workshop",
                "2024-03-25",
                "09:00",
                "Conference Hall",
                100
            )
            
            self.system.logout()
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("🏫 CAMPUS EVENT MANAGEMENT SYSTEM")
        print("="*60)
        
        if self.system.current_user:
            print(f"👤 Logged in as: {self.system.current_user.username} ({self.system.current_user.role.value})")
            print("-"*60)
            
            if self.system.current_user.role == UserRole.ADMIN:
                self.display_admin_menu()
            elif self.system.current_user.role == UserRole.EVENT_ORGANIZER:
                self.display_organizer_menu()
            else:  # Student/Visitor
                self.display_student_menu()
        else:
            self.display_login_menu()
    
    def display_login_menu(self):
        """Display login menu"""
        print("1. Login")
        print("2. Register new user")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            self.login_user()
        elif choice == "2":
            self.register_new_user()
        elif choice == "3":
            print("👋 Thank you for using the Campus Event Management System!")
            exit()
        else:
            print("❌ Invalid choice. Please try again.")
    
    def login_user(self):
        """Handle user login"""
        print("\n--- LOGIN ---")
        user_id = input("Enter User ID: ").strip()
        
        if self.system.login(user_id):
            print(f"✅ Welcome back, {self.system.current_user.username}!")
        else:
            print("❌ Invalid User ID. Please try again.")
    
    def register_new_user(self):
        """Handle new user registration"""
        print("\n--- REGISTER NEW USER ---")
        username = input("Enter username: ").strip()
        
        print("\nSelect role:")
        print("1. Admin")
        print("2. Event Organizer")
        print("3. Student")
        print("4. Visitor")
        
        role_choice = input("Enter role choice (1-4): ").strip()
        role_map = {
            "1": UserRole.ADMIN,
            "2": UserRole.EVENT_ORGANIZER,
            "3": UserRole.STUDENT,
            "4": UserRole.VISITOR
        }
        
        if role_choice not in role_map:
            print("❌ Invalid role choice.")
            return
        
        email = input("Enter email (optional): ").strip()
        
        user_id = self.system.register_user(username, role_map[role_choice], email)
        print(f"✅ User registered successfully! Your User ID is: {user_id}")
    
    def display_admin_menu(self):
        """Display admin menu"""
        print("ADMIN MENU:")
        print("1. Create Event")
        print("2. Update Event")
        print("3. Delete Event")
        print("4. View All Events")
        print("5. View Event Attendees")
        print("6. View Statistics")
        print("7. Export Events to CSV")
        print("8. Export Attendees to CSV")
        print("9. Logout")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            self.create_event_ui()
        elif choice == "2":
            self.update_event_ui()
        elif choice == "3":
            self.delete_event_ui()
        elif choice == "4":
            self.view_all_events_ui()
        elif choice == "5":
            self.view_event_attendees_ui()
        elif choice == "6":
            self.view_statistics_ui()
        elif choice == "7":
            self.export_events_ui()
        elif choice == "8":
            self.export_attendees_ui()
        elif choice == "9":
            self.system.logout()
            print("✅ Logged out successfully!")
        else:
            print("❌ Invalid choice. Please try again.")
    
    def display_organizer_menu(self):
        """Display event organizer menu"""
        print("EVENT ORGANIZER MENU:")
        print("1. Create Event")
        print("2. View My Events")
        print("3. View Event Attendees")
        print("4. Export Attendees to CSV")
        print("5. Logout")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            self.create_event_ui()
        elif choice == "2":
            self.view_my_events_ui()
        elif choice == "3":
            self.view_event_attendees_ui()
        elif choice == "4":
            self.export_attendees_ui()
        elif choice == "5":
            self.system.logout()
            print("✅ Logged out successfully!")
        else:
            print("❌ Invalid choice. Please try again.")
    
    def display_student_menu(self):
        """Display student/visitor menu"""
        print("STUDENT/VISITOR MENU:")
        print("1. Search Events")
        print("2. View Registered Events")
        print("3. Register for Event")
        print("4. Unregister from Event")
        print("5. Logout")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            self.search_events_ui()
        elif choice == "2":
            self.view_registered_events_ui()
        elif choice == "3":
            self.register_for_event_ui()
        elif choice == "4":
            self.unregister_from_event_ui()
        elif choice == "5":
            self.system.logout()
            print("✅ Logged out successfully!")
        else:
            print("❌ Invalid choice. Please try again.")
    
    def create_event_ui(self):
        """UI for creating events"""
        print("\n--- CREATE EVENT ---")
        name = input("Event name: ").strip()
        description = input("Description: ").strip()
        date = input("Date (YYYY-MM-DD): ").strip()
        time = input("Time (HH:MM): ").strip()
        location = input("Location: ").strip()
        
        try:
            max_capacity = int(input("Maximum capacity: ").strip())
        except ValueError:
            print("❌ Invalid capacity. Please enter a number.")
            return
        
        self.system.create_event(name, description, date, time, location, max_capacity)
    
    def update_event_ui(self):
        """UI for updating events"""
        print("\n--- UPDATE EVENT ---")
        self.view_all_events_ui()
        
        event_id = input("\nEnter Event ID to update: ").strip()
        if event_id not in self.system.events:
            print("❌ Event not found.")
            return
        
        print("\nEnter new values (press Enter to skip):")
        name = input("New name: ").strip()
        description = input("New description: ").strip()
        date = input("New date (YYYY-MM-DD): ").strip()
        time = input("New time (HH:MM): ").strip()
        location = input("New location: ").strip()
        
        max_capacity = None
        capacity_input = input("New maximum capacity: ").strip()
        if capacity_input:
            try:
                max_capacity = int(capacity_input)
            except ValueError:
                print("❌ Invalid capacity. Update cancelled.")
                return
        
        updates = {}
        if name: updates['name'] = name
        if description: updates['description'] = description
        if date: updates['date'] = date
        if time: updates['time'] = time
        if location: updates['location'] = location
        if max_capacity is not None: updates['max_capacity'] = max_capacity
        
        if updates:
            self.system.update_event(event_id, **updates)
        else:
            print("❌ No updates provided.")
    
    def delete_event_ui(self):
        """UI for deleting events"""
        print("\n--- DELETE EVENT ---")
        self.view_all_events_ui()
        
        event_id = input("\nEnter Event ID to delete: ").strip()
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            self.system.delete_event(event_id)
        else:
            print("❌ Deletion cancelled.")
    
    def view_all_events_ui(self):
        """UI for viewing all events"""
        print("\n--- ALL EVENTS ---")
        events = self.system.view_all_events()
        
        if not events:
            print("No events found.")
            return
        
        for event in events:
            print(f"\n📅 Event ID: {event.event_id}")
            print(f"   Name: {event.name}")
            print(f"   Description: {event.description}")
            print(f"   Date: {event.date} at {event.time}")
            print(f"   Location: {event.location}")
            print(f"   Capacity: {len(event.attendees)}/{event.max_capacity}")
            print(f"   Organizer: {self.system.users[event.organizer_id].username}")
    
    def view_my_events_ui(self):
        """UI for viewing organizer's events"""
        print("\n--- MY EVENTS ---")
        events = self.system.view_my_events()
        
        if not events:
            print("No events found.")
            return
        
        for event in events:
            print(f"\n📅 Event ID: {event.event_id}")
            print(f"   Name: {event.name}")
            print(f"   Description: {event.description}")
            print(f"   Date: {event.date} at {event.time}")
            print(f"   Location: {event.location}")
            print(f"   Capacity: {len(event.attendees)}/{event.max_capacity}")
    
    def view_registered_events_ui(self):
        """UI for viewing registered events"""
        print("\n--- MY REGISTERED EVENTS ---")
        events = self.system.view_registered_events()
        
        if not events:
            print("No registered events found.")
            return
        
        for event in events:
            print(f"\n📅 Event ID: {event.event_id}")
            print(f"   Name: {event.name}")
            print(f"   Description: {event.description}")
            print(f"   Date: {event.date} at {event.time}")
            print(f"   Location: {event.location}")
            print(f"   Capacity: {len(event.attendees)}/{event.max_capacity}")
    
    def search_events_ui(self):
        """UI for searching events"""
        print("\n--- SEARCH EVENTS ---")
        keyword = input("Enter search keyword: ").strip()
        
        events = self.system.search_events(keyword)
        
        if not events:
            print("No events found matching your search.")
            return
        
        print(f"\nFound {len(events)} event(s):")
        for event in events:
            print(f"\n📅 Event ID: {event.event_id}")
            print(f"   Name: {event.name}")
            print(f"   Description: {event.description}")
            print(f"   Date: {event.date} at {event.time}")
            print(f"   Location: {event.location}")
            print(f"   Capacity: {len(event.attendees)}/{event.max_capacity}")
            print(f"   Status: {'🟢 Available' if not event.is_full() else '🔴 Full'}")
    
    def register_for_event_ui(self):
        """UI for registering for events"""
        print("\n--- REGISTER FOR EVENT ---")
        self.search_events_ui()
        
        event_id = input("\nEnter Event ID to register: ").strip()
        self.system.register_for_event(event_id)
    
    def unregister_from_event_ui(self):
        """UI for unregistering from events"""
        print("\n--- UNREGISTER FROM EVENT ---")
        self.view_registered_events_ui()
        
        event_id = input("\nEnter Event ID to unregister: ").strip()
        self.system.unregister_from_event(event_id)
    
    def view_event_attendees_ui(self):
        """UI for viewing event attendees"""
        print("\n--- VIEW EVENT ATTENDEES ---")
        
        if self.system.current_user.role == UserRole.ADMIN:
            self.view_all_events_ui()
        else:
            self.view_my_events_ui()
        
        event_id = input("\nEnter Event ID to view attendees: ").strip()
        attendees = self.system.get_event_attendees(event_id)
        
        if not attendees:
            print("No attendees found for this event.")
            return
        
        print(f"\nAttendees for Event ID {event_id}:")
        for attendee in attendees:
            print(f"   👤 {attendee.username} ({attendee.role.value}) - {attendee.email}")
    
    def view_statistics_ui(self):
        """UI for viewing statistics"""
        print("\n--- SYSTEM STATISTICS ---")
        stats = self.system.get_statistics()
        
        if not stats:
            return
        
        print(f"📊 Total Events: {stats['total_events']}")
        print(f"👥 Total Attendees: {stats['total_attendees']}")
        
        if stats['highest_attendance_event']:
            event = stats['highest_attendance_event']
            print(f"🏆 Highest Attendance: '{event.name}' with {len(event.attendees)} attendees")
        
        if stats['lowest_attendance_event']:
            event = stats['lowest_attendance_event']
            print(f"📉 Lowest Attendance: '{event.name}' with {len(event.attendees)} attendees")
    
    def export_events_ui(self):
        """UI for exporting events"""
        filename = input("Enter filename (default: events_report.csv): ").strip()
        if not filename:
            filename = "events_report.csv"
        
        self.system.export_events_to_csv(filename)
    
    def export_attendees_ui(self):
        """UI for exporting attendees"""
        if self.system.current_user.role == UserRole.ADMIN:
            self.view_all_events_ui()
        else:
            self.view_my_events_ui()
        
        event_id = input("\nEnter Event ID to export attendees: ").strip()
        filename = input("Enter filename (optional): ").strip()
        
        if not filename:
            filename = None
        
        self.system.export_attendees_to_csv(event_id, filename)
    
    def run(self):
        """Run the main application loop"""
        print("🚀 Starting Campus Event Management System...")
        
        while True:
            try:
                self.display_menu()
            except KeyboardInterrupt:
                print("\n\n👋 Thank you for using the Campus Event Management System!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    ui = EventManagementUI()
    ui.run() 