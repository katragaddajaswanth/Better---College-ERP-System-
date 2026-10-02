-- ============================================
-- COLLEGE ERP SYSTEM
-- SAMPLE DATA
-- ============================================

-- ============================================
-- DEPARTMENTS
-- ============================================

INSERT INTO department
(department_id, department_name)
VALUES
(1, 'Computer Science and Engineering');

INSERT INTO department
(department_id, department_name)
VALUES
(2, 'Electronics and Communication Engineering');

INSERT INTO department
(department_id, department_name)
VALUES
(3, 'Mechanical Engineering');


-- ============================================
-- STUDENTS
-- ============================================

INSERT INTO student
(student_id, student_name, email, phone, department_id, semester)
VALUES
('CSE001',
 'Jaswanth',
 'jaswanth@example.com',
 '9876543210',
 1,
 3);

INSERT INTO student
(student_id, student_name, email, phone, department_id, semester)
VALUES
('CSE002',
 'Rahul',
 'rahul@example.com',
 '9876543211',
 1,
 3);

INSERT INTO student
(student_id, student_name, email, phone, department_id, semester)
VALUES
('ECE001',
 'Arjun',
 'arjun@example.com',
 '9876543212',
 2,
 3);


-- ============================================
-- FACULTY
-- ============================================

INSERT INTO faculty
(faculty_id, faculty_name, email, department_id)
VALUES
('FAC001',
 'Dr. Kumar',
 'kumar@example.com',
 1);

INSERT INTO faculty
(faculty_id, faculty_name, email, department_id)
VALUES
('FAC002',
 'Dr. Priya',
 'priya@example.com',
 2);


-- ============================================
-- COURSES
-- ============================================

INSERT INTO course
(course_id, course_name, department_id, semester)
VALUES
('CS301',
 'Database Management Systems',
 1,
 3);

INSERT INTO course
(course_id, course_name, department_id, semester)
VALUES
('CS302',
 'Operating Systems',
 1,
 3);

INSERT INTO course
(course_id, course_name, department_id, semester)
VALUES
('CS303',
 'Computer Networks',
 1,
 3);

INSERT INTO course
(course_id, course_name, department_id, semester)
VALUES
('EC301',
 'Digital Electronics',
 2,
 3);


-- ============================================
-- ATTENDANCE
-- ============================================

INSERT INTO attendance
(student_id, course_id, attended_classes, total_classes)
VALUES
('CSE001', 'CS301', 42, 50);

INSERT INTO attendance
(student_id, course_id, attended_classes, total_classes)
VALUES
('CSE001', 'CS302', 38, 50);

INSERT INTO attendance
(student_id, course_id, attended_classes, total_classes)
VALUES
('CSE001', 'CS303', 45, 50);

INSERT INTO attendance
(student_id, course_id, attended_classes, total_classes)
VALUES
('CSE002', 'CS301', 40, 50);

INSERT INTO attendance
(student_id, course_id, attended_classes, total_classes)
VALUES
('CSE002', 'CS302', 44, 50);


-- ============================================
-- FEES
-- ============================================

INSERT INTO fees
(student_id, total_fee, paid_fee, pending_fee, payment_status)
VALUES
('CSE001', 100000, 75000, 25000, 'PENDING');

INSERT INTO fees
(student_id, total_fee, paid_fee, pending_fee, payment_status)
VALUES
('CSE002', 100000, 100000, 0, 'PAID');

INSERT INTO fees
(student_id, total_fee, paid_fee, pending_fee, payment_status)
VALUES
('ECE001', 95000, 70000, 25000, 'PENDING');


-- ============================================
-- RESULTS
-- ============================================

INSERT INTO results
(student_id, course_id, marks, grade, result_status)
VALUES
('CSE001', 'CS301', 85, 'A', 'PASS');

INSERT INTO results
(student_id, course_id, marks, grade, result_status)
VALUES
('CSE001', 'CS302', 78, 'B+', 'PASS');

INSERT INTO results
(student_id, course_id, marks, grade, result_status)
VALUES
('CSE001', 'CS303', 91, 'A+', 'PASS');

INSERT INTO results
(student_id, course_id, marks, grade, result_status)
VALUES
('CSE002', 'CS301', 72, 'B+', 'PASS');

INSERT INTO results
(student_id, course_id, marks, grade, result_status)
VALUES
('CSE002', 'CS302', 65, 'B', 'PASS');


-- ============================================
-- NOTICES
-- ============================================

INSERT INTO notices
(title, description, notice_date)
VALUES
(
    'Semester Examination',
    'Semester examinations will begin from next month.',
    SYSDATE
);

INSERT INTO notices
(title, description, notice_date)
VALUES
(
    'Fee Payment',
    'Students are requested to clear pending fee payments.',
    SYSDATE
);

INSERT INTO notices
(title, description, notice_date)
VALUES
(
    'Result Announcement',
    'Semester results are now available through the ERP portal.',
    SYSDATE
);

INSERT INTO notices
(title, description, notice_date)
VALUES
(
    'Academic Calendar',
    'The updated academic calendar has been published.',
    SYSDATE
);


-- ============================================
-- LOGIN USERS
-- ============================================

-- Student
INSERT INTO users
(username, password, role, student_id)
VALUES
('CSE001', '1234', 'STUDENT', 'CSE001');

INSERT INTO users
(username, password, role, student_id)
VALUES
('CSE002', '1234', 'STUDENT', 'CSE002');

-- Faculty
INSERT INTO users
(username, password, role, student_id)
VALUES
('faculty', '1234', 'FACULTY', NULL);

-- Admin
INSERT INTO users
(username, password, role, student_id)
VALUES
('admin', 'admin123', 'ADMIN', NULL);

COMMIT;

PROMPT ============================================
PROMPT SAMPLE DATA INSERTED SUCCESSFULLY
PROMPT ============================================

SELECT 'Departments' AS table_name, COUNT(*) AS records
FROM department
UNION ALL
SELECT 'Students', COUNT(*)
FROM student
UNION ALL
SELECT 'Faculty', COUNT(*)
FROM faculty
UNION ALL
SELECT 'Courses', COUNT(*)
FROM course
UNION ALL
SELECT 'Attendance', COUNT(*)
FROM attendance
UNION ALL
SELECT 'Fees', COUNT(*)
FROM fees
UNION ALL
SELECT 'Results', COUNT(*)
FROM results
UNION ALL
SELECT 'Notices', COUNT(*)
FROM notices
UNION ALL
SELECT 'Users', COUNT(*)
FROM users;