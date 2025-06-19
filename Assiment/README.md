# Campus Event Management System

## Overview
A comprehensive Python-based Campus Event Management System with role-based access control, designed to manage campus events, handle attendee registration, and provide detailed reporting capabilities.

## Features

### 🔐 Role-Based Access Control
- **Admin**: Full system access - create, update, delete events, view all data, export reports
- **Event Organizer**: Manage their own events, view attendees, export attendee lists
- **Student/Visitor**: Search events, register/unregister, view personal event history

### 📅 Event Management
- Create, update, and delete events
- Track event capacity and attendance
- Input validation for all event fields
- Date and time management
- Location tracking

### 👥 Attendee Management
- Register attendees with capacity checks
- Prevent duplicate registrations
- Confirmation messages for successful operations
- Attendee list management

### 📊 Reporting & Analytics
- Total attendees across all events
- Events with highest and lowest attendance
- Statistical reports
- Data export to CSV format

### 💾 Data Persistence
- JSON-based data storage
- Automatic data loading and saving
- Backup and restore capabilities

## System Architecture

### Core Classes

#### 1. User Class
```python
class User:
    - user_id: str
    - username: str
    - role: UserRole (ADMIN, EVENT_ORGANIZER, STUDENT, VISITOR)
    - email: str
    - created_events: List[str]
    - registered_events: List[str]
```

#### 2. Event Class
```python
class Event:
    - event_id: str
    - name: str
    - description: str
    - date: str
    - time: str
    - location: str
    - max_capacity: int
    - organizer_id: str
    - attendees: List[str]
    - created_at: str
```

#### 3. EventManagementSystem Class
Main system controller with methods for:
- User management (register, login, logout)
- Event management (CRUD operations)
- Attendee registration
- Data persistence
- Reporting and analytics

#### 4. EventManagementUI Class
User interface layer providing:
- Menu-driven navigation
- Input validation
- User-friendly error messages
- Role-specific menus

## Installation & Usage

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Running the System
```bash
python event_management_system.py
```

### Demo Data
The system comes with pre-loaded demo data:
- **Admin**: admin (User ID: user_1)
- **Event Organizer**: organizer1 (User ID: user_2)
- **Student**: student1 (User ID: user_3)
- **Visitor**: visitor1 (User ID: user_4)

## User Workflows

### Admin Workflow
1. Login with admin credentials
2. Create, update, or delete events
3. View all events and attendees
4. Generate statistics and reports
5. Export data to CSV files

### Event Organizer Workflow
1. Login with organizer credentials
2. Create new events
3. View events they've created
4. Check attendee lists
5. Export attendee data

### Student/Visitor Workflow
1. Login with student/visitor credentials
2. Search for available events
3. Register for events of interest
4. View registered events
5. Unregister if needed

## Data Storage

### File Structure
```
data/
├── users.json          # User data
├── events.json         # Event data
├── events_report.csv   # Exported events report
└── attendees_*.csv     # Exported attendee reports
```

### Data Format
- **JSON**: Primary data storage for users and events
- **CSV**: Export format for reports and analytics

## Security Features

### Access Control
- Role-based permissions
- Input validation
- Data integrity checks
- Secure file operations

### Data Validation
- Date format validation (YYYY-MM-DD)
- Time format validation (HH:MM)
- Capacity validation (positive integers)
- Required field validation

## Error Handling

### User-Friendly Messages
- Clear error descriptions
- Actionable feedback
- Graceful failure handling

### Data Protection
- Automatic data saving
- File operation error handling
- Data corruption prevention

## Extensibility

### Adding New Features
The modular design allows easy extension:
- New user roles
- Additional event attributes
- Enhanced reporting
- Integration with external systems

### Customization
- Modify menu structures
- Add new validation rules
- Custom export formats
- Additional statistics

## Performance Considerations

### Scalability
- Efficient data structures
- Minimal memory usage
- Fast search operations
- Optimized file I/O

### Data Management
- Automatic data persistence
- Efficient JSON serialization
- Minimal disk space usage

## Testing

### Manual Testing Scenarios
1. **User Registration**: Test all role types
2. **Event Creation**: Validate all fields
3. **Registration Process**: Test capacity limits
4. **Data Export**: Verify CSV output
5. **Error Handling**: Test invalid inputs

### Sample Test Cases
- Create event with invalid date
- Register for full event
- Export data with no events
- Login with invalid user ID

## Troubleshooting

### Common Issues
1. **File Permission Errors**: Ensure write access to data directory
2. **Invalid Date Format**: Use YYYY-MM-DD format
3. **Capacity Issues**: Enter positive integers only
4. **Login Problems**: Use correct User ID format

### Data Recovery
- Automatic backup through JSON files
- Manual data restoration possible
- Data integrity checks

## Future Enhancements

### Planned Features
- Email notifications
- Event categories and tags
- Advanced search filters
- Calendar integration
- Mobile app interface
- Real-time updates
- Multi-language support

### Technical Improvements
- Database integration (SQLite/PostgreSQL)
- Web interface (Flask/Django)
- API endpoints
- Authentication system
- Data encryption

## Contributing

### Development Guidelines
- Follow PEP 8 style guide
- Add comprehensive comments
- Include error handling
- Test all new features
- Update documentation

### Code Structure
- Modular design
- Clear separation of concerns
- Consistent naming conventions
- Proper exception handling

## License

This project is open source and available under the MIT License.

## Support

For questions or issues:
1. Check the troubleshooting section
2. Review the code comments
3. Test with demo data
4. Verify file permissions

---

**Note**: This system is designed for educational purposes and demonstrates advanced Python programming concepts including OOP, file handling, data persistence, and user interface design. 