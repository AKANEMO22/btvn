# Installation and Setup Guide

## Quick Start

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Installation Steps

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd Campus-Event-Management-System
   
   # Or simply download and extract the files
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # Should show Python 3.7 or higher
   ```

3. **Run the System**
   ```bash
   python event_management_system.py
   ```

4. **Run Tests (Optional)**
   ```bash
   python test_system.py
   ```

## File Structure

```
Campus-Event-Management-System/
├── event_management_system.py    # Main system file
├── test_system.py               # Test and demo script
├── README.md                    # Comprehensive documentation
├── flowchart.md                 # System flowchart
├── requirements.txt             # Dependencies (none required)
├── INSTALL.md                   # This file
└── data/                        # Data directory (created automatically)
    ├── users.json              # User data
    ├── events.json             # Event data
    └── *.csv                   # Exported reports
```

## Demo Data

The system comes with pre-loaded demo users:

| Role | Username | User ID | Email |
|------|----------|---------|-------|
| Admin | admin | user_1 | admin@campus.edu |
| Event Organizer | organizer1 | user_2 | organizer1@campus.edu |
| Student | student1 | user_3 | student1@campus.edu |
| Visitor | visitor1 | user_4 | visitor1@campus.edu |

## First Time Setup

1. **Start the System**
   ```bash
   python event_management_system.py
   ```

2. **Login with Demo Account**
   - Choose option 1 (Login)
   - Enter User ID: `user_1` (for admin access)
   - Explore the admin menu

3. **Create Your Own Account**
   - Choose option 2 (Register New User)
   - Enter your details
   - Select your role
   - Note your User ID for future logins

## Usage Examples

### Admin Workflow
```bash
# Login as admin
User ID: user_1

# Create an event
1. Choose "Create Event"
2. Enter event details
3. Confirm creation

# View statistics
1. Choose "View Statistics"
2. Review system metrics

# Export data
1. Choose "Export Events to CSV"
2. Check data/ folder for files
```

### Student Workflow
```bash
# Login as student
User ID: user_3

# Search for events
1. Choose "Search Events"
2. Enter keywords
3. View results

# Register for event
1. Choose "Register for Event"
2. Enter Event ID
3. Confirm registration
```

## Troubleshooting

### Common Issues

1. **Python Not Found**
   ```bash
   # Try these commands:
   python3 event_management_system.py
   # or
   py event_management_system.py
   ```

2. **Permission Errors**
   ```bash
   # Ensure write permissions in the directory
   # On Windows, run as administrator if needed
   # On Linux/Mac:
   chmod +x event_management_system.py
   ```

3. **File Not Found**
   ```bash
   # Ensure you're in the correct directory
   ls  # or dir on Windows
   # Should show event_management_system.py
   ```

4. **Data Directory Issues**
   ```bash
   # The system creates data/ automatically
   # If issues persist, create manually:
   mkdir data
   ```

### Error Messages

- **"Access denied"**: You don't have permission for this action
- **"Event not found"**: Invalid Event ID entered
- **"Event is at full capacity"**: No more registrations allowed
- **"You are already registered"**: Duplicate registration attempt

## Advanced Setup

### Custom Configuration

1. **Modify Demo Data**
   - Edit the `setup_demo_data()` method in `event_management_system.py`
   - Add your own users and events

2. **Change Data Directory**
   - Modify `self.data_dir` in `EventManagementSystem.__init__()`
   - Ensure the directory exists and is writable

3. **Add New Roles**
   - Extend the `UserRole` enum
   - Update menu logic in `EventManagementUI`

### Development Setup

1. **Install Development Tools**
   ```bash
   # Optional: Install testing framework
   pip install pytest
   
   # Optional: Install code formatter
   pip install black
   ```

2. **Run Tests**
   ```bash
   python test_system.py
   ```

3. **Code Quality**
   ```bash
   # Format code (if black is installed)
   black event_management_system.py
   ```

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.7 or higher
- **RAM**: 128 MB
- **Storage**: 10 MB free space

### Recommended Requirements
- **OS**: Windows 11, macOS 12+, or Ubuntu 20.04+
- **Python**: 3.9 or higher
- **RAM**: 512 MB
- **Storage**: 100 MB free space

## Security Notes

1. **Data Storage**: All data is stored locally in JSON format
2. **No Network**: The system operates entirely offline
3. **File Permissions**: Ensure proper file permissions for data directory
4. **Backup**: Regularly backup the `data/` directory

## Support

For issues or questions:

1. Check the troubleshooting section above
2. Review the README.md for detailed documentation
3. Run the test script to verify system functionality
4. Check the data/ directory for any error logs

## License

This project is open source and available under the MIT License.

---

**Note**: This system is designed for educational purposes and demonstrates advanced Python programming concepts. For production use, consider implementing additional security measures and database integration. 