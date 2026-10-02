-- ============================================
-- COLLEGE ERP SYSTEM
-- DATABASE INDEXES
-- ============================================

-- ============================================
-- STUDENT INDEXES
-- ============================================

CREATE INDEX idx_student_department
ON student(department_id);


-- ============================================
-- FACULTY INDEXES
-- ============================================

CREATE INDEX idx_faculty_department
ON faculty(department_id);


-- ============================================
-- COURSE INDEXES
-- ============================================

CREATE INDEX idx_course_department
ON course(department_id);

CREATE INDEX idx_course_semester
ON course(semester);


-- ============================================
-- ATTENDANCE INDEXES
-- ============================================

CREATE INDEX idx_attendance_student
ON attendance(student_id);

CREATE INDEX idx_attendance_course
ON attendance(course_id);

CREATE INDEX idx_attendance_student_course
ON attendance(student_id, course_id);


-- ============================================
-- FEES INDEXES
-- ============================================

CREATE INDEX idx_fees_student
ON fees(student_id);

CREATE INDEX idx_fees_status
ON fees(payment_status);


-- ============================================
-- RESULTS INDEXES
-- ============================================

CREATE INDEX idx_results_student
ON results(student_id);

CREATE INDEX idx_results_course
ON results(course_id);

CREATE INDEX idx_results_student_course
ON results(student_id, course_id);


-- ============================================
-- NOTICES INDEXES
-- ============================================

CREATE INDEX idx_notices_date
ON notices(notice_date);


-- ============================================
-- USERS INDEXES
-- ============================================

CREATE INDEX idx_users_student
ON users(student_id);

CREATE INDEX idx_users_role
ON users(role);

COMMIT;

PROMPT ============================================
PROMPT DATABASE INDEXES CREATED SUCCESSFULLY
PROMPT ============================================