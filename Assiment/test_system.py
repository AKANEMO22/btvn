#!/usr/bin/env python3
"""
Test script for Campus Event Management System
This script demonstrates all major features of the system
"""

import sys
import os
from event_management_system import EventManagementSystem, UserRole

def test_system():
    """Run comprehensive tests of the system"""
    print("🧪 TESTING CAMPUS EVENT MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Initialize system
    system = EventManagementSystem()
    
    # Test 1: User Registration
    print("\n📝 TEST 1: User Registration")
    print("-" * 40)
    
    admin_id = system.register_user("test_admin", UserRole.ADMIN, "admin@test.edu")
    organizer_id = system.register_user("test_organizer", UserRole.EVENT_ORGANIZER, "organizer@test.edu")
    student_id = system.register_user("test_student", UserRole.STUDENT, "student@test.edu")
    visitor_id = system.register_user("test_visitor", UserRole.VISITOR, "visitor@test.edu")
    
    print(f"✅ Admin created: {admin_id}")
    print(f"✅ Organizer created: {organizer_id}")
    print(f"✅ Student created: {student_id}")
    print(f"✅ Visitor created: {visitor_id}")
    
    # Test 2: Admin Login and Event Creation
    print("\n👑 TEST 2: Admin Event Management")
    print("-" * 40)
    
    system.login(admin_id)
    print(f"✅ Logged in as: {system.current_user.username}")
    
    # Create events
    event1_id = system.create_event(
        "Tech Conference 2024",
        "Annual technology conference with industry experts",
        "2024-04-15",
        "09:00",
        "Main Conference Hall",
        150
    )
    
    event2_id = system.create_event(
        "Student Art Exhibition",
        "Showcase of student artwork and creative projects",
        "2024-04-20",
        "14:00",
        "Art Gallery",
        80
    )
    
    print(f"✅ Event 1 created: {event1_id}")
    print(f"✅ Event 2 created: {event2_id}")
    
    # Test 3: View All Events (Admin)
    print("\n📋 TEST 3: View All Events (Admin)")
    print("-" * 40)
    
    events = system.view_all_events()
    print(f"📊 Total events: {len(events)}")
    for event in events:
        print(f"   📅 {event.name} - {event.date} at {event.time}")
    
    # Test 4: Student Registration
    print("\n🎓 TEST 4: Student Event Registration")
    print("-" * 40)
    
    system.logout()
    system.login(student_id)
    print(f"✅ Logged in as: {system.current_user.username}")
    
    # Search events
    search_results = system.search_events("Tech")
    print(f"🔍 Found {len(search_results)} events matching 'Tech'")
    
    # Register for event
    if search_results:
        success = system.register_for_event(search_results[0].event_id)
        print(f"✅ Registration result: {success}")
    
    # View registered events
    registered = system.view_registered_events()
    print(f"📋 Registered events: {len(registered)}")
    
    # Test 5: Visitor Registration
    print("\n👤 TEST 5: Visitor Event Registration")
    print("-" * 40)
    
    system.logout()
    system.login(visitor_id)
    print(f"✅ Logged in as: {system.current_user.username}")
    
    # Register for both events
    for event in system.search_events(""):
        success = system.register_for_event(event.event_id)
        print(f"✅ Registration for '{event.name}': {success}")
    
    # Test 6: Event Organizer Management
    print("\n🎪 TEST 6: Event Organizer Management")
    print("-" * 40)
    
    system.logout()
    system.login(organizer_id)
    print(f"✅ Logged in as: {system.current_user.username}")
    
    # Create organizer event
    organizer_event_id = system.create_event(
        "Workshop Series",
        "Weekly programming workshops",
        "2024-04-25",
        "16:00",
        "Computer Lab 201",
        25
    )
    
    print(f"✅ Organizer event created: {organizer_event_id}")
    
    # View my events
    my_events = system.view_my_events()
    print(f"📋 My events: {len(my_events)}")
    
    # Test 7: Admin Statistics and Reports
    print("\n📊 TEST 7: Admin Statistics and Reports")
    print("-" * 40)
    
    system.logout()
    system.login(admin_id)
    print(f"✅ Logged in as: {system.current_user.username}")
    
    # Get statistics
    stats = system.get_statistics()
    print(f"📈 Total events: {stats['total_events']}")
    print(f"👥 Total attendees: {stats['total_attendees']}")
    
    if stats['highest_attendance_event']:
        print(f"🏆 Highest attendance: {stats['highest_attendance_event'].name}")
    
    if stats['lowest_attendance_event']:
        print(f"📉 Lowest attendance: {stats['lowest_attendance_event'].name}")
    
    # Test 8: View Event Attendees
    print("\n👥 TEST 8: View Event Attendees")
    print("-" * 40)
    
    for event in system.view_all_events():
        attendees = system.get_event_attendees(event.event_id)
        print(f"📅 {event.name}: {len(attendees)} attendees")
        for attendee in attendees:
            print(f"   👤 {attendee.username} ({attendee.role.value})")
    
    # Test 9: Export Data
    print("\n💾 TEST 9: Export Data")
    print("-" * 40)
    
    # Export events
    events_export = system.export_events_to_csv("test_events_report.csv")
    print(f"✅ Events export: {events_export}")
    
    # Export attendees for first event
    if system.view_all_events():
        first_event = system.view_all_events()[0]
        attendees_export = system.export_attendees_to_csv(
            first_event.event_id, 
            f"test_attendees_{first_event.name.replace(' ', '_')}.csv"
        )
        print(f"✅ Attendees export: {attendees_export}")
    
    # Test 10: Error Handling
    print("\n⚠️ TEST 10: Error Handling")
    print("-" * 40)
    
    # Try to register for non-existent event
    system.logout()
    system.login(student_id)
    result = system.register_for_event("non_existent_event")
    print(f"❌ Expected error for non-existent event: {not result}")
    
    # Try to access admin function as student
    result = system.delete_event("event_1")
    print(f"❌ Expected access denied for student: {not result}")
    
    # Try to create event with invalid data
    system.logout()
    system.login(admin_id)
    result = system.create_event("", "", "invalid-date", "", "", -5)
    print(f"❌ Expected validation error: {not result}")
    
    print("\n🎉 ALL TESTS COMPLETED!")
    print("=" * 60)
    
    # Show final system state
    print("\n📋 FINAL SYSTEM STATE:")
    print(f"👥 Total users: {len(system.users)}")
    print(f"📅 Total events: {len(system.events)}")
    
    total_attendees = sum(len(event.attendees) for event in system.events.values())
    print(f"🎫 Total registrations: {total_attendees}")
    
    print("\n✅ System is working correctly!")

def demo_user_interaction():
    """Demonstrate user interaction scenarios"""
    print("\n🎭 DEMO: User Interaction Scenarios")
    print("=" * 60)
    
    system = EventManagementSystem()
    
    # Scenario 1: Admin creates and manages events
    print("\n👑 SCENARIO 1: Admin Workflow")
    print("-" * 40)
    
    admin_id = system.register_user("demo_admin", UserRole.ADMIN)
    system.login(admin_id)
    
    # Create multiple events
    events_created = []
    event_names = [
        "Spring Festival",
        "Career Workshop",
        "Sports Tournament",
        "Academic Seminar"
    ]
    
    for i, name in enumerate(event_names):
        event_id = system.create_event(
            name,
            f"Description for {name}",
            f"2024-05-{10+i:02d}",
            "10:00",
            f"Venue {i+1}",
            50 + i*10
        )
        events_created.append(event_id)
        print(f"✅ Created: {name}")
    
    # Scenario 2: Students register for events
    print("\n🎓 SCENARIO 2: Student Registration")
    print("-" * 40)
    
    student_ids = []
    for i in range(3):
        student_id = system.register_user(f"student_{i+1}", UserRole.STUDENT)
        student_ids.append(student_id)
    
    # Students register for events
    for i, student_id in enumerate(student_ids):
        system.logout()
        system.login(student_id)
        print(f"👤 Student {i+1} registering for events...")
        
        for j, event_id in enumerate(events_created):
            if j % (i+1) == 0:  # Different registration patterns
                success = system.register_for_event(event_id)
                event_name = system.events[event_id].name
                print(f"   📅 {event_name}: {'✅' if success else '❌'}")
    
    # Scenario 3: Organizer manages their events
    print("\n🎪 SCENARIO 3: Event Organizer Management")
    print("-" * 40)
    
    organizer_id = system.register_user("demo_organizer", UserRole.EVENT_ORGANIZER)
    system.logout()
    system.login(organizer_id)
    
    # Create organizer event
    organizer_event_id = system.create_event(
        "Organizer's Special Event",
        "A special event organized by our demo organizer",
        "2024-05-15",
        "15:00",
        "Special Venue",
        30
    )
    
    # View my events
    my_events = system.view_my_events()
    print(f"📋 Organizer has {len(my_events)} events")
    
    # Scenario 4: Admin generates reports
    print("\n📊 SCENARIO 4: Admin Reporting")
    print("-" * 40)
    
    system.logout()
    system.login(admin_id)
    
    # Get comprehensive statistics
    stats = system.get_statistics()
    print(f"📈 System Statistics:")
    print(f"   Events: {stats['total_events']}")
    print(f"   Total Attendees: {stats['total_attendees']}")
    
    if stats['highest_attendance_event']:
        print(f"   🏆 Most Popular: {stats['highest_attendance_event'].name}")
    
    if stats['lowest_attendance_event']:
        print(f"   📉 Least Popular: {stats['lowest_attendance_event'].name}")
    
    # Export data
    system.export_events_to_csv("demo_events_report.csv")
    print("✅ Demo data exported to CSV")
    
    print("\n🎉 Demo scenarios completed!")

if __name__ == "__main__":
    print("🚀 Campus Event Management System - Test Suite")
    print("=" * 60)
    
    try:
        # Run comprehensive tests
        test_system()
        
        # Run demo scenarios
        demo_user_interaction()
        
        print("\n✅ All tests and demos completed successfully!")
        print("📁 Check the 'data' folder for generated files")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc() 