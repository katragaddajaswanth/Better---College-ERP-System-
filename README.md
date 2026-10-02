# College ERP Management System

A modern, secure, and student-focused **College Enterprise Resource Planning (ERP) System** designed to improve the traditional college ERP experience through a cleaner interface, centralized data access, personalized dashboards, and protected student information.

The project combines **Flask, Oracle Database, HTML, CSS, and JavaScript** to provide a scalable foundation for managing academic and administrative services.

---

## 📌 Project Overview

Traditional college ERP systems often contain multiple disconnected modules, complex navigation, and interfaces that are difficult for students to use.

This project redesigns the conventional ERP approach by focusing on:

* Simplicity
* Better user experience
* Secure student access
* Centralized academic information
* Personalized dashboards
* Responsive design
* Clear separation between public and private information

Instead of exposing student information through publicly accessible forms, the system is designed around **authenticated, student-specific access**.

---

## ✨ Major Changes From a Traditional ERP

### 1. Modern Student-Centric Interface

The traditional ERP-style interface has been redesigned into a cleaner and more approachable web experience.

The UI uses an **Autumn Luxe-inspired light color palette** with:

* Warm cream backgrounds
* Off-white cards
* Terracotta/copper accents
* Dark warm-brown typography
* Soft borders and shadows

The goal is to make the ERP feel more like a modern web application rather than a conventional administrative portal.

---

### 2. Personalized Student Dashboard

Instead of requiring students to repeatedly enter their Student ID, the system uses the authenticated user's session to identify the student.

The dashboard can provide:

* Student name
* Student ID
* Department
* Semester
* Email
* Phone
* Attendance summary
* Fee summary
* Result summary
* Recent notices
* Quick access to student services

This creates a more personalized experience and reduces unnecessary data entry.

---

### 3. Secure Student Data Access

One of the major architectural improvements is moving away from publicly accessible Student ID-based queries.

Previously, a student could enter a Student ID to retrieve information such as attendance or fees.

The improved architecture is designed so that:

```text
Login
   ↓
Authenticated Session
   ↓
Student ID obtained from session
   ↓
Student-specific database query
   ↓
Personalized information
```

This prevents users from simply changing a Student ID in a form to attempt to access another student's information.

---

### 4. Authentication and Role-Based Access

The system includes an authentication layer using the `users` table.

Supported roles include:

* **STUDENT**
* **FACULTY**
* **ADMIN**

The architecture is designed to allow each role to have its own protected functionality.

For example:

```text
STUDENT
 └── Student Dashboard
     ├── Attendance
     ├── Fees
     ├── Results
     └── Notices

FACULTY
 └── Faculty Portal
     ├── Courses
     ├── Attendance
     └── Results

ADMIN
 └── Admin Portal
     ├── Students
     ├── Faculty
     ├── Courses
     ├── Fees
     └── Notices
```

---

## 🏠 Improved Home Page

The public home page was redesigned to act as the main entry point of the ERP.

It contains:

* College ERP branding
* Hero section
* Clear navigation
* Latest notices
* Quick Services
* Student Login
* ERP information
* Responsive layout

### Quick Services

The main page focuses on the most frequently required student services:

* 📊 Attendance
* 💰 Fee Details
* 🔐 Student Login

Results and other personal information are intended to remain inside the authenticated portal.

This creates a clear distinction between **public information** and **private student information**.

---

## 📢 Dynamic Notice System

College notices are stored in the Oracle database rather than being hard-coded into the webpage.

The frontend retrieves notices through:

```text
GET /api/notices
```

The system dynamically displays:

* Notice title
* Description
* Notice date

Notices are ordered by the latest date, allowing important announcements to appear first.

This means administrators can eventually manage notices from an admin portal without modifying the frontend code.

---

## 📊 Attendance Management

The attendance module retrieves course-wise attendance information from Oracle.

It provides:

* Course name
* Classes attended
* Total classes
* Attendance percentage

The percentage is calculated dynamically:

```text
Attendance % = (Attended Classes / Total Classes) × 100
```

The system also handles cases where total classes are zero.

---

## 💰 Fee Management

The fee module provides a structured overview of a student's financial information.

It displays:

* Total fee
* Paid fee
* Pending fee
* Payment status

This creates a clearer alternative to manually checking financial records through a traditional ERP interface.

---

## 🎓 Result Management

The results module provides authenticated access to academic results.

Students can view:

* Course name
* Marks
* Grade
* Result status

Results are retrieved directly from Oracle through the Flask backend.

---

## 🔐 Login System

The application includes a dedicated login page and authentication API.

### Login Flow

```text
Username + Password
        ↓
     Flask API
        ↓
    Oracle Users
        ↓
Authentication
        ↓
Session Created
        ↓
Dashboard
```

The Flask session stores relevant authenticated-user information, including:

* Username
* Role
* Student ID

This allows the application to identify the logged-in student without repeatedly requesting their Student ID.

---

## 🗄️ Database Architecture

The system uses Oracle Database as the central data layer.

### Main Tables

| Table        | Purpose                                    |
| ------------ | ------------------------------------------ |
| `department` | Stores department information              |
| `student`    | Stores student information                 |
| `faculty`    | Stores faculty information                 |
| `course`     | Stores course information                  |
| `attendance` | Stores student attendance                  |
| `fees`       | Stores student fee information             |
| `results`    | Stores academic results                    |
| `notices`    | Stores college announcements               |
| `users`      | Stores authentication and role information |

Relationships between these tables allow the application to retrieve meaningful information through SQL joins.

---

## 🔗 Backend API Structure

The Flask backend provides routes for both webpages and API operations.

### Main Pages

```text
/
 /login
 /dashboard
 /attendance
 /fees
 /results
 /logout
```

### API Endpoints

```text
POST /api/login
POST /api/attendance
POST /api/fees
POST /api/results
GET  /api/notices
```

The API-based structure separates frontend presentation from backend database operations and makes the system easier to extend.

---

## 🎨 Frontend Improvements

The frontend was redesigned with reusable styling and responsive layouts.

Important UI improvements include:

* Consistent navigation
* Responsive cards
* Improved forms
* Better spacing
* Modern buttons
* Interactive hover states
* Responsive tables
* Mobile-friendly layouts
* Consistent color system
* Cleaner typography
* Improved visual hierarchy

The design intentionally avoids an overly dark enterprise interface and instead uses a lighter, professional academic theme.

---

## 📱 Responsive Design

The interface includes responsive CSS rules for different screen sizes.

The application is designed to remain usable on:

* Desktop
* Laptop
* Tablet
* Mobile

Navigation, cards, forms, and tables adapt to smaller screens.

---

## 🧩 Technical Architecture

```text
┌──────────────────────────┐
│       Frontend           │
│ HTML + CSS + JavaScript  │
└────────────┬─────────────┘
             │
             │ HTTP / JSON
             ▼
┌──────────────────────────┐
│       Flask Backend      │
│ Routes + Authentication  │
│ API + Business Logic     │
└────────────┬─────────────┘
             │
             │ SQL
             ▼
┌──────────────────────────┐
│      Oracle Database     │
│ Students • Faculty       │
│ Courses • Attendance     │
│ Fees • Results • Notices │
│ Users                    │
└──────────────────────────┘
```

---

## 🛡️ Security Improvements

Security is an important part of the planned production architecture.

The system is being moved toward:

* Session-based authentication
* Protected dashboards
* Role-based access
* Student-specific database queries
* Password hashing
* HTTP-only session cookies
* Secure session configuration
* Environment-based secrets
* Production error handling
* Login rate limiting
* HTTPS deployment

The key principle is:

> **A student's identity should come from their authenticated session, not from an ID supplied by the browser.**

---

## 🚀 Future Enhancements

The current architecture provides a foundation for additional ERP modules.

### Student Portal

* Profile editing
* Password change
* Attendance alerts
* Result downloads
* Fee receipts
* Academic calendar
* Notifications

### Faculty Portal

* Faculty dashboard
* Student attendance entry
* Attendance editing
* Marks entry
* Result publishing
* Course management

### Admin Portal

* Student management
* Faculty management
* Department management
* Course management
* Fee management
* Notice management
* User management
* Reports and analytics

### Advanced Features

Future versions can also include:

* Online fee payment
* Email notifications
* PDF report generation
* Excel exports
* Attendance alerts
* Result analytics
* Audit logs
* Password reset
* Multi-semester support
* Search and filtering
* Administrative analytics

---

## 🛠️ Technology Stack

| Technology                 | Purpose                                    |
| -------------------------- | ------------------------------------------ |
| **Python**                 | Backend programming                        |
| **Flask**                  | Web framework                              |
| **Oracle Database**        | Database management                        |
| **HTML5**                  | Page structure                             |
| **CSS3**                   | UI and responsive design                   |
| **JavaScript**             | Frontend interaction and API communication |
| **Jinja2**                 | Dynamic HTML rendering                     |
| **OracleDB Python Driver** | Flask–Oracle connectivity                  |
| **VS Code**                | Development environment                    |

---

## 📁 Project Structure

```text
College-ERP/
│
├── app.py
├── db.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── attendance.html
│   ├── fees.html
│   └── results.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd College-ERP
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Oracle Database

Create the required Oracle tables and configure the database connection in `db.py`.

The database should contain:

```text
department
student
faculty
course
attendance
fees
results
notices
users
```

### 6. Run the application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## 🔑 Important Deployment Considerations

Before deploying the application publicly, development configuration should be replaced with production configuration.

In particular:

* Do not hard-code the Flask secret key.
* Do not store plain-text passwords.
* Store database credentials in environment variables.
* Disable Flask debug mode.
* Enable secure cookies when HTTPS is available.
* Use production-grade WSGI hosting.
* Do not expose database error messages to users.
* Add CSRF protection where appropriate.
* Add login rate limiting.
* Validate all incoming data.
* Restrict access to student-specific resources.

---

## 🎯 Project Goal

The goal of this project is not simply to reproduce a conventional ERP system.

It is to **modernize the ERP experience** by combining the functionality of a traditional college management system with:

> **Security + Personalization + Simplicity + Modern UI + Centralized Data**

The result is a foundation for a scalable College ERP platform that can evolve from a student-focused academic portal into a complete institution-wide management system.

---

## 👨‍💻 Project Status

**Current Status:** Active Development

### Completed / Implemented

* [x] Flask backend
* [x] Oracle database integration
* [x] Student database
* [x] Faculty database
* [x] Department database
* [x] Course database
* [x] Attendance module
* [x] Fee module
* [x] Results module
* [x] Notice module
* [x] User authentication
* [x] Session-based dashboard
* [x] Responsive frontend
* [x] Modernized home page
* [x] Student-focused navigation
* [x] Dynamic API-driven data
* [x] Foundation for role-based portals
* [ ] Production security hardening
* [ ] Faculty portal
* [ ] Admin portal
* [ ] Online payment integration
* [ ] Advanced reporting

---

## 📄 License

This project is intended for educational and institutional ERP development purposes. Add an appropriate open-source or institutional license before public distribution.
